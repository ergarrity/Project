from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    return render_template("homepage.html")


@app.route('/baker')
def baker_stats():
  """Show statistics for Baker County"""

  return render_template("baker.html")


@app.route('/benton')
def benton_stats():
  """Show statistics for Benton County"""

  return render_template("benton.html")


@app.route('/clackamas')
def clackamas_stats():
  """Show statistics for Clackamas County"""

  return render_template("clackamas.html")


@app.route('/clatsop')
def clatsop_stats():
  """Show statistics for Clatsop County"""

  return render_template("clatsop.html")


@app.route('/columbia')
def columbia_stats():
  """Show statistics for Columbia County"""

  return render_template("columbia.html")


@app.route('/coos')
def coos_stats():
  """Show statistics for Coos County"""

  return render_template("coos.html")


@app.route('/crook')
def crook_stats():
  """Show statistics for Crook County"""

  return render_template("crook.html")


@app.route('/curry')
def curry_stats():
  """Show statistics for Curry County"""

  return render_template("curry.html")


@app.route('/deschutes')
def deschutes_stats():
  """Show statistics for Deschutes County"""

  return render_template("deschutes.html")


@app.route('/douglas')
def douglas_stats():
  """Show statistics for Douglas County"""

  return render_template("douglas.html")


@app.route('/gilliam')
def gilliam_stats():
  """Show statistics for Gilliam County"""

  return render_template("gilliam.html")


@app.route('/grant')
def grant_stats():
  """Show statistics for Grant County"""

  return render_template("grant.html")


@app.route('/harney')
def harney_stats():
  """Show statistics for Harney County"""

  return render_template("harney.html")


@app.route('/hoodriver')
def hood_river_stats():
  """Show statistics for Hood River County"""

  return render_template("hoodriver.html")


@app.route('/jackson')
def jackson_stats():
  """Show statistics for Jackson County"""

  return render_template("jackson.html")


@app.route('/jefferson')
def jefferson_stats():
  """Show statistics for Jefferson County"""

  return render_template("jefferson.html")


@app.route('/josephine')
def josephine_stats():
  """Show statistics for Josephine County"""

  return render_template("josephine.html")


@app.route('/klamath')
def klamath_stats():
  """Show statistics for Klamath County"""

  return render_template("klamath.html")


@app.route('/lake')
def lake_stats():
  """Show statistics for Lake County"""

  return render_template("lake.html")


@app.route('/lane')
def lane_stats():
  """Show statistics for Lane County"""

  return render_template("lane.html")


@app.route('/lincoln')
def lincoln_stats():
  """Show statistics for Lincoln County"""

  return render_template("lincoln.html")


@app.route('/linn')
def linn_stats():
  """Show statistics for Linn County"""

  return render_template("linn.html")


@app.route('/malheur')
def malheur_stats():
  """Show statistics for Malheur County"""

  return render_template("malheur.html")


@app.route('/marion')
def marion_stats():
  """Show statistics for Marion County"""

  return render_template("marion.html")


@app.route('/morrow')
def morrow_stats():
  """Show statistics for Morrow County"""

  return render_template("morrow.html")


@app.route('/multnomah')
def multnomah_stats():
  """Show statistics for Multnomah County"""

  return render_template("multnomah.html")


@app.route('/polk')
def polk_stats():
  """Show statistics for Polk County"""

  return render_template("polk.html")


@app.route('/sherman')
def sherman_stats():
  """Show statistics for Sherman County"""

  return render_template("sherman.html")


@app.route('/tillamook')
def tillamook_stats():
  """Show statistics for Tillamook County"""

  return render_template("tillamook.html")


@app.route('/umatilla')
def umatilla_stats():
  """Show statistics for Umatilla County"""

  return render_template("umatilla.html")


@app.route('/union')
def union_stats():
  """Show statistics for Union County"""

  return render_template("union.html")


@app.route('/wallowa')
def wallowa_stats():
  """Show statistics for Wallowa County"""

  return render_template("wallowa.html")


@app.route('/wasco')
def wasco_stats():
  """Show statistics for Wasco County"""

  return render_template("wasco.html")


@app.route('/washington')
def washington_stats():
  """Show statistics for Washington County"""

  return render_template("washington.html")


@app.route('/wheeler')
def wheeler_stats():
  """Show statistics for Wheeler County"""

  return render_template("wheeler.html")


@app.route('/yamhill')
def yamhill_stats():
  """Show statistics for Yamhill County"""

  return render_template("yamhill.html")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5012)