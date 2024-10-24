from typing import Union
from results import DeleteResult, UpdateResult
import requests as req
import coffeedb

class Collection:
    def __init__(self, cluster_name: str, database_name: str, name: str):
        pass

    def stack(self, each):
        # /a/<db>/<collection>/stack
        pass

    def _reload_config(self):
        pass

    def _modificar_config(self, key, value):
        pass

    def get_config(self, key):
        # /a/<db>/<collection>/get_config # data {key: 'config_key'}
        pass

    def create_index(self, field: str, unique: bool = False):
        # /a/<db>/<collection>/create_index # data {name: 'index_name', unique: bool}
        pass

    def _flush_indexes_to_disk(self):
        pass

    def insert(self, data: dict) -> Union[int, None]:
        # /a/<db>/<collection>/insert # data {data: dict}
        pass

    def select(self, filtro=None, project=None, limit=None):
        # /a/<db>/<collection>/select # data {filtro: dict | None, project: dict | None, limit: int | None}
        pass

    def _project(self, data: dict, project: dict):
        pass

    def delete(self, filtro={}) -> DeleteResult:
        # /a/<db>/<collection>/delete # data {filtro: dict}
        pass

    def update(self, filtro={}, nuevos_datos={}) -> UpdateResult:
        # /a/<db>/<collection>/update # data {filtro: dict, nuevos_datos: dict}
        pass

class Db:
    def __init__(self, cluster_name: str, name: str):
        pass

    def __getitem__(self, key):
        # /db/get_collection # data {name: 'collection_name'}
        pass
    
    def get_collections_names(self):
        # /db/get_collections_names
        pass
    
    def get_collections_list(self):
        # /db/get_collections_names # formatearlas
        pass
    
    def delete_collection(self, collection: Union[str, Collection]):
        # /db/delete_collection # data {name: 'collection_name'}
        pass

class CoffeeClient:
    def __init__(self, url: str) -> None:
        # /auth
        pass

    def __getitem__(self, key):
        # /get_db # data {name: 'db_name'}
        pass
    
    def get_databases_names(self):
        # /get_db_names
        pass
    
    def get_databases_list(self):
        # /get_db_names # formatearlo
        pass
    
    def create_database(self, database_name: str):
        # /create_db # data {name: 'db_name'}
        pass

    def delete_database(self, database: Union[str, Db]):
        # /create_db # data {name: 'db_name'}
        pass
