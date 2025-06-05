from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

click_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('success'))
        else:
            error = 'Nieprawidłowy login lub hasło'
    return render_template('login.html', error=error)

@app.route('/success')
def success():
    return "Zalogowano pomyślnie!"

@app.route('/counter', methods=['GET', 'POST'])
def counter():
    global click_count
    if request.method == 'POST':
        click_count += 1
    return render_template('counter.html', count=click_count)

if __name__ == '__main__':
    app.run(debug=True)
