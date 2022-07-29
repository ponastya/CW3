from typing import Optional

from flask import Blueprint, jsonify, render_template, request

from app.blueprints.post_blueprint.dao.post_dao import File, Post
from app.logger import logger

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')



@post_blueprint.route('/', methods=['GET'])
def main_page():
    posts = File().get_all_posts()
    return render_template('index.html', posts=posts)


@post_blueprint.route('/post/<int:post_id>', methods=['GET'])
def post_page(post_id: int):
    post_by_id: Optional[dict] = Post().get_post_by_id(post_id)
    comments_by_id: list[dict] = Post().get_comments(post_id)
    return  render_template('post.html', post_by_id=post_by_id, comments_by_id=comments_by_id)


@post_blueprint.route('/search/', methods=['GET'])
def search_page():
    search_word: str = request.args.get('search_word')
    print(search_word)
    posts_by_word = Post().search_posts_by_word(search_word)
    return render_template('search.html', posts_by_word=posts_by_word)


@post_blueprint.route('/users/<username>')
def user_page(username: str):
    posts = Post().search_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)

# API
@post_blueprint.route('/api/post')
def api_all_post():
    posts = File().get_all_posts()
    logger.info('Request /api/post')
    return jsonify(posts)


@post_blueprint.route('/api/post/<int:post_id>')
def api_post(post_id: int):
    post_by_id: Optional[dict] = Post().get_post_by_id(post_id)
    logger.info(f'Request /api/post/{post_id}')
    return jsonify(post_by_id)

