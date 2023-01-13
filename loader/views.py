import logging

from flask import Blueprint, render_template, request
from loader.utils import save_uploaded_picture
from config import POST_PATH
from main.utils import PostsHandler
import locale

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def create_new_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Данные не получены'
    picture_path = save_uploaded_picture(picture)

    if not picture_path:
        return 'Файл- не изображение'

    posts_handler = PostsHandler(POST_PATH)
    new_post = {'pic': picture_path, 'content': content}
    posts_handler.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)

