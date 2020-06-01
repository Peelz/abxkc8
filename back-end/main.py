from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='/static', static_folder='static')

mock_data = [
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

@app.route('/')
def get_all():
    return mock_data

@app.route('/create', methods=['POST'])
def add_data():
    try:
        req_json = request.get_json()
    except Exception as e:
        pass
    for v in req_json['data']:
        mock_data.append({'nane': v})
    return {'data': mock_data}
