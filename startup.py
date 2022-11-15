from luacomplier.translator import Translator

complier = Translator()

with open('test.py', "r") as f:
    pycode = f.read()

with open("src/server/init.server.lua", "a") as f:
    f.write(complier.translate(pycode))
    f.close()
    print('Done.')
