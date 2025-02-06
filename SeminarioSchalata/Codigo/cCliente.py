from cObjetoListavel import Objeto_Listavel

class Cliente(Objeto_Listavel):
    def __init__(self, sNome: str, sEndereco: str, sEmail: str) -> None:
        self.__sNome = sNome
        self.__sEndereco = sEndereco
        self.__sEmail = sEmail
    
    def __str__(self) -> str:
        return self.__sNome

    @property
    def nome(self) -> str:
        return self.__sNome
    
    @nome.setter
    def set_nome(self, sNovoNome: str) -> None:
        self.__sNome = sNovoNome
    
    @property
    def endereco(self) -> str:
        return self.__sEndereco
    
    @endereco.setter
    def set_endereco(self, sNovoEndereco: str) -> None:
        self.__sEndereco = sNovoEndereco
    
    @property
    def email(self) -> str:
        return self.__sEmail
    
    @email.setter
    def set_email(self, sNovoEmail: str) -> None:
        self.__sEmail = sNovoEmail
    
    @property
    def info(self) -> list:
        return [self.__sNome, self.__sEndereco, self.__sEmail]