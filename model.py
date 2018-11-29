"""Data model for counties in Oregon."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#---------------------------------------------------------------------#

# class County(db.Model):
#     """Map points for counties."""

#     __tablename__ = "counties"

#     marker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     county_name = db.Column(db.String(64), nullable=True)


#     def __repr__(self):
#         """Clear representation of county."""

#         repr_str = "<County={county_name} Marker ID={marker_id}>"
#         return repr_str.format(county_name=self.county_name, marker_id=self.marker_id)


#---------------------------------------------------------------------#

class County(db.Model):
    """County in Oregon"""

    __tablename__ = "counties"

    county_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    county_name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullabe=False)
    longitude = db.Column(db.Float, nullable=False)


class District(db.Model):
    """School districts in Oregon"""

    __tablename__ = "districts"

    district_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    district_name = db.Column(db.String(100), nullable=False)


class Group(db.Model):
    """Groups of students by living situation"""

    __tablename__ = "groups"

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///counties'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
