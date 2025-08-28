from flask import Flask, render_template

app = Flask(__name__)

"""
Alla statiska filer lagras i katalogen 'static'. 
Detta är den standardplats där Flask-applikationer serverar statiska resurser. 
Statiskt innehåll kan inkludera bilder, ljud, video, stilmallar och JavaScript-filer.
"""

@app.route('/')
def index():
    return render_template('index.html', heading="Welcome to the Flask Static Files Demo")

"""
Trots att den här routen är jättelång så fungerar referenserna till de statiska
filerna. 
Det fungerar eftersom mallen använder {{ url_for('static', filename='images/sneakers.png') }}
istället för den absoluta sökvägen "static/images/sneakers.png".
"""
@app.route('/a/really/long/route')
def index_again():
    return render_template('index.html', heading="This page is on a long route")


if __name__ == '__main__':
    app.run(debug=True)
