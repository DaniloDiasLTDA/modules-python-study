import json

from flask import Flask, jsonify, request

app = Flask(__name__)

file_name = 'clientes.json'


def load_data():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
         print('Arquivo não existe.')

data = load_data()

def save_data():
     with open('data_client.json', 'w') as file:
         json.dump(data)


# Buscar todos os clientes
@app.route('/usuarios', methods=['GET'])
def search_clients():
     if not data:
         return jsonify({'message': f'Sem clientes disponiveis'})
     return jsonify(data)


# Buscar apenas um cliente / # TODO: Adicionar Expect

def search_name(user_name):
    try:
        for client in data:
            if client['nome'].lower() == user_name.lower():
                return client
        return jsonify({'mensagem': f'Usuario {user_name} não encontrado'})
    
    except TypeError as e:
        return jsonify({'message': f'valor {e} não permitido'})
  


# Atualizar o nome de um cliente
def att_name(old_name):
    new_name = request.json.get('new_name')
    name_changed = None
    
    for usuario in data:
         if usuario['nome'].lower() == old_name.lower():
             usuario['nome'] = new_name
             name_changed = usuario
    if name_changed:
        save_data(data)
        return jsonify(name_changed)
    else:
        return jsonify({'message': f'Nenhum usuario encontrado com esse nome'})


# Adicionar um cliente ao banco de dados


# Excluir um cliente da lista



if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)


