from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')  

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    with open("data.txt", "a", encoding='utf-8') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    return redirect('/thanks')

@app.route('/thanks')
def thanks():
    return "<h1>Thank you for submitting!</h1>"

if __name__ == '__main__':
    app.run(debug=True)