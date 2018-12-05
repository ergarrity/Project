"""Data model for counties in Oregon."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#---------------------------------------------------------------------#

class County(db.Model):
    """County in Oregon"""

    __tablename__ = "counties"

    county_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    county_name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False) #to do change from float to string
    county_name_lower = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<County county_id={}, county_name={}, latitude={}, longitude={}>".format(
            self.county_id, self.county_name, self.latitude, self.longitude)



class District(db.Model):
    """School districts in Oregon"""

    __tablename__ = "districts"

    district_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    district_name = db.Column(db.String(100), unique=True, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'))

    county = db.relationship("County", backref=db.backref("districts"))

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<District district_id={}, district_name={}>".format(
            self.district_id, self.district_name)



class Group(db.Model):
    """Groups of students by living situation"""

    __tablename__ = "groups"

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Group group_id={}, group_name={}>".format(
            self.group_id, self.group_name)



class DistrictGroup(db.Model):

    __tablename__ = "district_groups"

    district_group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    district_id = db.Column(db.Integer, db.ForeignKey('districts.district_id'))
    student_count = db.Column(db.Integer)
    year = db.Column(db.Integer)

    # Define relationship to group
    group = db.relationship("Group", backref=db.backref("districtgroups", order_by=group_id))

    # Define relationship to district
    district = db.relationship("District", backref=db.backref("districtgroups", order_by=district_id))


class Student(db.Model):
    """Individual students"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    county = db.Column(db.String(50), nullable=False)
    living_situation = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)



def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hbpj'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
