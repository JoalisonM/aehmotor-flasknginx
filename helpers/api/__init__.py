from flask import Blueprint
from flask_restful import Api

from resources.logout import Logout
from resources.login import Login
from resources.pretensao import Pretensoes,PretensaoById
from resources.viagem import Viagens,ViagemById
from resources.rotaInstiruicaoEnsino import RotaInstituicoesDeEnsino, RotasInstituicoesDeEnsino
from resources.motorista import Motoristas, MotoristaById
from resources.veiculo import Veiculos, VeiculoById
from resources.motorista import Motoristas, MotoristaById, MotoristaByNome
from resources.veiculo import Veiculos, VeiculoById, VeiculoByPlaca
from resources.passageiro import Passageiros, PassageiroById
from resources.cidade import Cidades,CidadeById, CidadeByNome
from resources.endereco import Enderecos, EnderecoById, EnderecoByLogradouro
from resources.aluno import Alunos, AlunoById, AlunoByNome
from resources.pessoa import Pessoas, PessoaById, PessoaByNome, PessoaMe
from resources.uf import Ufs, UfById, UfByNome
from resources.instituicaoEnsino import InstituicoesDeEnsino, InstituicaoDeEnsinoById, InstituicaoDeEnsinoByNome
from resources.funcionario import Funcionarios, FuncionarioById, FuncionarioByNome
from resources.rota import Rotas, RotaById, RotaByCidadeDestino
from resources.prefeitura import Prefeituras, PrefeituraById, PrefeituraByNome

# Api e Blueprint
api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api")

api.add_resource(PretensaoById,'/pretensoes/<int:id>')
api.add_resource(Pretensoes, '/pretensoes')
api.add_resource(Viagens, '/viagens')
api.add_resource(ViagemById, '/viagens/<int:id>')
api.add_resource(Logout, '/logout')
api.add_resource(Login, '/login')
api.add_resource(Motoristas,'/motoristas')
api.add_resource(MotoristaById,'/motoristas/<int:id>')
api.add_resource(MotoristaByNome,'/motoristas/<nome>')
api.add_resource(Veiculos,'/veiculos')
api.add_resource(VeiculoById,'/veiculos/<int:id>')
api.add_resource(VeiculoByPlaca,'/veiculos/<placa>')
api.add_resource(Passageiros, '/passageiros')
api.add_resource(PassageiroById,'/passageiros/<int:id>')
api.add_resource(Alunos, '/alunos')
api.add_resource(AlunoById, '/alunos/<int:idPessoa>')
api.add_resource(AlunoByNome,'/alunos/<query>')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(PessoaById, '/pessoas/<int:id>')
api.add_resource(PessoaByNome,'/pessoas/<nome>')
api.add_resource(PessoaMe,'/pessoas/me')
api.add_resource(Cidades,'/cidades')
api.add_resource(CidadeById,'/cidades/<int:id>')
api.add_resource(CidadeByNome,'/cidades/<nome>')
api.add_resource(Enderecos,'/enderecos')
api.add_resource(EnderecoById,'/enderecos/<int:id>')
api.add_resource(EnderecoByLogradouro,'/enderecos/<logradouro>')
api.add_resource(Ufs, '/ufs')
api.add_resource(UfById, '/ufs/<int:id>')
api.add_resource(UfByNome,'/ufs/<nome>')
api.add_resource(InstituicoesDeEnsino, '/instituicoesDeEnsino')
api.add_resource(InstituicaoDeEnsinoById, '/instituicoesDeEnsino/<int:id>')
api.add_resource(InstituicaoDeEnsinoByNome,'/instituicoesDeEnsino/<nome>')
api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(FuncionarioById, '/funcionarios/<int:id>')
api.add_resource(FuncionarioByNome,'/funcionarios/<nome>')
api.add_resource(Rotas, '/rotas')
api.add_resource(RotaById, '/rotas/<int:id>')
api.add_resource(RotaByCidadeDestino,'/rotas/<cidade_destino>')
api.add_resource(Prefeituras, '/prefeituras')
api.add_resource(PrefeituraById, '/prefeituras/<int:id>')
api.add_resource(PrefeituraByNome,'/prefeituras/<nome>')
api.add_resource(RotaInstituicoesDeEnsino,'/rota-instituicoes')
api.add_resource(RotasInstituicoesDeEnsino,'/rota-instituicoes/<int:id>')