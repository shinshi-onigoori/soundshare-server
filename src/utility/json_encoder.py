from datetime import datetime
import json
from typing import Callable
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

class JsonEncoder(json.JSONEncoder):
    def default(self, o: object) -> object:
        ENCODE_FUNCS : dict[type, Callable] = {
            datetime : self.encode_datetime,
            DatetimeWithNanoseconds : self.encode_datetime
        }
        return ENCODE_FUNCS.get(type(o), super().default)(o)

    def encode_datetime(self, value : datetime) -> str:
        return str(value)