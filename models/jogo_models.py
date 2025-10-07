# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe Jogo que representa a tabela 'jogos' no banco de dados
class Jogo(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogos'  

    # Define as colunas da tabela 'jogos'
    titulo = db.Column(db.Integer, primary_key=True)  # Coluna para o titulo do jogo, chave primária
    genero = db.Column(db.String(80), nullable=False)  # Coluna para o genero do jogo, não pode ser nulo
    desenvolvedor = db.Column(db.String(80), nullable=False)  # Coluna para a desenvolvedor do jogo, não pode ser nulo
    plataforma = db.Column(db.Integer, nullable=False)  # Coluna para a plataforma do jogo, não pode ser nulo

    # Método para retornar os dados do jogo como um dicionário
    def json(self):  
        return {
            'titulo': self.titulo,  # titulo do jogo
            'genero': self.genero,  # genero do jogo
            'desenvolvedor': self.desenvolvedor,  # desenvolvedor do jogo
            'plataforma': self.plataforma  # plataforma do jogo
        }
