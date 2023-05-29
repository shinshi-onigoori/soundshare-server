from entity.firestore.firestore_document import FirestoreDocument


class Content(FirestoreDocument):
    """配信するコンテンツのメタデータのデータモデル

    Args:
        FirestoreDocument (FirestoreDocument): データモデルの基盤
    """
    __json__: dict
    tag: list[str]
    title: str
    location: str
    description: str

    def __init__(self, id: str, title: str = None, location: str = None, tag: list = [], description: str = '', **kwargs) -> None:
        """配信コンテンツの各項目を初期化

        Args:
            id (str): ドキュメントID
            title (str): コンテンツのタイトル
            tag (list, optional): コンテンツに付けるタグ(検索を助ける). Defaults to [].
        """
        super().__init__(id)
        self.title = title
        self.tag = tag
        self.location = location
        self.description = description

    # TODO 辞書化のたびにパラメータいじるのはきもいので、処理方式を変える
    def to_dict(self) -> dict:
        super().to_dict()
        self.__json__.update({
            'tag': self.tag,
            'title': self.title,
            'location': self.location,
            'description': self.description
        })
        return self.__json__
