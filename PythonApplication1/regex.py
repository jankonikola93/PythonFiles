import re
def provera(string):
    if re.match("^[a-zA-Z_][a-zA-Z0-9_\s]+$", string):
        return True
    return False
def pocetak(string):
    if re.match("^[a-zA-Z_]", string):
        return True
    return False