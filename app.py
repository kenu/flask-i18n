from flask import Flask, render_template, request, session
from flask_babel import Babel, get_locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['en', 'ko', 'zh'])

app.jinja_env.globals['get_locale'] = get_locale
babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_language/<language>')
def set_language(language):
    session['language'] = language
    return 'Language set to ' + language + '<br><a href="/">Back to index</a>'

if __name__ == '__main__':
    app.run(debug=True)
