from sqlalchemy.orm import sessionmaker
from modelo_relacional import engine, Clinica, Parque

Session = sessionmaker(bind=engine)
session = Session()

# --- INSERTAR DATOS ---
print("--- INSERTANDO DATOS EN SQL ---")
c1 = Clinica(nombre="Salud Total", especialidad_principal="Cardiologia", direccion="Av. 10 de Agosto", telefono="099123456")
c2 = Clinica(nombre="MediCenter", especialidad_principal="Pediatria", direccion="Calle Loja", telefono="098765432")

p1 = Parque(nombre="Parque La Carolina", ubicacion="Norte", horario="6am - 6pm", tiene_juegos_mecanicos="Si")
p2 = Parque(nombre="Parque Metropolitano", ubicacion="Mirador", horario="5am - 7pm", tiene_juegos_mecanicos="No")

session.add_all([c1, c2, p1, p2])
session.commit()
print("Datos guardados correctamente.\n")

# --- CONSULTAR DATOS ---
print("--- CONSULTANDO CLINICAS ---")
clinicas = session.query(Clinica).all()
for c in clinicas:
    print(c)

print("\n--- CONSULTANDO PARQUES ---")
parques = session.query(Parque).all()
for p in parques:
    print(p)