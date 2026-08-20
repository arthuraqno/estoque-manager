from sqlalchemy import create_engine
from base import Base
from models.produto import Produto
from models.equipamento import Equipamento
import os
from dotenv import load_dotenv
from models.suplemento import Suplemento
from models.venda import Venda

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")