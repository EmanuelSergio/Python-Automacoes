#API - lugar para disponibilizar recursos e/ou funcionalidades
#1 objetivo - criar API que disponibiliza a consulta, criação, edição e exclusao
#2 URL base - localhost
#3 Endpoints - 
    #- localhost/livros (GET)
    # - localhost/livros/id (GET)
    #- localhost/livros/id (PUT)
    #- localhost/livros/id (DELETE)
#4 quais recursos - LIVROS

from flask import Flask, jsonify, request

app = Flask(__name__)#nome da aplicação com o nome do arquivo atual

livros = [
    {
        'id':1,
        'titulo': 'Direito Penal',
        'Autor': 'Carlos'
    },
    {
        'id':2,
        'titulo': 'Direito Civil',
        'Autor': 'Roberto'
    },
    {
         'id':3,
        'titulo': 'Direito da familia',
        'Autor': 'Gustavo'
    }
]

#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


#consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
        return jsonify(livro)
    
    
#Editar
@app.route('/livros/<int>id>',methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    
    
    
app.run(port=5000,host='localhost',debug=True)