from tinydb import TinyDB, Query
from pydantic import BaseModel
from datetime import datetime

class UsuarioSchema(BaseModel):
  nome: str
  posicao: int
  prioridade: bool
  dataChegada: datetime
  atendido: bool

class NovoUsuarioSchema(BaseModel):
  nome: str
  prioridade: bool

class Usuario:
  def __init__(self, nome: str, prioridade: bool):
    ultimoRegistro = self.ultimoUsuario()
    self.id = ultimoRegistro['id'] + 1
    self.nome = nome
    self.prioridade = prioridade
    self.posicao = ultimoRegistro['posicao'] + 1 if ultimoRegistro else 1
    self.dataChegada = datetime.now()
    self.atendido = False
  
  
  def novo(self):
    db = TinyDB('db.json')
    db.insert({
      'id': self.id,
      'nome': self.nome,
      'posicao': self.posicao,
      'prioridade': self.prioridade,
      'dataChegada': self.dataChegada.isoformat(),
      'atendido': self.atendido
    })
  
  @classmethod
  def recuperarFilaTodos(cls):
    db = TinyDB('db.json')
    registros = db.all()
    return registros
  
  @classmethod
  def ultimoUsuario(cls):
    db = TinyDB('db.json')
    registros = db.all()
    if registros:
      ultimo = sorted(registros, key=lambda x: x['posicao'], reverse=True)[0]
      return ultimo
    return None
  
  @classmethod
  def recuperarPorId(cls, id):
    db = TinyDB('db.json')
    query = Query()
    registros = db.search(query.id == id)
    
    if registros:
      return registros[-1]
    return None
  
  @classmethod
  def recuperarFila(cls):
    db = TinyDB('db.json')
    registros = db.all()
    
    prioritarios = [r for r in registros if r['prioridade'] and not r['atendido']]
    naoPrioritarios = [r for r in registros if not r['prioridade'] and not r['atendido']]
    
    prioritarios.sort(key=lambda x: x['dataChegada'])
    naoPrioritarios.sort(key=lambda x: x['dataChegada'])

    fila = prioritarios + naoPrioritarios
    return fila
  
  @classmethod
  def atenderProximo(cls):
    db = TinyDB('db.json')
    query = Query()
    nao_atendidos = db.search(query.atendido == False)
    
    if not nao_atendidos:
        return None

    nao_atendidos.sort(key=lambda x: datetime.strptime(x['dataChegada'], '%Y-%m-%dT%H:%M:%S.%f'))
    proximo = nao_atendidos[0]

    nova_posicao = 0 if proximo['posicao'] == 1 else proximo['posicao']
    db.update({'posicao': nova_posicao, 'atendido': True}, query.id == proximo['id'])

    for registro in nao_atendidos[1:]:
        nova_posicao = registro['posicao'] - 1
        db.update({'posicao': nova_posicao}, query.id == registro['id'])

    return proximo
    