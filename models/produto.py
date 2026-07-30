from sqlalchemy import Column, Integer, String, Numeric
from base import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    quantidade = Column(Integer, nullable=False)
    categoria = Column(String(50), nullable=False)
    tipo = Column(String(20), nullable=False)

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "produto"
    }

    def __str__(self):
        return f"[{self.id}] {self.nome} | R${self.preco} | Qtd: {self.quantidade} | {self.categoria}"