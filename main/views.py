from flask import Blueprint, render_template, request
from config import POST_PATH
import logging

from main.utils import PostsHandler

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s', '')
    posts_handler = PostsHandler(POST_PATH)
    posts = posts_handler.search_posts(substr)

    return render_template('post_list.html', posts=posts, substr=substr)
