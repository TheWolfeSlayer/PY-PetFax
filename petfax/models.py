from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ = 'facts'

    # makes column ID that is an integer and is primary key
    id = db.Column(db.Integer, primary_key=True)
    # makes column submitter as a string with a limit of 250 characters
    submitter = db.Column(db.String(250))
    # makes column for the fact with no size limit
    fact = db.Column(db.Text)