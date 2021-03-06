from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ------- Get Blog Data -------- #
response = requests.get("https://api.npoint.io/7af7044942ccc095c1a7")
response.raise_for_status()
blog_posts = response.json()


# -------- Website Pages -------- #
@app.route("/")
def home_page():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html", contact_received=False)
    elif request.method == 'POST':
        contact_name = request.form['name']
        contact_email = request.form['email']
        contact_phone = request.form['phone']
        contact_message = request.form['message']
        return render_template("contact.html", contact_received=True)
    else:
        return '<h1>Invalid request to contact_page (must be GET or POST)</h1>'


@app.route("/posts/<post_id>")
def get_post(post_id):
    # Make sure post_id is a number
    if not post_id.isnumeric():
        return render_template("contact.html")
    else:
        post_id = int(post_id)

    # Find the post and render it
    for post in blog_posts:
        if post['id'] == post_id:
            return render_template("post.html", post=post)

    # Post not found:
    return render_template("contact.html")


# ------- Entry point ------- #
if __name__ == "__main__":
    app.run(debug=True)
