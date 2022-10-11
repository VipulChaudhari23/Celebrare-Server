from flask import Flask, render_template, request, jsonify

from logic.video import createVideoOnAws

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-video', methods=["POST"])
def createVideo():
    videoData = request.form
    brideName = videoData["bridename"]
    groomName = videoData["groomname"]
    weddingDate = videoData["wdate"]
    videoUrl = createVideoOnAws(brideName, groomName, weddingDate)
    # videoUrl = "/static/videos/templateVideo01.mp4"

    return jsonify({
        "videoUrl": videoUrl,
        "requestData": {
            "brideName": brideName,
            "groomName": groomName,
            "weddingDate": weddingDate,
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 
