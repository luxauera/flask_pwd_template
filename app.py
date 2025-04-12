from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'todo_secret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'todos' not in session:
        session['todos'] = []

    if request.method == 'POST':
        new_todo = request.form.get('todo')
        if new_todo:
            session['todos'].append(new_todo)
            session.modified = True
        return redirect(url_for('index'))

    return render_template('index.html', todos=session['todos'])


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 'todos' in session and 0 <= todo_id < len(session['todos']):
        session['todos'].pop(todo_id)
        session.modified = True
    return redirect(url_for('index'))


@app.route('/manifest.json')
def manifest():
    return redirect(url_for('static', filename='manifest.json'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
