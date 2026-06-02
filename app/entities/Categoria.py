class Categoria:

    def __init__(self, id: int = None, descricao: str = ""):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"Categoria(id={self.id}, descricao={self.descricao})"

    def __repr__(self):
        return self.__str__()