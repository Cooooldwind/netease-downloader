from netease_encode_api import EncodeSession
from class163 import Playlist, Music, Search
from typing import Union, Dict, List
from global_args import SEARCH_MODE


class SearchResultModel:
    def __init__(self) -> None:
        self.mode: SEARCH_MODE = "playlist_id"
        self.id: str = ""
        self.key: str = ""
        self.encode_session = EncodeSession()
        self.result_list: list[Union[Music, None]] = []
        self.result_dict: Dict = {}

    def get_info(self):
        if self.mode == "playlist_id":
            playlist = Playlist(self.id)
            print(self.id)
            playlist.get_detail(each_music=True, session=self.encode_session)
            self.result_list = playlist.track
            self.result_dict = playlist.info_dict()
            return None
        if self.mode == "search_playlist":
            pass
            return None
        if self.mode == "search_song":
            pass
            return None
        if self.mode == "song_id":
            pass
            return None