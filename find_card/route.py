from flask import Blueprint, request
from .controller import search_all

card=Blueprint(
    'card', __name__, static_folder='static',
    url_prefix='/card'
    )

@card.post('/get_card')
def index():
    data = request.get_json()
    return search_all(data["card_name"])