# PySide6
from PySide6.QtCore import QObject, QThread, Signal

# netease_encode_api
from netease_encode_api import EncodeSession

# class163
from class163 import Search, Playlist, Music
from class163.common import artist_join
from class163.global_args import SEARCH_TYPE

# typing
from typing import Dict, List, Union

# internal
from model.global_args import SEARCH_MODE


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
            "creator": self.instance.creator if self.search_mode == "playlist" else None,
        }
        self.result_signal.emit(initialize_dict)
        if self.search_mode == "search_song":
            cnt = 0
            for i in self.instance.search_result_sorted:
                i = Music(i.id)
                i.get_detail(encode_session=self.encode_session)
                if i.cover_file_url != None: 
                    i.set_cover_size(64)
                    i.cover_file.begin_download()
                edit_dict = {
                    "mode": "edit",
                    "item": "music",
                    "search_mode": self.search_mode,
                    "title": i.title,
                    "artist": artist_join(i.artist, "/"),
                    "album": i.album,
                    "index": cnt,
                    "tot": self.instance.result_count,
                    "cover": i.cover_file.get_data(),
                    "sub_title": i.subtitle if i.subtitle != None else "",
                    "trans_title": i.trans_title if i.trans_title != None else "",
                    "key": self.key,
                }
                self.result_signal.emit(edit_dict)
                cnt += 1
            ending_dict = {
                "mode": "ending",
                "title": self.key,
            }
            self.result_signal.emit(ending_dict)
        elif self.search_mode == "playlist":
            cnt = 0
            for i in self.instance.track:
                i = Music(i.id)
                i.get_detail(encode_session=self.encode_session)
                if i.cover_file_url != None: 
                    i.set_cover_size(64)
                    i.cover_file.begin_download()
                edit_dict = {
                    "mode": "edit",
                    "item": "music",
                    "search_mode": self.search_mode,
                    "title": i.title,
                    "artist": artist_join(i.artist, "/"),
                    "album": i.album,
                    "index": cnt,
                    "tot": self.instance.track_count,
                    "cover": i.cover_file.get_data(),
                    "sub_title": i.subtitle if i.subtitle != None else "",
                    "trans_title": i.trans_title if i.trans_title != None else "",
                    "playlist_title": self.instance.title,
                    "creator": self.instance.creator
                }
                self.result_signal.emit(edit_dict)
                cnt += 1
            ending_dict = {
                "mode": "ending",
                "title": self.instance.title,
            }
            self.result_signal.emit(ending_dict)
