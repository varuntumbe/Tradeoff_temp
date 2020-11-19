from app import app, db


class db_table(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(25))
    descr = db.Column(db.String(100))
    end = db.Column(db.String(50))

    def __repr__(self):
        return "<object of id {}>".format(self.id)
