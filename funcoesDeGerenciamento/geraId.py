import random
import string

def geraId(ids):
    ''' Método que gera uma quantidade de ID '''

    for i in range(ids):
        id = "".join([random.choice(string.digits) for i in range(12)])
        print(id)
    return id

