from google.cloud import firestore
from entity.firestore.content import Content
from repository.firestore.firestore_basic_logic import FirestoreBasicLogic
from utility.contents_exception import ContentNotFoundError, ContentValidationError, ContentDuplicatedError
from utility.logging import LOGGER

class ContentRepository(FirestoreBasicLogic):
    content_collection : firestore.CollectionReference

    def __init__(self) -> None:
        super().__init__()
        self.content_collection = self.firestore_client.collection('contents')
    
    def _before_set(self, content_data : Content) -> tuple[dict, str]:
        super()._before_set()
        # created_atとかのバリデーションをここでしたい
        set_data = content_data.to_dict()
        set_id = set_data.pop('documentId', None)
        return set_data, set_id
    
    def _before_update(self, content_data : Content) -> tuple[dict, str]:
        set_data = content_data.to_dict()
        set_id = set_data.pop('documentId', None)
        if set_id is None:
            raise ContentNotFoundError()
        set_data.pop('createdAt')
        set_data.pop('location')
        set_data.pop('title')
        return set_data, set_id

    def is_exist(self, document_id : str=None) -> bool:
        if document_id is None:
            return False
        return self.content_collection.document(document_id).get().exists

    def create(self, document : Content):
        if self.is_exist(document.document_id):
            raise ContentDuplicatedError()
        add_data, add_id = self._before_set(document)
        self.content_collection.add(document_data=add_data, document_id=add_id)

    def get_by_id(self, document_id : str) -> Content:
        LOGGER.debug('get_by_id start')
        content_snapshot = self.content_collection.document(document_id).get()
        if content_snapshot.exists:
            content = content_snapshot.to_dict()
            LOGGER.debug('{}'.format(document_id))
            content['id'] = content_snapshot.id
            return Content(**content)
        else:
            LOGGER.debug('Content id <{}> does not exist'.format(document_id))
            return None
    
    def get_by_tags(self, tags : list[str]) -> list[Content]:
        query = self.content_collection.where('tag', 'array_contains_any', tags).limit(30)
        contents : list[dict] = []
        for snapshot in query.stream():
            temp_dict = snapshot.to_dict()
            temp_dict['id'] = snapshot.id
            contents.append(temp_dict)
        try:
            return [Content(**content) for content in contents]
        except Exception as err:
            LOGGER.debug(err)
            raise ContentValidationError()
    
    def update_by_id(self, document_data : dict):
        content = Content(**document_data)
        update_data, update_id = self._before_update(content)
        if self.is_exist(update_id):
            self.content_collection.document(update_id).set(update_data, merge=True)
            return
        else:
            raise ContentNotFoundError()

    def delete_by_id(self, document_id : str) -> None:
        try:
            if self.is_exist(document_id):
                self.content_collection.document(document_id).delete()
            return
        except Exception as err:
            LOGGER.debug(err)
            raise ContentNotFoundError()