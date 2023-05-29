from typing import Callable
from entity.firestore.user import User
from flask import Request

# from entity.firestore.content import Content
from repository.firestore.user_repository import UserRepository
from utility.logging import LOGGER

USER_REPOSITORY : UserRepository = UserRepository()

def get_users():
    return

def register_user(request : Request) -> None:
    try:
        user_data = request.json
        register_data = User(**user_data)
        USER_REPOSITORY.create(register_data)
    except Exception as e:
        LOGGER.debug(e)
        raise e

def sign_in(request : Request) -> dict:
    try:
        req_header = request.headers
        doc_id = req_header.get('User-Id')
        password = req_header.get('User-Password')
        user_data = USER_REPOSITORY.get_user_by_id_and_password(doc_id, password)
        return user_data.to_dict()
    except Exception as e:
        LOGGER.debug(e)
        raise e

USERS_METHODS : dict[str, Callable] = {
    "user_id":{
        "GET" : sign_in
    },
    "GET" : get_users,
    "POST" : register_user
}