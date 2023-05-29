import os
import json
from flask import Flask, request, make_response
from flask_cors import CORS
import gunicorn

from service import users_service, contents_service
from utility.contents_exception import ContentsException
from utility.logging import LOGGER
from utility.json_encoder import JsonEncoder
from utility.users_exception import UsersException

METHOD_TYPES = ["GET", "POST", "PUT", "DELETE", "PATCH"]
APP = Flask(__name__)
CORS(
    APP,
    supports_credentials=True,
    methods=METHOD_TYPES
)

@APP.route("/users", methods=METHOD_TYPES)
def users_api():
    try:
        return make_response(json.dumps(users_service.USERS_METHODS[request.method](request), cls=JsonEncoder), 200)
    except UsersException as err:
        return make_response(json.dumps(err.to_json()), err.error_code)


@APP.route("/users/<string:user_id>", methods=METHOD_TYPES)
def user_api(user_id: str):
    try:
        return make_response(json.dumps(users_service.USERS_METHODS['user_id'][request.method](request), cls=JsonEncoder), 200)
    except UsersException as err:
        return make_response(json.dumps(err.to_json()), err.error_code)


@APP.route("/contents", methods=METHOD_TYPES)
def contents_api():
    try:
        return_body = contents_service.CONTENTS_METHODS[request.method](
            request)
        return make_response(json.dumps(return_body, cls=JsonEncoder), 200)
    except ContentsException as err:
        return make_response(json.dumps(err.to_json()), err.error_code)


@APP.route("/contents/<string:content_id>", methods=METHOD_TYPES)
def content_api(content_id: str):
    LOGGER.debug('request : {}'.format(request))
    return make_response(json.dumps(contents_service.CONTENTS_METHODS['content_id'][request.method](content_id), cls=JsonEncoder), 200)


if __name__ == "__main__":
    APP.run()
