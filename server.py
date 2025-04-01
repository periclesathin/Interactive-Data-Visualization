from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__)

# Constants
DATA_DIRECTORY = 'json_files'

@app.route('/get_data', methods=['GET'])
def get_data():
    """Fetch all data from JSON files."""
    data = []

    for filename in os.listdir(DATA_DIRECTORY):
        if filename.endswith('.json'):
            file_path = os.path.join(DATA_DIRECTORY, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                data.extend({'date': entry['date'], 'price': entry['price']} for entry in json_data)

    return jsonify(data)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/list_json_files')
def list_json_files():
    files = [f for f in os.listdir(DATA_DIRECTORY) if os.path.isfile(os.path.join(DATA_DIRECTORY, f))]
    return jsonify(files)

@app.route('/generate_plot', methods=['POST'])
def generate_plot():
    """Generate plot data based on selected cases and number of days."""
    data = request.get_json()
    market_hash_names = data.get('market_hash_names', [])
    num_days = int(data.get('num_days', 0))

    prices = []
    for name in market_hash_names:
        file_path = os.path.join(DATA_DIRECTORY, name)
        try:
            with open(file_path, 'r') as file:
                price_data = json.load(file)
                prices.append({
                    'name': name.rsplit('.', 1)[0],
                    'data': [{'x': idx, 'y': item[1], 't': item[0]} for idx, item in enumerate(price_data[:num_days])]
                })
        except (FileNotFoundError, json.JSONDecodeError) as e:
            app.logger.error(f"Error processing file {file_path}: {e}")

    return jsonify({'prices': prices})

if __name__ == '__main__':
    app.run(debug=True)
