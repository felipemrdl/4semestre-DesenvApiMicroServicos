from domain.Response import ResponseObject

def createResponse(sucesso: bool, mensagem: str, dados: any):
  return {
    "sucesso": sucesso,
    "mensagem": mensagem,
    "dados": dados
  }