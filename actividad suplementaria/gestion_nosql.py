import json

DB_FILE = "base_no_relacional.json"

# --- 1. ESTRUCTURA NO RELACIONAL (Documentos) ---
# En NoSQL no hay tablas fijas, usamos diccionarios/documentos
data_store = {
    "clinicas": [],
    "parques": []
}

# Agregamos Documento 1: Clínica
data_store["clinicas"].append({
    "id": "C001",
    "nombre": "Clinica San Gabriel",
    "servicios": ["Urgencias", "Cardiología", "Laboratorio"], # Lista anidada
    "direccion": {"calle": "Av. America", "numero": 123},     # Objeto anidado
    "es_privada": True
})

# Agregamos Documento 2: Parque
data_store["parques"].append({
    "id": "P001",
    "nombre": "Parque Metropolitano",
    "caracteristicas": ["Senderismo", "Zona de parrillas", "Mirador"],
    "acceso_libre": True
})

# --- 2. GUARDAR (Simulando escritura en base de datos) ---
def guardar_db():
    with open(DB_FILE, 'w') as f:
        json.dump(data_store, f, indent=4)
    print(">>> Datos guardados en formato JSON (NoSQL) correctamente.")

# --- 3. CONSULTAR (Simulando lectura) ---
def consultar_db():
    try:
        with open(DB_FILE, 'r') as f:
            datos = json.load(f)
            
        print("\n--- CONSULTA DE CLINICAS ---")
        for c in datos["clinicas"]:
            print(f"Nombre: {c['nombre']} | Servicios: {c['servicios']}")
            
        print("\n--- CONSULTA DE PARQUES ---")
        for p in datos["parques"]:
            print(f"Nombre: {p['nombre']} | Caracteristicas: {p['caracteristicas']}")
            
    except FileNotFoundError:
        print("La base de datos aun no existe.")

if __name__ == "__main__":
    guardar_db()
    consultar_db()
    