from typing import Callable, Union
from flask import Request
from entity.firestore.content import Content

# from entity.firestore.content import Content
from repository.firestore.content_repository import ContentRepository
from utility.logging import LOGGER
from utility.common_function import get_video_info

CONTENT_REPOSITORY: ContentRepository = ContentRepository()


def create_content(request: Request) -> None:
    req_body = request.json
    video_id = req_body['id']
    video_info = get_video_info(video_id)
    req_body['title'] = video_info['items'][0]['snippet']['title']
    set_content = Content(**req_body)
    try:
        CONTENT_REPOSITORY.create(set_content)
    except Exception as e:
        LOGGER.debug(e)
        raise e


def search_contents(request: Request) -> list[dict]:
    header = request.headers
    tag = header.get('Content-Tags').split(',')
    try:
        return [content.to_dict() for content in CONTENT_REPOSITORY.get_by_tags(tag)]
    except Exception as e:
        LOGGER.debug(e)
        raise e


def delete_content(content_id) -> dict:
    try:
        return CONTENT_REPOSITORY.delete_by_id(content_id)
    except Exception as e:
        LOGGER.debug(e)
        raise e


def update_content(request: Request):
    try:
        rep_body = request.json
        CONTENT_REPOSITORY.update_by_id(rep_body)
        return
    except Exception as e:
        LOGGER.debug(e)
        raise e


def get_content(content_id) -> dict:
    try:
        return CONTENT_REPOSITORY.get_by_id(content_id).to_dict()
    except Exception as e:
        LOGGER.debug(e)
        raise e


CONTENTS_METHODS: dict[str, Union[Callable, dict[str, Union[str, Callable]]]] = {
    "content_id": {
        "GET": get_content,
        "DELETE": delete_content
    },
    "GET": search_contents,
    "POST": create_content,
    "PATCH": update_content
}
