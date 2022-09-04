from flask import Flask, render_template, request, flash

application = Flask(__name__)
application.secret_key = "Abc"


@application.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@application.route("/greet", methods=["POST", "GET"])
def greeter():
    flash("Hi " + str(request.form["name_input"]) + ", great to see you!")
    return render_template("page2.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0', use_reloader=True, debug=True)
