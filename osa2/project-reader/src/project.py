class Project:
    def __init__(self, tiedot):
        self.tiedot = tiedot

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        s = ""
        a = "Authors: \n"
        depe = "Dependencies: \n"
        d = "Development dependencies: \n"
        for key in self.tiedot:
            if isinstance(self.tiedot[key], str):
                s += key.capitalize() + ": " + self.tiedot[key] + "\n"
                continue
            if key == "authors":
                 for i in self.tiedot[key]:
                     a += "- " + i + "\n"
                 continue
            if key == "dependencies":
                for key in self.tiedot[key]:
                    depe += "- " + key + "\n"
                continue

        for key in self.tiedot['group']['dev']['dependencies']:
            d += "- " + key + "\n"
        return s + "\n" + a + "\n" + depe + "\n" + d
