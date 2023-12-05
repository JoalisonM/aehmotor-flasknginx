from flask_restful import Resource,reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.veiculo import*
from model.viagem import *
from model.message import*
from model.rota import *
from model.motorista import *
from helpers.base_logger import logger

parser = reqparse.RequestParser()
parser.add_argument('cidade', type=str, help='Problema no campo de cidade',required=True)
parser.add_argument('qtd_passageiros', type=int, help='Problema na quantidade de passageiros',required=True)
parser.add_argument('tipo_veiculo', type=str, help='Problema no tipo de veículo',required=True)
parser.add_argument('placa', type=str, help='Problema na placa do veículo',required=True)


class Veiculos(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Veículos listados com sucesso!")
        veiculos = Veiculo.query.all()
        return marshal(veiculos, veiculo_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = parser.parse_args()
        try:
           cidade = args["cidade"]
           qtd_passageiros = args["qtd_passageiros"]
           tipo_veiculo = args["tipo_veiculo"]
           placa = args["placa"]

           veiculo = Veiculo(cidade, qtd_passageiros, tipo_veiculo, placa)

           db.session.add(veiculo)
           db.session.commit()

           logger.info("Veículo cadastrado com sucesso!")

           return marshal(veiculo, veiculo_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao cadastrar veículo", 2)
            return marshal(message, message_fields), 404

class VeiculoById(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        veiculo = Veiculo.query.get(id)

        if veiculo is None:
            logger.error(f"Veiculo {id} não encontrado")

            message = Message(f"Veiculo {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Veiculo {id} encontrado com sucesso!")
        return marshal(veiculo, veiculo_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = parser.parse_args()

        try:
            veiculo = Veiculo.query.get(id)

            if veiculo is None:
                logger.error(f"Veículo {id} não encontrado")
                message = Message(f"Veículo {id} não encontrado", 1)
                return marshal(message, message_fields)

            veiculo.cidade = args["cidade"]
            veiculo.qtd_passageiros = args["qtd_passageiros"]
            veiculo.tipo_veiculo = args["tipo_veiculo"]
            veiculo.placa = args["placa"]

            db.session.add(veiculo)
            db.session.commit()

            logger.info("Veículo cadastrado com sucesso!")
            return marshal(veiculo, veiculo_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Erro ao atualizar veículo", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token, token_tipo, id):
        veiculo = Veiculo.query.get(id)

        if veiculo is None:
            logger.error(f"Veículo {id} não encontrado")
            message = Message(f"Veículo {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(veiculo)
        db.session.commit()

        message = Message("Veículo deletado com sucesso!", 3)
        return marshal(message, message_fields), 200

class VeiculoByPlaca(Resource):
    @token_verifica
    def get(self, refresh_token, token_tipo, placa):
        veiculo = Veiculo.query.filter(
            Veiculo.placa.ilike(f"%{placa}%")
        ).all()

        if veiculo is None:
            logger.error(f"Veículo {id} não encontrado")

            message = Message(f"Veículo {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Veículo {id} encontrado com sucesso!")
        return marshal(veiculo, veiculo_fields), 200