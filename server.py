from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    return render_template("homepage.html")


@app.route('/counties/<county>')
def county_stats(county):
  """Show statistics for Baker County"""
  # Use your database to retrieve the county data
  county = County.query.get(county)
  # ...or
  county = County.query.filter(name=county).first()
  return render_template("counties/detail.html", county=county)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5012)
