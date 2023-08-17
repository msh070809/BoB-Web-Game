from app import db

class User(db.Model):
    __tablename__ = "USER"
    username = db.Column("userid",db.String(80), unique=True, nullable=False,primary_key=True)
    userpw = db.Column("userpw",db.String(120), nullable=False)