from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hi %s' % username


@app.route('/contact-us')
def contact_us():
    return 'contact us'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Posting %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_ = request.form['username']
        password_ = request.form['password']
        searchword = request.args.get('name', '')
        return 'login post %s %s' % (username_, searchword)
    else:
        return 'login get'


@app.errorhandler(404)
def page_not_found(error):
    return {
        'message': 'halaman tidak ditemukan bro'
           }, 404
