from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def __repr__(self):
        return title


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50),unique= True,nullable= False)
    password = db.Column(db.String(250),nullable = False)
    posts = relationship("BlogPost",  backref="author")
    def __repr__(self):
        return name

with app.app_context():
    db.create_all()



parent1 = User(name = "anshu",email = "vvv@gmail.com",password = 123)
child2 = BlogPost(title = 'The life of cactus',subtitle = "Nothing to be serious",date = "12/23/2333",body = "hwoooooooooooooooooooooooooo nnnnnnnnnnnn wooooooorrrrrrrlllllldddddddd",img_url = "https://www.google.com",author_id = parent1)

db.session.add(parent1)
db.session.add(child2)
db.commit()

