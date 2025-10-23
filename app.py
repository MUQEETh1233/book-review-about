from flask import Flask, render_template, request

app = Flask(__name__)

reviews = []

@app.route('/')
def home():
    return render_template('home.html', reviews=reviews)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    book = request.form['book']
    review = request.form['review']
    reviews.append({'name': name, 'book': book, 'review': review})
    return render_template('home.html', reviews=reviews)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
