from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    return render_template("homepage.html")


@app.route('/baker')
def baker_stats():
  """Show statistics for Baker County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/benton')
def benton_stats():
  """Show statistics for Benton County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/clackamas')
def clackamas_stats():
  """Show statistics for Clackamas County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/clatsop')
def clatsop_stats():
  """Show statistics for Clatsop County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/columbia')
def columbia_stats():
  """Show statistics for Columbia County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/coos')
def coos_stats():
  """Show statistics for Coos County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/crook')
def crook_stats():
  """Show statistics for Crook County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/curry')
def curry_stats():
  """Show statistics for Curry County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/deschutes')
def deschutes_stats():
  """Show statistics for Deschutes County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/douglas')
def douglas_stats():
  """Show statistics for Douglas County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/gilliam')
def gilliam_stats():
  """Show statistics for Gilliam County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/grant')
def grant_stats():
  """Show statistics for Grant County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/harney')
def harney_stats():
  """Show statistics for Harney County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/hoodriver')
def hood_river_stats():
  """Show statistics for Hood River County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/jackson')
def jackson_stats():
  """Show statistics for Jackson County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/jefferson')
def jefferson_stats():
  """Show statistics for Jefferson County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/josephine')
def josephine_stats():
  """Show statistics for Josephine County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/klamath')
def klamath_stats():
  """Show statistics for Klamath County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/lake')
def lake_stats():
  """Show statistics for Lake County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/lane')
def lane_stats():
  """Show statistics for Lane County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/lincoln')
def lincoln_stats():
  """Show statistics for Lincoln County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/linn')
def linn_stats():
  """Show statistics for Linn County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/malheur')
def malheur_stats():
  """Show statistics for Malheur County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/marion')
def marion_stats():
  """Show statistics for Marion County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/morrow')
def morrow_stats():
  """Show statistics for Morrow County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/multnomah')
def multnomah_stats():
  """Show statistics for Multnomah County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/polk')
def polk_stats():
  """Show statistics for Polk County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/sherman')
def sherman_stats():
  """Show statistics for Sherman County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/tillamook')
def tillamook_stats():
  """Show statistics for Tillamook County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/umatilla')
def umatilla_stats():
  """Show statistics for Umatilla County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/union')
def union_stats():
  """Show statistics for Union County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/wallowa')
def wallowa_stats():
  """Show statistics for Wallowa County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/wasco')
def wasco_stats():
  """Show statistics for Wasco County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/washington')
def washington_stats():
  """Show statistics for Washington County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/wheeler')
def wheeler_stats():
  """Show statistics for Wheeler County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


@app.route('/yamhill')
def yamhill_stats():
  """Show statistics for Yamhill County"""

  return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5010)