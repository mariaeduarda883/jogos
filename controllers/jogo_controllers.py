from models.jogo_models import jogo  # Importa o modelo jogo
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

def get_jogo():
    jogo = jogo.query.all()  # Busca todos os jogo no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogo.',
            'dados': [jogo.json() for jogo in jogo]  # Converte os objetos de jogo para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

def get_jogo_by_id(jogo_id):
    jogo = jogo.query.get(jogo_id)  # Busca o jogo pelo ID
    if jogo:  # Verifica se o jogo foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'jogo encontrado.',
                'dados': jogo.json()  # Converte os dados do jogo para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

def create_jogo(jogo_data):
    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvedor e plataforma são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    novo_jogo = jogo(

        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        desenvolvedor=jogo_data['desenvolvedor'],
        plataforma=jogo_data['plataforma']
    )
    
    db.session.add(novo_jogo)  # Adiciona o novo jogo ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    response = make_response(

        json.dumps({

            'mensagem': 'jogo cadastrado com sucesso.',
            'jogo': novo_jogo.json()  # Retorna os dados do jogo cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response


def update_jogo(jogo_id,jogo_data):
    jogo = jogo.query.get(jogo_id)
    if not jogo:
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.'}, ensure_ascii=False),
            404
        )

    response.headers['Content-Type'] = 'application/json'
    return response 

    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor','plataforma']):

     response = make_response(

        json.dumps({'mensagem': 'Dados invalidos. titulo, genero, desenvolvedor e plataforma são obrigatorios.'}, ensure_ascii=False),

        400
    )  

    response.headers['Content-type'] = 'application/json'
    return response

    jogo.titulo = jogo_data['titulo']
    jogo.genero = jogo_data['genero']
    jogo.desenvolvedor = jogo_data['desenvolvedor']
    jogo.plataforma = jogo_plataforma['plataforma']

    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'jogo atualizado com sucesso',
            'jogo': jogo.json()
        },ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
   