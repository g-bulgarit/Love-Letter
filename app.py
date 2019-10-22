from flask import Flask

UPLOAD_FOLDER = '/home/pi/LoveLetter/Images/'

app = Flask(__name__)
app.secret_key = "key_for_this_app"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 24 * 1024 * 1024