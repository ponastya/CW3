import os

PATH_MAIN = os.path.dirname(os.path.abspath(__file__))
PATH_CONFIG = os.path.join(PATH_MAIN, 'config', 'dev_config.py')
PATH_DATA =  os.path.join(PATH_MAIN, 'data')
PATH_DATA_BOOKMARKS =  os.path.join(PATH_DATA, 'bookmarks.json')
PATH_DATA_COMMENTS =  os.path.join(PATH_DATA, 'comments.json')
PATH_DATA_DATA =  os.path.join(PATH_DATA, 'data.json')
PATH_DATA_STATIC =  os.path.join(PATH_MAIN, 'blueprints', 'static')
