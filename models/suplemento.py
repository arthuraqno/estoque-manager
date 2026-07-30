from sqlalchemy import Column, String, Integer, ForeignKey
from models.produto import Produto

class Suplemento(Produto):
    __tablename__ = "suplementos"

    id = Column(Integer, ForeignKey("produtos.id"), primary_key=True)
    sabor = Column(String(50), nullable=False)
    data_validade = Column(String(20), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "suplemento"
    }

    def __str__(self):
        return super().__str__() + f" | Sabor: {self.sabor} | Validade: {self.data_validade}"