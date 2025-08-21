from flask import Flask, render_template

app = Flask(__name__)

"""
All static files are stored in the 'static' directory. 
This is the standard location for serving static assets in Flask applications.
Static content could include images, audio, video, stylesheets, and JavaScript files.
"""

@app.route('/')
def index():
    return render_template('index.html', heading="Welcome to the Flask Static Files Demo")

if __name__ == '__main__':
    app.run(debug=True)
