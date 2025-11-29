from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la Base de Datos SQL (SQLite)
engine = create_engine('sqlite:///base_relacional.db')
Base = declarative_base()

# Entidad 1: Clinicas Particulares
class Clinica(Base):
    __tablename__ = 'clinicas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especialidad_principal = Column(String)
    direccion = Column(String)
    telefono = Column(String)

    def __str__(self):
        return f"Clínica: {self.nombre} | Esp: {self.especialidad_principal}"

# Entidad 2: Parques Recreativos
class Parque(Base):
    __tablename__ = 'parques'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ubicacion = Column(String)
    horario = Column(String)
    tiene_juegos_mecanicos = Column(String)

    def __str__(self):
        return f"Parque: {self.nombre} | Horario: {self.horario}"

# Crear las tablas
Base.metadata.create_all(engine)