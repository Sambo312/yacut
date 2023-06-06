from datetime import datetime
import random
import string

from flask import url_for

from yacut import db
from settings import MAX_RANDOM_URL_LENGTH, MAX_SHORT_URL_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_URL_LENGTH), unique=True, nullable=False
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def as_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short_id=self.short,
                _external=True
            )
        )

    def check_short_url(self, short_url):
        if self.query.filter_by(short=short_url).first() is None:
            return True
        return False

    def get_uniq_short(self):
        random_short_link = str(''.join(
            random.choices(
                string.ascii_letters + string.digits, k=MAX_RANDOM_URL_LENGTH)))
        if self.check_short_url(self, random_short_link):
            return random_short_link
        return None

    def get_original_url(self, short_url):
        return self.query.filter_by(short=short_url).first().original
