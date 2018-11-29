"""Load bear data into database."""

from model import County, connect_to_db, db
from server import app

#---------------------------------------------------------------------#

def get_counties():
    """Load counties from dataset into database."""

    for i, row in enumerate(open('data/counties_data.csv')):
        data = row.rstrip().split(",")
        county_name = data

        county = County(county_name=county_name)

        db.session.add(county)

        if i % 100 == 0:
            print(i)

    db.session.commit()

#---------------------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_counties()
