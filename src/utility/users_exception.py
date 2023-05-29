from abc import abstractmethod


class UsersException(Exception):
    """Userデータを扱う際の基底例外クラス

    Args:
        Exception (_type_): _description_
    """
    error_code : int
    description : str
    message : str

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    @abstractmethod
    def to_json() -> dict:
        pass

class UserDuplicatedError(UsersException):
    """Userデータの登録に重複があった場合の例外

    Args:
        UsersException (_type_): Userデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 409
        self.message = 'signUp failed'
        self.description = 'User ID already exist'

    def __str__(self) -> str:
        super().__str__()
        return '\n'.join([self.message, self.description])
    
    def to_json(self) -> dict:
        return {
            'message' : self.message,
            'description' : self.description
        }

class UserNotFoundError(UsersException):
    """UserIDに紐づくデータが見つからなかった時のエラー

    Args:
        UsersException (_type_): Userデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 404
        self.message = 'signIn failed'
        self.description = 'User ID is not found'

    def __str__(self) -> str:
        super().__str__()
        return '\n'.join([self.message, self.description])
    
    def to_json(self) -> dict:
        return {
            'message' : self.message,
            'description' : self.description
        }

class WrongPasswordError(UsersException):
    """Userのパスワードが誤っていた際のエラー

    Args:
        UsersException (_type_): Userデータを扱う際の基底例外クラス
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 403
        self.message = 'signIn failed'
        self.description = 'User Password is wrong'

    def __str__(self) -> str:
        super().__str__()
        return '\n'.join([self.message, self.description])
    
    def to_json(self) -> dict:
        return {
            'message' : self.message,
            'description' : self.description
        }