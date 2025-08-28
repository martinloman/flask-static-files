# Flask static files demo

A minimal Flask project that demos the use of static files. This demo contains an
image, a css file and a javascript file.

Static files are stored in the `/static` folder. That folder name is standard convention.

Note the use of the `url_for` function (in the templates) to serve static files. This enables Flask to dynamically generate the correct URLs for static assets, ensuring that they are properly linked in your HTML. It does not matter what route a template is rendered from; the `url_for` function will always point to the correct static file.

## How to run

1. Install dependencies:
```
pip install -r requirements.txt
```
   or
```
py -m pip install -r requirements.txt
```
2. Start the server:
```
python app.py
```
   or
```
py app.py
```
3. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.
