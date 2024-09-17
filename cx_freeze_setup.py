import sys
from cx_Freeze import setup, Executable

# 要打包的Python脚本路径
script = "__init__.py"

# 创建可执行文件的配置
exe = Executable(
    script=script,
    base=(
        "Win32GUI" if sys.platform == "win32" else None
    ),  # 根据平台决定是否需要隐藏控制台
    target_name="NeteaseDownloader",  # 生成的可执行文件名称
)

# 打包的参数配置
options = {
    "build_exe": {
        "build_exe": "NeteaseDownloader",
        "packages": [
            "PySide6.QtWidgets",
            "PySide6.QtCore",
            "PySide6.QtGui",
            "qfluentwidgets",
            "class163",
            "netease_encode_api",
        ],  # 需要打包的额外Python包列表
        "excludes": [],  # 不需要打包的Python包列表
        # "include_files": ["data/config.json", "downloads/"],  # 需要包含的文件或文件夹
        "include_msvcr": True,  # 是否包含Microsoft Visual C++运行时库
        # "optimize": 2,  # 启用Python优化（可选）
    }
}

# 打包配置
setup(
    name="NeteaseDownloader",
    version="0.0.1",
    description="A music & playlist downloader for Netease Cloud Music",
    options=options,
    executables=[exe],
)
