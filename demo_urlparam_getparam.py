from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    arr = [-1, 2, 3, 4, 5]
    return render_template("index.html", arr=arr)


@app.route("/hello/<name>/<int:year>")
def hello(name, year):
    msg = ""
    if request.args.get("location") and request.args.get("email"):
        msg = "%s - %s" % (request.args["location"], request.args["email"])

    return "HELLO %s; year: %d; msg: %s" % (name, year, msg)


@app.route("/login", methods=["get","post"])
def login():
    if request.method == "POST":
        username = request.form["un"]
        password = request.form["pass"]
        if username == "admin" and password == "123":
            return render_template("login.html", username=username, password=password)
        else:
            return "Fail"
    return render_template("login.html")


@app.template_filter("even")
def select_even(arr):
    return [a for a in arr if a > 0 and a % 2 == 0]


if __name__ == "__main__":
    app.run()
