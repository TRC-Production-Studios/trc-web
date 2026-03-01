from flask import Flask, render_template, abort
from blog_posts import BLOG_POSTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=BLOG_POSTS[:3])

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=BLOG_POSTS)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = next((p for p in BLOG_POSTS if p['slug'] == slug), None)
    if not post:
        abort(404)
    return render_template('blog_post.html', post=post)

@app.route('/imprint')
def imprint():
    return render_template('imprint.html')

# Redirect old /impressum to /imprint just in case
@app.route('/impressum')
def impressum_redirect():
    from flask import redirect
    return redirect('/imprint', code=301)

if __name__ == '__main__':
    app.run(debug=True)
