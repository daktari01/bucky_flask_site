from flask import Flask, request, render_template

app = Flask(__name__)


# @ signifies a decorator - way to wrap a funtion and modifying its behaviour

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)




if __name__ == '__main__':
    app.run(debug=True)