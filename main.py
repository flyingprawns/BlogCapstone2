from flask import Flask, render_template

app = Flask(__name__)


# -------- Website Pages -------- #
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/About")
def about_page():
    return render_template("about.html")


@app.route("/Contact")
def contact_page():
    return render_template("contact.html")


# ------- Entry point ------- #
if __name__ == "__main__":
    app.run(debug=True)
