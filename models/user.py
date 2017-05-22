from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #init method
        self.username = username
        self.password = password

    def save_to_db(self):
        #saves user to db
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        #searches for user in db by username
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        #searches for user by id
        return cls.query.filter_by(id=_id).first()
