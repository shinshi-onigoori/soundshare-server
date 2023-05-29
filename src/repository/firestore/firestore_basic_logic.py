from abc import ABCMeta, abstractmethod

from google.cloud import firestore
from google.oauth2 import service_account

class FirestoreBasicLogic(metaclass=ABCMeta):
    """Firestore にデータを永続化するためのクラスの基底ロジック
    """
    
    firestore_client : firestore.Client

    @abstractmethod
    def __init__(self) -> None:
        """service account を使用してfirestore clientを初期化
        """
        # Use a service account
        credential = service_account.Credentials.from_service_account_file(filename='service_account_info.json')
        self.firestore_client = firestore.Client(
            credentials=credential,
            project=credential.project_id
        )
    
    @abstractmethod
    def _before_set(self):
        pass
