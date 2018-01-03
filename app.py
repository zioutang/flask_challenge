import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route('/success/<name>', methods=["POST"])
def success(name):
   return 'welcome %s' % name

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request);
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    return render_template("image.html", image_name=filename)

@app.route('/upload/<filename>', methods=["POST"])
def send_image(filename):
    print(send_from_directory("images", filename));
    print(request.form);
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
