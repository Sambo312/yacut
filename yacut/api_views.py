from http import HTTPStatus

from flask import jsonify, request

from . import app

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import check_user_url, check_url, get_short_url, save_url_map


@app.route('/api/id/', methods=('POST',))
def add_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if not data.get('url'):
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if data.get('custom_id'):
        check_user_url(data.get('custom_id'))
    if check_url(data.get('url')):
        user_url = get_short_url(data.get('custom_id'))
        if user_url.get('warning'):
            raise InvalidAPIUsage(f'Имя "{data.get("custom_id")}" уже занято.')
        url_map = save_url_map(data.get('url'), user_url.get('url'))
        if isinstance(url_map, URLMap):
            return jsonify(url_map.as_dict()), HTTPStatus.CREATED
        raise InvalidAPIUsage(url_map, HTTPStatus.INTERNAL_SERVER_ERROR)
    raise InvalidAPIUsage('Введён некорректный "url"!')


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_original_url(short_id):
    if URLMap.check_short_url(URLMap, short_id):
        return (
            jsonify({'url': URLMap.get_original_url(URLMap, short_id)}),
            HTTPStatus.OK
        )
    raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
