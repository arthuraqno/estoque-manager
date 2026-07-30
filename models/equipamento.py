from sqlalchemy import Column, String, Integer, ForeignKey
from models.produto import Produto

class Equipamento(Produto):
    __tablename__ = "equipamentos"

    id = Column(Integer, ForeignKey("produtos.id"), primary_key=True)
    tamanho = Column(String(10), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "equipamento"
    }

    def __str__(self):
        return super().__str__() + f" | Tamanho: {self.tamanho}"