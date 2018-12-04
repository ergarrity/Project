

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
        county = data[1]

        if District.query.filter_by(district_name=district_name).first():
            continue

        county_id = County.query.filter_by(county_name=county).first().county_id

        district = District(district_name=district_name, county_id=county_id)

        db.session.add(district)

    db.session.commit()


def get_groups():
    """Load groups from list into database."""

    groups = ["shelter", "sharing", "unsheltered", "motel"]

    for item in groups:
        group = Group(group_name=item)

        db.session.add(group)

    db.session.commit()


def get_districtgroups():
    """Load districtgroup data from dataset into database"""

    group_ids = {"shelter": 1, "sharing":2 , "unsheltered":3, "motel":4}

    for i, row in enumerate(open('data/student_counts.csv')):
        data = row.rstrip().split(",")

        (district_name, county_name, total_count, shelter_count, sharing_count, 
        unsheltered_count, motel_count, year) = data

        district_id = District.query.filter_by(district_name=district_name).first().district_id
        
        # add shelter stat
        dg1 = DistrictGroup(group_id=group_ids["shelter"], district_id=district_id, student_count=shelter_count, year=year)

        # add sharing stat
        dg2 = DistrictGroup(group_id=group_ids["sharing"], district_id=district_id, student_count=sharing_count, year=year)

        # add unsheltered stat
        dg3 = DistrictGroup(group_id=group_ids["unsheltered"], district_id=district_id, student_count=unsheltered_count, year=year)

        # add motel stat
        dg4 = DistrictGroup(group_id=group_ids["motel"], district_id=district_id, student_count=motel_count, year=year)

        db.session.add(dg1)
        db.session.add(dg2)
        db.session.add(dg3)
        db.session.add(dg4)

    db.session.commit()





#---------------------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_counties()

    get_groups()

    get_districts()

    get_districtgroups()
