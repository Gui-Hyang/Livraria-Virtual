from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [
    {
        'Id': 1,
        'Nome': 'Diario de um Banana: Dias de Cão',
        'Paginas': 224,
        'Autor': 'Jeff Kinney'
    },


    {
        'Id': 2,
        'Nome': 'Harry Potter e a Pedra Filosofal',
        'Paginas': 208,
        'Autor': 'J.K Rowling'
    },

    {
        'Id': 3,
        'Nome': 'O Chamado de Cthulhu',
        'Paginas': 208,
        'Autor': 'H.P Lovecraft'
    },

    {
        'Id': 4,
        'Nome': 'Necromicon: Vida & Morte',
        'Paginas': 888,
        'Autor': 'H.P Lovecraft'
    }
]

@app.route('/livros', methods= ['GET'])
def consultar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])

def consultar_livros_por_id(id):
    for livro in livros:
     if livro.get('id') == id:
      return jsonify (livros)

@app.route ('/livros', methods=['POST'])
def cadastrar_livros():
    novo_livro = request.get_json()
    livros.append (novo_livro)
    return jsonify (livros)

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_por_id(id):
 livros_atualizado = request.get_json()
 for indice,livro in enumerate(livros):
    if livro.get('id') == id:
        livros[indice].update(livros_atualizado)
        return jsonify (livros[indice])

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify (livros)

app.run(port=8080,host='localhost',debug=True)