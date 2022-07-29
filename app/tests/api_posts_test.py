from app.blueprints.post_blueprint.dao.post_dao import File, Post


class TestAPI:
    # def test_get_all_posts(self, open_mock):
    #     assert isinstance(File().get_all_posts(), list)
    #     assert 'post_id' in File().get_all_posts()[0].keys()

    def test_get_all_post_2(self):
        assert {
                   "poster_name": "leo",
                   "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
                   "pic": "Эб",
                   "content": "Ага",
                   "views_count": 376,
                   "likes_count": 154,
                   "pk": 1
               }.keys() == File().get_all_posts()[0].keys()
        assert isinstance(File().get_all_posts(), list)

    def test_get_post_by_id(self):
        assert {
                   "poster_name": "leo",
                   "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
                   "pic": "Эб",
                   "content": "Ага",
                   "views_count": 376,
                   "likes_count": 154,
                   "pk": 1
               }.keys() == Post().get_post_by_id(1).keys()
        assert isinstance(Post().get_post_by_id(1), dict)
