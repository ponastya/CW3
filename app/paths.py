from pathlib import Path

PATH_MAIN = Path(__file__).resolve().parent
PATH_CONFIG = PATH_MAIN.joinpath('config', 'dev_config.py')
PATH_DATA = PATH_MAIN.joinpath('data')
PATH_DATA_BOOKMARKS = PATH_DATA.joinpath('bookmarks.json')
PATH_DATA_COMMENTS = PATH_DATA.joinpath('comments.json')
PATH_DATA_DATA = PATH_DATA.joinpath('data.json')
PATH_DATA_STATIC = PATH_MAIN.joinpath('blueprints', 'static')
PATH_LOGGING = PATH_MAIN.parent.joinpath('logs', 'logging_data.log')
