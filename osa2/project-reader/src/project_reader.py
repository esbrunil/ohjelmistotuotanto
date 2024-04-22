from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        c = toml.loads(content)
        tiedot = c["tool"]["poetry"]
        return Project(tiedot)
