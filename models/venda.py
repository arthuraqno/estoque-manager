from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from base import Base

class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_total = Column(Numeric(10, 2), nullable=False)
    data_venda = Column(Date, nullable=False, default=date.today)

    produto = relationship("Produto")

    def __str__(self):
        return (
            f"Venda #{self.id} | "
            f"Produto: {self.produto.nome} | "
            f"Qtd: {self.quantidade} | "
            f"Total: R${self.preco_total} | "
            f"Data: {self.data_venda}"
        )