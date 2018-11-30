

from model import County, District, Group, DistrictGroup, connect_to_db, db
from server import app

#---------------------------------------------------------------------#

def get_counties():
    """Load counties from dataset into database."""

    for i, row in enumerate(open('data/counties_data.csv')):
        data = row.rstrip().split(",")
        county_name, latitude, longitude = data

        county = County(county_name=county_name, latitude=latitude, longitude=longitude)

        db.session.add(county)

        if i % 100 == 0:
            print(i)

    db.session.commit()


def get_districts():
    """Load districts from dataset into database."""

    for i, row in enumerate(open('data/student_counts.csv')):
        data = row.rstrip().split(",")
        district_name = data[0]

def get_groups():
    """Load groups from list into database."""

    groups = ["sheltered", "unsheltered", "sharing", "motel"]

    for item in groups:
        group = Group(group_name=item)

        db.session.add(group)

    db.session.commit()


def get_districtgroups():
    """Load districtgroup data from dataset into database"""

    for i, row in enumerate(open('data/student_counts.csv')):
        data = row.rstrip().split(",")
        



#---------------------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_counties()

    get_groups()
