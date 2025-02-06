from cObjetoListavel import Objeto_Listavel
from enum import Enum
from cCliente import Cliente

class StatusPedido(Enum):
    PENDENTE = 1
    ENTREGUE = 2
    CANCELADO = 3

class Pedido(Objeto_Listavel):
    def __init__(self, sCod: str, cCliente: Cliente, lListaProdutos: list, eStatus: StatusPedido) -> None:
        self.__sCod = sCod
        self.__cCliente = cCliente
        self.__lListaProdutos = lListaProdutos
        self.__eStatus = eStatus
    
    def __str__(self) -> str:
        return self.__sCod

    @property
    def cod(self) -> str:
        return self.__sCod
    
    @cod.setter
    def set_cod(self, sNovoCod: str) -> None:
        self.__sCod = sNovoCod

    @property
    def cliente(self) -> Cliente:
        return self.__cCliente
    
    @cliente.setter
    def set_client(self, cNovoCliente: Cliente) -> None:
        self.__cCliente = cNovoCliente

    @property
    def lista_produtos(self) -> list:
        return self.__lListaProdutos

    @lista_produtos.setter
    def set_lista_produtos(self, lNovaListaProdutos: list) -> None:
        self.__lListaProdutos = lNovaListaProdutos
    
    @property
    def status(self) -> StatusPedido:
        return self.__eStatus
    
    @status.setter
    def set_status(self, eNovoStatus: StatusPedido) -> None:
        self.__eStatus = eNovoStatus
    
    @property
    def info(self) -> list:
        return [str(self.__cCliente), str(self.__lListaProdutos), str(self.__eStatus)]

