from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://caiohenrks:12345678@localhost/mysqldb'
db = SQLAlchemy(app)

# Configuração do OAuth2
oauth = OAuth(app)
auth = HTTPBasicAuth()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    av3 = db.Column(db.Float)
    av4 = db.Column(db.Float)

@auth.verify_password
def verify_password(username, password):
    user = Usuario.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user

# Configuração do Swagger UI
SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Alunos"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Usuario(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuario registrado!'})

@app.route('/cadastrar_aluno', methods=['POST'])
@auth.login_required
def cadastrar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(nome=data['nome'], av1=data['av1'], av2=data['av2'], av3=data['av3'], av4=data['av4'])
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno cadastrado!'})

@app.route('/alunos', methods=['GET'])
@auth.login_required
def get_all_alunos():
    alunos_list = Aluno.query.all()
    alunos = []
    for aluno in alunos_list:
        alunos.append({'nome': aluno.nome, 'av1': aluno.av1, 'av2': aluno.av2, 'av3': aluno.av3, 'av4': aluno.av4})
    return jsonify({'alunos': alunos})

@app.route('/aluno/<id>', methods=['GET'])
@auth.login_required
def get_one_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado!'})
    return jsonify({'nome': aluno.nome, 'av1': aluno.av1, 'av2': aluno.av2, 'av3': aluno.av3, 'av4': aluno.av4})

@app.route('/aluno/<id>', methods=['PUT'])
@auth.login_required
def update_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado!'})
    data = request.get_json()
    aluno.nome = data['nome']
    aluno.av1 = data['av1']
    aluno.av2 = data['av2']
    aluno.av3 = data['av3']
    aluno.av4 = data['av4']
    db.session.commit()
    return jsonify({'message': 'Aluno atualizado!'})

@app.route('/aluno/<id>', methods=['DELETE'])
@auth.login_required
def delete_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado!'})
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno deletado!'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

