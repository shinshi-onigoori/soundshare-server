from entity.firestore.firestore_document import FirestoreDocument

class User(FirestoreDocument):
    """配信するコンテンツのメタデータのデータモデル

    Args:
        FirestoreDocument (FirestoreDocument): データモデルの基盤
    """
    __json__ : dict
    user_name : str
    password : str
    mail_address : str

    def __init__(self, id : str, userName : str, password : str,**kwargs) -> None:
        """Userの持つ各項目を初期化

        Args:
            id (str): ドキュメントID
            user_name (str): ユーザ名
            password (str): ログインに使用するパスワード
            mail_address (str): ログインに使用するメールアドレス
        """
        super().__init__(id)
        self.user_name = userName
        self.password = password
    
    # TODO 辞書化のたびにパラメータいじるのはきもいので、処理方式を変える
    def to_dict(self) -> dict:
        super().to_dict()
        self.__json__.update({
            'userId' : self.document_id,
            'userName' : self.user_name,
            'password' : self.password
        }) 
        return self.__json__