from class163 import Search, Playlist, Music
from class163.common import artist_join
from class163.global_args import SEARCH_TYPE
from netease_encode_api import EncodeSession
from PySide6.QtCore import Slot, Signal, QObject, QThread
from typing import Dict, Union

from module.global_args import SEARCH_MODE


class SearchResult(QThread):
    search_signal = Signal(dict)

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.key = None
        self.type = None
        self.search_type = None
        self.instance: Union[Search, Playlist, Music] = None
        self.encode_session: EncodeSession = None

    def set_attribute(
        self,
        key: str,
        mode: SEARCH_MODE,
        search_type: SEARCH_TYPE = "song",
        encode_session: EncodeSession = EncodeSession(),
    ):
        self.type = mode
        if self.type == "search_playlist" or self.type == "search_song":
            self.encode_session = encode_session
            self.key, self.type = key, search_type
            self.instance = Search(
                key=self.key,
                search_type=self.search_type,
                encode_session=self.encode_session,
            )
        elif self.type == "playlist":
            self.encode_session = encode_session
            self.key = key
            self.instance = Playlist(self.key)
            self.instance.encode_session = self.encode_session
        elif self.type == "song":
            self.encode_session = encode_session
            self.key = key
            self.instance = Music(self.key)
            self.instance.encode_session = self.encode_session
        return None

    def run(self): self.get()

    def get(self):
        if self.type == "playlist":
            self.instance.get_detail(each_music=False)
            initialize_result = {
                "mode": "initialize",
                "cnt": self.instance.track_count,
                "playlist_title": self.instance.title,
                "playlist_creator": self.instance.creator,
            }
            self.search_signal.emit(initialize_result)
            cnt = 0
            for i in self.instance.track:
                if i.cover_file_url == None:
                    i.get_detail(encode_session=self.encode_session)
                i.set_cover_size(64)
                no_cover = False
                try: i.cover_file.begin_download()
                except: 
                    no_cover = True
                    pass
                result_dict = {
                    "mode": "edit_table",
                    "playlist_title": self.instance.title,
                    "playlist_creator": self.instance.creator,
                    "title": i.title,
                    "cnt": cnt,
                    "artist": artist_join(i.artist, "/"),
                    "album": i.album,
                    "sub_title": i.subtitle if i.subtitle != None else "",
                    "trans_title": i.trans_title if i.trans_title != None else "",
                    "cover": i.cover_file.get_data(),
                    "tot_cnt": self.instance.track_count,
                }
                self.search_signal.emit(result_dict)
                cnt += 1
            ending_result = {
                "mode": "ending",
                "cnt": self.instance.track_count,
                "playlist_title": self.instance.title,
                "playlist_creator": self.instance.creator,
            }
            self.search_signal.emit(ending_result)
