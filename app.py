from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"<h2>Hello, {name}! Welcome to Flask UI demo.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
