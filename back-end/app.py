from flask import Flask, request, send_from_directory, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_pyfile('config/app.cfg')

__mock_data = [
    {
        'name': 'Por',
    },
    {
        'name': 'Tong',
    },
    {
        'name': 'Tent',
    },
    {
        'name': 'Film',
    }
]

@app.route('/', methods=['GET'])
def get_all():
    return {"data": __mock_data}

@app.route('/create', methods=['POST'])
def add_data():
    try:
        req_json = request.get_json()
    except Exception as e:
        pass
    for v in req_json['data']:
        __mock_data.append({'nane': v})
    return {'data': __mock_data}

@app.route('/HealthCheck', methods=['POST', 'GET'])
def health_check():
    return Response("I'm Alive", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host='0.0.0.0')