import json

from flask import Flask, jsonify

app = Flask(__name__)

try:
    with open('data_client.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print('Arquivo não existe.')

# Buscar todos os clientes
@app.route('/usuarios', methods=['GET'])
def search_clients():
    return jsonify(data)

# Buscar apenas um cliente

def search_name(user_name):
    user = next((client for client in data if client['name'].lower() == user_name.lower()), None)
    if user:
        return jsonify(user)
    return jsonify({'mensagem': f'Usuario {user_name} não encontrado'})

# Atualizar o nome de um cliente



# Adicionar um cliente ao banco de dados



# Excluir um cliente da lista


if __name__ == '__main__':
    app.run(debug=True)





