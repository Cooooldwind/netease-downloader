# PySide6
from PySide6.QtCore import QObject, QThread, Signal, QMutex

# netease_encode_api
from netease_encode_api import EncodeSession

# class163
from class163 import Search, Playlist, Music
from class163.common import artist_join
from class163.global_args import SEARCH_TYPE

# typing
from typing import Dict, List, Union

# other
import time

# internal
from model.global_args import SEARCH_MODE

# p.s. SingleMusicSearchModel缩写: smsm
class SingleMusicSearchModel(QThread):

    result_signal = Signal(Music)

    def __init__(self, music: Music, encode_session: EncodeSession) -> None:
        super().__init__()
        self.music = music
        self.encode_session = encode_session

    def run(self):
        self.music.get_detail(encode_session=self.encode_session)
        if self.music.cover_file_url != None:
            self.music.set_cover_size(64)
            self.music.cover_file.begin_download()
        self.result_signal.emit(self.music)


class SearchModel(QThread):

    result_signal = Signal(dict)

    def __init__(
        self,
        encode_session: EncodeSession,
        key: str,
        search_mode: SEARCH_MODE,
        parent: QObject | None = ...,
    ) -> None:
        super().__init__(parent)
        self.encode_session = encode_session
        self.key: str = key
        self.search_mode: SEARCH_MODE = search_mode
        self.instance: Union[Search, Playlist, Music] = None
        # 判断不同类型创建实例
        if self.search_mode == "search_playlist" or self.search_mode == "search_song":
            self.instance = Search(
                key=key,
                search_type="song" if self.search_mode == "search_song" else "playlist",
                encode_session=self.encode_session,
            )
            self.instance.encode_session = self.encode_session
        elif self.search_mode == "playlist":
            self.instance = Playlist(key)
            self.instance.encode_session = self.encode_session
        else:
            self.instance = Music(key)
            self.instance.encode_session = self.encode_session
        # 结果在这里
        self.result_list: list[Music, Playlist] = []
        self.smsm_cnt = 0
        self.smsm_list: list[SingleMusicSearchModel] = []
        # 互斥锁
        self.mutex = QMutex()
        self.active_threads = 0
        self.max_threads = 4

    def initialize_and_ending_dict(self, initialize: bool = True):
        if initialize:
            initialize_dict = {
                "mode": "initialize",
                "search_mode": self.search_mode,
                "title": (
                    self.instance.title
                    if self.search_mode == "playlist" or self.search_mode == "song"
                    else self.key
                ),
                "tot": (
                    self.instance.result_count
                    if self.search_mode == "search_playlist"
                    or self.search_mode == "search_song"
                    else self.instance.track_count if self.search_mode == "playlist" else 1
                ),
                "creator": (
                    self.instance.creator if self.search_mode == "playlist" else None
                ),
            }
            return initialize_dict
        else:
            ending_dict = {
                "mode": "ending",
                "search_mode": self.search_mode,
                "title": (
                    self.instance.title
                    if self.search_mode == "playlist" or self.search_mode == "song"
                    else self.key
                ),
                "tot": (
                    self.instance.result_count
                    if self.search_mode == "search_playlist"
                    or self.search_mode == "search_song"
                    else self.instance.track_count if self.search_mode == "playlist" else 1
                ),
                "creator": (
                    self.instance.creator if self.search_mode == "playlist" else None
                ),
            }
            return ending_dict
            

    def run(self):
        # 判断不同类型运行实例
        if self.search_mode == "search_playlist" or self.search_mode == "search_song":
            self.instance.get()
            self.result_list = self.instance.search_result_sorted
        elif self.search_mode == "playlist":
            self.instance.get_detail(each_music=False)
            self.result_list = self.instance.track
        else:
            self.instance.get_detail()
            self.result_list = [self.instance]
        # 返回初始化信号
        initialize_dict = self.initialize_and_ending_dict(initialize = True)
        self.result_signal.emit(initialize_dict)
        # 搜索里面的歌曲
        if self.search_mode != "search_playlist":
            for i in self.result_list:
                i = Music(i.id)
                smsm = SingleMusicSearchModel(i, self.encode_session)
                smsm.result_signal.connect(self.edit_music)
                self.smsm_list.append(smsm)
            for smsm in self.smsm_list:
                if self.active_threads < self.max_threads:
                    smsm.start()
                    self.active_threads += 1
                else:
                    # Wait for a thread to finish before starting the next one.
                    while self.active_threads >= self.max_threads:
                        time.sleep(0.1)
                    smsm.start()
                    self.active_threads += 1
            for smsm in self.smsm_list:
                smsm.wait()


    def edit_music(self, i: Music):
        edit_dict = {
            "mode": "edit",
            "item": "music",
            "search_mode": self.search_mode,
            "title": i.title,
            "artist": artist_join(i.artist, "/"),
            "album": i.album,
            "index": self.smsm_cnt,
            "tot": len(self.result_list),
            "cover": i.cover_file.get_data() if i.cover_file.tot_size > 0 else None,
            "sub_title": i.subtitle if i.subtitle != None else "",
            "trans_title": i.trans_title if i.trans_title != None else "",
        }
        if self.search_mode == "search_song":
            edit_dict.update(
                {
                    "key": self.key,
                }
            )
        elif self.search_mode == "playlist":
            edit_dict.update(
                {
                    "playlist_title": self.instance.title,
                    "creator": self.instance.creator,
                }
            )
        self.result_signal.emit(edit_dict)
        self.mutex.lock()
        self.smsm_cnt += 1
        self.active_threads -= 1
        self.mutex.unlock()
        # 结束的信号
        if self.smsm_cnt == len(self.result_list):
            ending_dict = self.initialize_and_ending_dict(initialize = False)
            self.result_signal.emit(ending_dict)
