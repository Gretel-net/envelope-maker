
from template_parser import TemplateParser

struct = {
    "to": {
        "filename": str,
        "zip_code": str,
        "address": list,
        "name": list,
    },
}


class TemplateTo(TemplateParser):
    def __init__(self, path):
        super().__init__(path, struct)

        self.filename = None
        self.zip_code = None
        self.address = None
        self.name = None
        self.contents = None

        self._store()

    def _store(self):
        self.filename = self._body["to"]["filename"]
        self.zip_code = self._body["to"]["zip_code"]
        self.address = self._body["to"]["address"]
        self.name = self._body["to"]["name"]
        self.contents = self._body["to"].get("contents")
