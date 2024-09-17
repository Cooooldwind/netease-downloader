from PySide6.QtCore import Slot, Signal, QObject, SignalInstance, QThread

# from ui import MainWindow
from model.search_result import SearchResultModel

from class163 import OriginFile, Music
from class163.common import artist_join

from netease_encode_api import EncodeSession

from global_args.global_bin import DEFAULT_COVER


class SearchResultController(QThread):
    update_init_signal = Signal(dict)
    update_signal = Signal(Music)

    def __init__(self, model: SearchResultModel):
        super(SearchResultController, self).__init__()
        self.model = model
        self.encode_session = EncodeSession()
        # 绑定信号和槽

    def run(self):
        self.search()

    def search(self):
        self.model.get_info()
        self.update_init_signal.emit(self.model.result_dict)
        cnt = 0
        for i in self.model.result_list:
            result_dict = {}
            i.get_detail(self.encode_session)
            cover_existed = False
            if i.cover_file_url != None:
                cover_existed = True
                i.cover_file_url = i.cover_file_url + "?param=48y48"
                i.cover_file = OriginFile(i.cover_file_url)
                try:
                    i.cover_file.begin_download()
                except:
                    pass
            cnt += 1
            result_dict.update(
                {
                    "data": i.cover_file.get_data() if cover_existed else DEFAULT_COVER,
                    "title": i.title,
                    "artist": artist_join(i.artist, "/"),
                    "index": cnt,
                    "row": len(self.model.result_list),
                    "from": self.model.result_dict["title"],
                }
            )
            self.update_signal.emit(result_dict)
