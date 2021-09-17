
from template_parser import TemplateParser

struct = {
    "name": str,
    "width": int,
    "height": int,
}


class PaperLayout(TemplateParser):
    def __init__(self, path):
        super().__init__(path, struct)

        self.name = None
        self.width = None
        self.height = None

        self._store()

    def _store(self):
        self.name = self._body["name"]
        self.width = self._body["width"]
        self.height = self._body["height"]
