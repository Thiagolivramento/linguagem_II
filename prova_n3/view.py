from http import HTTPStatus
from app import app
from flask import jsonify, request, Response
from app.model import Pessoa
from app.service import controladorPessoa

@app.route("/")
def contexto_app():
    return "Bem vindo ao CRUD de pessoa", HTTPStatus.OK

@app.route("/pessoas", methods=['POST'])

    def save():
        lista = request.json
        if lista is None:
            return "Arquivo Json em branco", HTTPStatus.BAD_REQUEST
        try:
            persona_service = controladorPessoa()
            persona_service.salvar(lista)
            return "Informações salvas corretamente", HTTPStatus.CREATED
        except Exception as e:
            return str(e), HTTPStatus.OK

@app.route("/pessoas", methods =['DELETE'])

    def deleta(id):
      if id is None:
          return "Usuário não encontrado, digite um id válido", HTTPStatus.BAD_REQUEST

