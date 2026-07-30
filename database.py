from sqlalchemy import create_engine
from base import Base
from models.produto import Produto
from models.equipamento import Equipamento
from models.suplemento import Suplemento
from models.venda import Venda

engine = create_engine(
    "postgresql://postgres:104248652@localhost:5432/estoque_db"
)

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")