from flask import Blueprint, render_template

chat_bp = Blueprint(
    'chat_route',
    __name__,
    url_prefix='/chat')

@chat_bp.get('')
def get_chat_page():
    return render_template('index.html')