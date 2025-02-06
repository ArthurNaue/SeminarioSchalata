from cObjetoListavel import Objeto_Listavel

class Produto(Objeto_Listavel):
    def __init__(self, sNome: str, sDescricao: str, fPreco: float, iQuantidade: int) -> None:
        self.__sNome = sNome
        self.__sDescricao = sDescricao
        self.__fPreco = fPreco
        self.__iQuantidade = iQuantidade
    
    def __str__(self) -> str:
        return self.__sNome
    
    @property
    def nome(self) -> str:
        return self.__sNome

    @nome.setter
    def set_nome(self, sNovoNome: str) -> None:
        self.__sNome = sNovoNome
    
    @property
    def descricao(self) -> str:
        return self.__sNome

    @descricao.setter
    def set_descricao(self, sNovaDescricao: str) -> None:
        self.__sDescricao = sNovaDescricao

    @property
    def preco(self) -> float:
        return self.__fPreco

    @preco.setter
    def set_preco(self, fNovoPreco: float) -> None:
        self.__fPreco = fNovoPreco
    
    @property
    def quantidade(self) -> int:
        return self.__iQuantidade

    @quantidade.setter
    def set_quantidade(self, iNovaQuantidade) -> None:
        self.__iQuantidade = iNovaQuantidade

    @property
    def info(self) -> list:
        return [self.__sNome, self.__sDescricao, str(self.__fPreco), str(self.__iQuantidade)]