from flask import Flask, abort, redirect, render_template, request, url_for
from hashids import Hashids
from redis import Redis

import forms


app = Flask(__name__)
app.debug = True
app.secret_key = 'hY|PSRtNPHa6Kcip4NcDZYVNQxn-csvO'

redis = Redis()


def get_unique_id():
    id_pasta = redis.incr('pasta:id')
    hashids = Hashids(salt=app.secret_key, min_length=8)
    unique_id = hashids.encode(int(id_pasta))
    return unique_id


@app.route('/', methods=['GET'])
def home():
    keys = redis.keys('pasta-*')
    elements = []
    for key in keys:
        key = key.decode('utf-8')
        prefix, unique_id = key.split('-')
        title = redis.hget(key, 'title')
        if unique_id and title:
            element = {
                'unique_id': unique_id,
                'title': title.decode('utf-8'),
            }
            elements.append(element)
    return render_template('home.html', elements=elements)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    form = forms.CreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            unique_id = get_unique_id()
            key = 'pasta-{}'.format(unique_id)
            redis.hset(key, 'title', form.data['title'])
            redis.hset(key, 'content', form.data['content'])
            return redirect(url_for('show', unique_id=unique_id))
    return render_template('create.html', form=form)


@app.route('/<unique_id>/', methods=['GET'])
def show(unique_id):
    key = 'pasta-{}'.format(unique_id)
    title = redis.hget(key, 'title')
    content = redis.hget(key, 'content')
    if title and content:
        title = title.decode('utf-8')
        content = content.decode('utf-8')
        return render_template(
            'show.html',
            unique_id=unique_id,
            title=title,
            content=content)
    else:
        abort(404)


if __name__ == '__main__':
    app.run()

