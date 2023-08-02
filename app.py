from flask import Flask, jsonify, request

app = Flask(__name__)

#fontes de dados com dicionario mesmo
livros = [
    {
        'id': 1,
        'titulo': 'A vila dos Tecidos',
        'autor': 'Anne Jacobs'
    },
    {
        'id': 2,
        'titulo': 'Fogo e Sangue',
        'autor': 'George R.R. Martin'
    },
    {
        'id': 3,
        'titulo': 'O Cavaleiro dos sete reinos',
        'autor': 'George R.R. Martin'
    },
]


#consultar todos GET
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar por id GET
# passar por todos os id e ve se e o que eu quero
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#editar id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


#criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)


app.run(port=7000, host='localhost', debug=True)