from abc import ABC, abstractmethod

class MunicipioDAO(ABC):
    @abstractmethod
    def get_municipio(self, codi_municipio: int) -> dict:
        pass
    
    @abstractmethod
    def create_municipio(self, municipio_data: dict) -> int:
        pass
    
    @abstractmethod
    def update_municipio(self, codi_municipio: int, municipio_data: dict) -> None:
        pass
    
    @abstractmethod
    def delete_municipio(self, codi_municipio: int) -> None:
        pass

class PopulacaoDAO(ABC):
    @abstractmethod
    def get_populacao(self, ano: int, codi_municipio: int) -> dict:
        pass
    
    @abstractmethod
    def create_populacao(self, populacao_data: dict) -> None:
        pass
    
    @abstractmethod
    def update_populacao(self, ano: int, codi_municipio: int, populacao_data: dict) -> None:
        pass
    
    @abstractmethod
    def delete_populacao(self, ano: int, codi_municipio: int) -> None:
        pass

class DengueDAO(ABC):
    @abstractmethod
    def get_dengue(self, casos: int, codi_municipio: int) -> dict:
        pass
    
    @abstractmethod
    def create_dengue(self, dengue_data: dict) -> None:
        pass
    
    @abstractmethod
    def update_dengue(self, casos: int, codi_municipio: int, dengue_data: dict) -> None:
        pass
    
    @abstractmethod
    def delete_dengue(self, casos: int, codi_municipio: int) -> None:
        pass
