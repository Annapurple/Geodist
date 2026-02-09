import secrets
from flask import Flask, render_template, redirect, abort, request, url_for, send_file, jsonify
from flask_login import login_user, LoginManager, logout_user, login_required, current_user

app = Flask(__name__)


@app.route('/')
def page():
    return render_template("main_page.html")


@app.route('/text1')
def text1():
    return render_template("text1.html", test="test1")


@app.route('/text2')
def text2():
    return render_template("text2.html", test="test2")


@app.route('/text3')
def text3():
    return render_template("text3.html", test="test3")


@app.route('/text4')
def text4():
    return render_template("text4.html", test="test4")


@app.route('/test1', methods=['GET', 'POST'])
def test1():
    return render_template('test1.html')


@app.route('/test2', methods=['GET', 'POST'])
def test2():
    return render_template('test2.html')


@app.route('/test3', methods=['GET', 'POST'])
def test3():
    return render_template('test3.html')


@app.route('/test4', methods=['GET', 'POST'])
def test4():
    return render_template('test4.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
