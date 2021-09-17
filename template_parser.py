

import json


class TemplateParser(object):
    def __init__(self, path, struct):
        self._body = None

        self._load(path)
        self._validation(struct, self._body)

    def _load(self, path):
        with open(path, "r") as fh:
            self._body = json.load(fh)

    def _validation(self, struct, body, root_key_name="root"):
        for key, format_type in struct.items():
            if type(body) is not dict:
                raise FormatError(
                    f"type error: '{root_key_name}' is expecting dict type")

            if key not in body:
                raise FormatError(
                    f"'required: {root_key_name}.{key}' is required")

            body_value = body.get(key)

            if type(format_type) is dict:
                self._validation(struct[key], body_value,
                                 f"{root_key_name}.{key}")
                continue

            if type(body_value) is not format_type if type(format_type) is type else type(format_type):
                raise FormatError(
                    f"type error: '{root_key_name}.{key}' is expecting {format_type.__name__} type")


class FormatError(Exception):
    pass
