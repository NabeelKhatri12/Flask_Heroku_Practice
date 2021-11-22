import os
from flask import Flask, render_template, request
from predictor import check


author = 'BTD'

app = Flask(__name__)

static_folder=os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = static_folder

#APP_ROOT = os.path.dirname(os.path.abspath("C:/Users/HP/Downloads/BrainTumorDetectionFlask-master"))


@app.route('/')
@app.route('/index')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        #dest = "/".join([target, filename])
        dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # dest = r'{}\{}'.format(target, filename)
        print(dest)
        file.save(dest)

    status = check(filename)

    return render_template('complete.html', image_name=dest, predvalue=status)

if __name__ == "__main__":
    #app.run(port=5000, debug= True)
    app.run(host="localhost", port=5000, debug = False)