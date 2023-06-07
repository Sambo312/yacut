import re

from . import db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from settings import VALID_SYMBOLS, MAX_SHORT_URL_LENGTH


def create_short_url():
    short_url = None
    while short_url is None:
        short_url = URLMap.get_uniq_short(URLMap)
    return short_url


def save_url_map(url, short_url):
    try:
        url_map = URLMap(original=url, short=short_url)
        db.session.add(url_map)
        db.session.commit()
    except Exception as error:
        return str(error)
    return url_map


def get_short_url(short_url=None):
    warning = None
    user_url = short_url
    if short_url:
        if URLMap.check_short_url(URLMap, short_url):
            short_url = create_short_url()
            warning = f'Имя {user_url} уже занято!'
    else:
        short_url = create_short_url()
    return {'url': short_url, 'warning': warning}


def check_user_url(user_url):
    if (
        (re.match(VALID_SYMBOLS, user_url) is not None) and
        (len(user_url) <= MAX_SHORT_URL_LENGTH)
    ):
        return user_url
    raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')


def check_url(url):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    if not isinstance(url, str):
        return False
    return re.search(re.compile(regex), url)
