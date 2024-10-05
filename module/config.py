from class163.global_args import LEVEL

from module.global_args import SEARCH_MODE

class Config:
    def __init__(self):
        self.search_mode: SEARCH_MODE = "song"
        self.level: LEVEL = "standard"
        self.cover_download, self.cover_write, self.lyric_download, self.arrtibute_write = False, False, False, False
        self.lyric_encoding = "UTF-8"
        self.cookies = {}
        self.cover_size = 1000
        self.third_party_config = {}