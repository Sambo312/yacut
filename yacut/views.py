from flask import flash, redirect, render_template

from . import app
from .forms import URLForm
from .models import URLMap
from .utils import get_short_url, save_url_map


@app.route('/', methods=('GET', 'POST',))
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        user_url = get_short_url(form.custom_id.data)
        if user_url.get('warning'):
            flash(user_url.get('warning'), 'warning')
        url_map = save_url_map(
            form.original_link.data,
            user_url.get('url')
        )
        if isinstance(url_map, str):
            flash(url_map, 'warning')
            return render_template('index.html', form=form)
        flash(url_map.as_dict().get('short_link'), 'successfully')
        return render_template('index.html', form=form)
    if len(form.errors) > 0:
        flash(form.errors, 'warning')
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def redirect_view(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )
