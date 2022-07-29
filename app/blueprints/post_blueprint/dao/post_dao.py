import json

from app.paths import PATH_DATA_DATA, PATH_DATA_COMMENTS


class File:
    def __init__(self):
        self.path_data: str = PATH_DATA_DATA
        self.path_comments: str = PATH_DATA_COMMENTS

    def get_all_posts(self) -> list[dict]:
        with open(self.path_data, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_all_comments(self) -> list[dict]:
        with open(self.path_comments, 'r', encoding='utf-8') as f:
            return json.load(f)


class Post(File):
    def get_post_by_id(self, id: int) -> dict:
        datas: list[dict] = self.get_all_posts()
        return [post for post in datas if post['pk'] == id][0]

    def get_comments(self, id: int) -> list[dict]:
        all_comments: list[dict] = self.get_all_comments()
        return [comment for comment in all_comments if comment['post_id'] == id ]

    def search_posts_by_word(self, word: str) -> list[dict]:
        all_posts = self.get_all_posts()
        return [post for post in all_posts if word.lower() in post['content'].lower()]

    def search_posts_by_user(self, user: str) -> list[dict]:
        all_posts = self.get_all_posts()
        return [posts for posts in all_posts if posts['poster_name'] == user]
