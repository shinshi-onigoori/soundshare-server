from abc import ABCMeta, abstractmethod
from datetime import datetime

class FirestoreDocument(metaclass=ABCMeta):
    """Firestoreに格納するデータモデルの基底クラス
    """
    __json__ : dict
    document_id : str
    created_at : datetime
    updated_at : datetime

    @abstractmethod
    def __init__(self, id : str = None) -> None:
        """firestore に格納する上での必須項目の初期化

        Args:
            id (str): ドキュメントID
        """
        self.document_id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    # TODO 辞書化のたびにパラメータいじるのはきもいので、処理方式を変える
    @abstractmethod
    def to_dict(self) -> dict:
        self.__json__ = {
            'documentId' : self.document_id,
            'createdAt' : self.created_at, 
            'updatedAt' : self.updated_at
        }
        return self.__json__