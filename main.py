from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route("/shopping")
def shopping():
    food = [
        "Omena", 
        "Sukuma wiki", 
        "Nyama choma", 
        "Chips mwitu", 
        "Madondo chafua",
        "Muturaa sosa"
        ]
    return render_template("shopping.html", food=food)





if __name__ == '__main__':
    app.run(debug=True)