import os
import random
import string
import tools
from coffeedb import Cluster
from datetime import datetime

def generar_dato_aleatorio():
    """Genera un dato aleatorio para insertar en una colección."""
    return {
        'nombre': ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        'edad': random.randint(18, 70),
        'email': ''.join(random.choices(string.ascii_lowercase, k=7)) + "@test.com"
    }

def test_insercion_y_seleccion(cluster: Cluster):
    db = cluster['test_db']
    collection = db['usuarios']

    # Crear índices
    collection.create_index('email', unique=True)
    collection.create_index('edad', unique=False)

    # Insertar 10,000 registros en la colección
    for _ in range(10000):
        data = generar_dato_aleatorio()
        sta = datetime.now()
        collection.insert(data)
        end = datetime.now()
        print(f'inserto en {end - sta}')

    # Seleccionar registros con filtro e índice (usar un valor que sabemos está en el rango)
    filtro = {'edad': 25}
    resultados = collection.select(filtro=filtro, limit=10)
    print(f"Registros seleccionados con filtro de edad 25: {len(resultados)}")

def test_actualizacion(cluster):
    db = cluster['test_db']
    collection = db['usuarios']

    # Actualizar registros donde la edad es 25
    filtro = {'edad': 25}
    nuevos_datos = {'grupo': 'joven'}
    resultado_update = collection.update(filtro=filtro, nuevos_datos=nuevos_datos)
    print(f"Registros actualizados: {resultado_update.modified_count}")

def test_borrado(cluster):
    db = cluster['test_db']
    collection = db['usuarios']

    # Borrar registros donde el grupo es 'joven'
    filtro = {'grupo': 'joven'}
    resultado_delete = collection.delete(filtro=filtro)
    print(f"Registros eliminados: {resultado_delete.deleted_count}")

def test_creacion_y_eliminacion_de_bd_y_colecciones(cluster):
    # Crear una nueva base de datos y colección
    db_nueva = cluster.create_database('db_nueva')
    collection_nueva = db_nueva['productos']
    collection_nueva.create_index('codigo', unique=True)

    # Insertar algunos registros en la colección nueva
    for i in range(5000):
        collection_nueva.insert({'codigo': i, 'nombre': f'Producto {i}', 'precio': random.randint(10, 100)})

    # Verificar que existen las bases de datos y colecciones
    dbs = cluster.get_databases_names()
    print(f"Bases de datos existentes: {dbs}")

    col_nombres = db_nueva.get_collections_names()
    print(f"Colecciones en 'db_nueva': {col_nombres}")

    # Eliminar la colección y la base de datos
    db_nueva.delete_collection('productos')
    cluster.delete_database('db_nueva')

def main():
    # Crear el cluster
    cluster = Cluster('data')

    # Ejecutar las pruebas
    print("Iniciando pruebas de inserción y selección...")
    test_insercion_y_seleccion(cluster)

    print("Iniciando pruebas de actualización...")
    test_actualizacion(cluster)

    print("Iniciando pruebas de borrado...")
    test_borrado(cluster)

    print("Iniciando pruebas de creación y eliminación de bases de datos y colecciones...")
    test_creacion_y_eliminacion_de_bd_y_colecciones(cluster)

    print("Todas las pruebas han finalizado.")

if __name__ == "__main__":
    main()
