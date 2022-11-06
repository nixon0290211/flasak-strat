from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "おっぱい"


# @app.route("/hiraizumi")
# def hello_world():
#     return "Hello,おちんちん"


# @app.route("/user/<name>")
# def heyName(name):
#     return name


@app.route("/user/<name>/<age>")
def heyName(name, age):
    return name + age


#
# @app.route("/html")
# def html():
#     html = """
#     <h1>vhsiuvhods</h1>
#     <h2>bsdfgs</h2>
#     """

#     return html


# if __name__ == "__main__":
#     app.run(
#         host="127.0.0.1",
#     )


# http://127.0.0.1:5000/user/name


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/html/<name>")
def htmlname(name):
    return render_template("index.html", name=name)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("name.html", age=age)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    return search_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
