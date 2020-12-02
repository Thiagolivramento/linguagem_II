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
    name = request.args.get('nome')
    identificador = request.args.get('identificador')
    email = request.args.get('email')
    try:
        return aluno.create(name, identificador, email)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/alunos/update", methods=['PUT'])
def updateAluno():
    identificador = request.args.get('identificador')
    email = request.args.get('email')
    try:
        return aluno.update(identificador, email)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/alunos/delete", methods=['DELETE'])
def deleteAluno():
    identificador = request.args.get('identificador')
    try:
        return aluno.delete(identificador)
    except Exception as e:
        return (str(e))
    return

if __name__ == '__main__':
    app.run(debug=True)
