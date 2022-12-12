from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/<myname>")
def hello(myname):
    params = {"name": myname.lower()}
    gender = requests.get(f"https://api.genderize.io?name={myname}", params=params)
    age = requests.get(f"https://api.agify.io?name={myname}", params=params)
    return render_template("index.html", myname=myname, gender=gender, age=age)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/ce6a08b5f7729a0d4b85"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", all_posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
