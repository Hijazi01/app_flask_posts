from flask import request, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlit"
db = SQLAlchemy(app)

@app.route('/',endpoint='all_posts')
def home():
    posts=Posts.query.all()
    # return f"<h1>home page</h1>"
    return render_template("tamplate_post/home.html",posts=posts)

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

# posts=[
#     {"id":1,"title":"post1","body":"the bode of the post 1"},
#     {"id":2,"title":"post2","body":"the bode of the post 2"},
#     {"id":3,"title":"post3","body":"the bode of the post 3"},
#     {"id":4,"title":"post4","body":"the bode of the post 4"},
# ]


@app.route("/post/<int:id>" ,endpoint="post.show")
def show_post(id):
    post=Posts.query.get_or_404(id)
    return render_template("tamplate_post/show.html",post=post)


    # post=filter(lambda std:std['id']==id,Posts)
    # post=list(post)
    # if post:
    #     print(post[0])
    #     return post[0]
    # return f"<h1>not found id of post is a number of : {id}</h1>",404


@app.route("/post/delete/<int:id>" ,endpoint="post.delete")
def show_post(id):
    post=Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('all_posts'))



    #
    # @app.route("/post/update/<int:id>", endpoint="post.update")
    # def update_post(id):
    #     post = Posts.query.get_or_404(id)
    #     return render_template("tamplate_post/create.html", post=post)



@app.route("/post/create", methods = ["GET", "POST"],endpoint="post.create")
def create_post():
    if request.method == "POST":
        post_title=request.form["title"]
        post_body=request.form["body"]
        post=Posts(title=post_title, body=post_body)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('all_posts'))
    return render_template("tamplate_post/create.html")




@app.errorhandler(404)
def page_not_found(error):
    return f"<h1>sorry the reguest page not found on the server:</br>{error}</h1>"







if __name__=='__main__':
    print(f"this is my module {__name__}")
    app.run(debug=True)