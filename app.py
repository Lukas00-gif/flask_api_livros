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



app.run(port=7000, host='localhost', debug=True)