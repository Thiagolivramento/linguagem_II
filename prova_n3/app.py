from flask import Flask, jsonify, request
from service import Aluno

app = Flask(__name__)

aluno = Aluno()

@app.route("/")
def contexto_app():
    return "Bem vindo ao CRUD mais SIMPLES POSSIVEL de alunos - NÃO VALIDA NADA!!!"

@app.route("/alunos", methods=['GET'])
def getAlunos():
    alunos = aluno.getAll()
    return jsonify(alunos)


@app.route(f"/alunos/save", methods=['POST'])
def createAluno():
    nome = request.args.get('nome')
    codigo = request.args.get('codigo')
    try:
        return aluno.create(nome, codigo)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno/update", methods=['PUT'])
def updateAluno():
    codigo = request.args.get('codigo')
    try:
        return aluno.update(codigo)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno/delete", methods=['DELETE'])
def deleteAluno():
    codigo = request.args.get('codigo')
    try:
        return aluno.delete(codigo)
    except Exception as e:
        return (str(e))
    return

if __name__ == '__main__':
    app.run(debug=True)
