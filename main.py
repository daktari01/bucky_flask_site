from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
@app.route('/<user>')
def idex(user=None):
    return render_template("user.html", user=user)




if __name__ == '__main__':
    app.run(debug=True)