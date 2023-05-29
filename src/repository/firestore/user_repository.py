from google.cloud import firestore

from entity.firestore.user import User
from repository.firestore.firestore_basic_logic import FirestoreBasicLogic
from utility.logging import LOGGER
from utility.users_exception import UserDuplicatedError, UserNotFoundError, WrongPasswordError

class UserRepository(FirestoreBasicLogic):
    content_collection : firestore.CollectionReference

    def __init__(self) -> None:
        super().__init__()
        self.user_collection = self.firestore_client.collection('users')
    
    def _before_set(self, user_data : User) -> tuple[dict, str]:
        super()._before_set()
        # created_atとかのバリデーションをここでしたい
        set_data = user_data.to_dict()
        set_id = set_data.pop('documentId', None)
        return set_data, set_id

    def is_exist(self, document_id : str=None) -> bool:
        if document_id is None:
            return False
        return self.user_collection.document(document_id).get().exists
    
    def get_user_by_id_and_password(self, document_id : str, password : str) -> User:
        user_snapshot = self.user_collection.document(document_id).get()
        if user_snapshot.exists:
            user_dict = user_snapshot.to_dict()
            user_dict['id'] = document_id
            user = User(**user_dict)
            if user.password == password:
                return user
            else:
                raise WrongPasswordError()
        else:
            raise UserNotFoundError()

    def get_all():
        pass

    def get_by_id(self, document_id : str) -> User:
        LOGGER.debug('get_by_id start')
        user_snapshot = self.user_collection.document(document_id).get()
        if user_snapshot.exists:
            user = user_snapshot.to_dict()
            LOGGER.debug('{}'.format(document_id))
            user['id'] = user_snapshot.id
            return User(**user)
        else:
            LOGGER.debug('User id <{}> does not exist'.format(document_id))
            return None

    def create(self, document : User) -> None:
        if self.is_exist(document.document_id):
            raise UserDuplicatedError()
        add_data, add_id = self._before_set(document)
        self.user_collection.add(document_data=add_data, document_id=add_id)

    def update():
        pass