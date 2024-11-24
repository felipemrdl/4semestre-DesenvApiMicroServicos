from fastapi import APIRouter
from models.usuario import NovoUsuarioSchema, Usuario, UsuarioSchema
from utils.CreateResponse import createResponse

router = APIRouter()

@router.get('/api/fila', name="Recuperar Fila", response_model=None)
async def recuperarFila():
  usuarios = Usuario.recuperarFila()
  usuariosPadronizados = [UsuarioSchema(**usuario) for usuario in usuarios]
  return createResponse(True, "Requisição processada com sucesso.", usuariosPadronizados)

@router.get('/api/fila_todos', name="Recuperar Fila", response_model=None)
async def recuperarFilaTodos():
  usuarios = Usuario.recuperarFilaTodos()
  usuariosPadronizados = [UsuarioSchema(**usuario) for usuario in usuarios]
  return createResponse(True, "Requisição processada com sucesso.", usuariosPadronizados)

@router.get('/api/fila/{id}', name="Recuperar Usuário")
async def recuperarUsuario(id: int):
  usuarios = Usuario.recuperarPorId(id)
  return createResponse(True, "Requisição processada com sucesso.", usuarios)

@router.post('/api/fila', name="Criar Usuário")
async def criarUsuario(usuario: NovoUsuarioSchema):
  novoUsuario = Usuario(usuario.nome, usuario.prioridade)
  Usuario.novo(novoUsuario)
  return createResponse(True, "Requisição processada com sucesso.", "Usuário adicionado a fila com sucesso.")

@router.put('/api/fila', name="Atualizar Fila")
async def atualizarFila():
  dados = Usuario.atenderProximo()
  return createResponse(True, "Requisição processada com sucesso.", dados)

@router.delete('/api/fila/:id', name="Remover Usuário")
async def removerUsuario(id: int):
  Usuario.removerUsuario(id)
  return createResponse(True, "Requisição processada com sucesso.", "Usuário removido da fila com sucesso.")