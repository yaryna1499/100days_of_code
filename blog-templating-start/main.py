from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/ce6a08b5f7729a0d4b85").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for obj in post_objects:
        if obj.post_id == index:
            requested_post = obj
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
