from getResponses import get_response
from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
# py -3 pip install pip install -U flask-cors

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods = ['GET'])
@cross_origin()
def home_page():
    #access your DB get your results here
    data = { "data":"This is the home page, wellcome!" }
    return jsonify(data)


@app.route('/message', methods = ['GET'])
@cross_origin()
def getResponses():
    message_query = str(request.args.get('message')) # http://127.0.0.1:3001/message?message=how
    response = {'response': str(get_response(message_query))}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3001)