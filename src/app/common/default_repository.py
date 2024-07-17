import uuid
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from src.app.common.deafult_entity import DefaultEntity

class DefaultRepository:

    def __init__(self):
        self.db = firestore.client()

    def client(self) -> firestore.Client:
        return self.db
    
    def create(self, collection:str, obj:DefaultEntity):
        id = str(uuid.uuid4())
        obj.id = id
        self.db.collection(collection).document(id).set(obj.model_dump())
        return id
    
    def find(self, collection: str, field: str, op: str, value: any):
        return self.db.collection(collection).where(filter=FieldFilter(field, op, value)).get()