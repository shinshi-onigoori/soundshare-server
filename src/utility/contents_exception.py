class ContentsException(Exception):
    """Contentデータを扱う際の基底例外クラス

    Args:
        Exception (_type_): _description_
    """
    error_code : int
    description : str
    message : str

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        super().__str__()
        return '\n'.join([self.message, self.description])

    def to_json(self) -> dict:
        return {
            'message' : self.message,
            'description' : self.description
        }

class ContentValidationError(ContentsException):
    """Contentデータの項目に不備があった際の例外

    Args:
        ContentsException (_type_): Contentデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 500
        self.message = ' failed'
        self.description = 'User ID already exist'

class ContentNotFoundError(ContentsException):
    """ContentIDに紐づくデータが見つからなかった時のエラー

    Args:
        ContentsException (_type_): Contentデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 404
        self.message = 'getting content failed'
        self.description = 'Content ID is not found'

class ContentDuplicatedError(ContentsException):
    """Contentデータの登録に重複があった場合の例外

    Args:
        ContentsException (_type_): Contentデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 409
        self.message = 'registering content failed'
        self.description = 'Content already exist'