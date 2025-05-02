import json

from flask import Flask, jsonify

app = Flask(__name__)

try:
    with open('data_client.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print('Arquivo não existe.')

@app.route('/usuarios', methods=['GET'])
def search_clients():
    return jsonify(data)






