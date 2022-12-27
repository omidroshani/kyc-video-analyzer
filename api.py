import flask
from flask import jsonify
from flask import request
import json
import uuid
from flask import current_app as app, send_file, abort
import os
import uuid
import requests
from pathlib import Path
from utils.video_converter import VideoConverter



app = flask.Flask(__name__)
app.config["DEBUG"] = True
BASE_URL = "http://localhost:8080"

@app.route('/video', methods=['POST'])
def video():
    duration = request.form.get('duration')
    keyframes = request.form.get('keyframes')
    Path('tmp').mkdir(exist_ok=True)
    uploaded_file = flask.request.files.get('file')
    uuid_generated = str(uuid.uuid4())
    tmp_file_name = uuid_generated + '.' + uploaded_file.filename.split('.')[-1]
    tmp_file_path = 'tmp/' + tmp_file_name
    uploaded_file.save(tmp_file_path)

    ins = VideoConverter(tmp_file_path,duration=int(duration),keyframes=int(keyframes))
    sound = f"{BASE_URL}/download?path={ins.extact_sound_from_video()}"
    frames = [ f"{BASE_URL}/download?path={i}" for i in ins.extract_frames_2()]
    return jsonify({'id': uuid_generated,'sound' : sound,'frames':frames})

@app.route('/download',methods=['GET'])
def downloadFile ():
    filepath = request.args.get('path')
    return send_file(filepath, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',8080)))

