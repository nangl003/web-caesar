from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
        <label for="rot">
        Rotate by: <input type="text" name="rot" value="0">
        </label>
        <br>
        <br>

        <textarea name="text">{0}</textarea>

        <br>

        <input type="submit" value="Submit Query">
        </form>

    </body>
</html>"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation_num = int(request.form['rot'])
    text_area = str(request.form['text'])
    
    encrypted_message = rotate_string(text_area, rotation_num)

    return form.format(encrypted_message)

@app.route("/")
def index():

    return form.format("")

app.run()