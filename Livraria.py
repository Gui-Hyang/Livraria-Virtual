from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [
    {
        "id": 1,
        "livro": "Dragon Ball Super - Vol 1",
        "autor": "Akira Toriyama",
        "paginas": 234
    },
  
    {
        "id": 2,
        "livro": "Jujutsu Kaisen - Vol 245",
        "autor": "Gege Akutami",
        "paginas": 230

    },
    
    {
        "id": 3,
        "livro": "Devil May Cry - Vol 5",
        "autor": "Kamiya",
        "paginas": 256
    },
    
    {
        "id": 4,
        "livro": "Naruto Shippuden - Vol 104",
        "autor": "Masashi Kishimoto",
        "paginas": 252

    }

]

@app.route('/livros', methods= ['GET'])
def consultar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods= ['GET'])
def consultar_livro_por_id(id):
    for livro in livros:
        if livro.get ('id') == id:
            return jsonify (livro)

@app.route('/livros', methods= ['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify (livros)

@app.route('/livros/<int:id>', methods= ['PUT'])
def atualizar_livro_por_id(id):
    livro_atualizado = request.get_json()
    for indice, livro in enumerate (livros):
        if livro.get('id') == id:
            livros[indice].update(livro_atualizado)
            return jsonify (livros[indice])

@app.route('/livros/<int:id>', methods= ['DELETE'])
def excluir_livro_por_id(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify (livros)

app.run(port=8080,host='localhost',debug=True)