class Dictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __call__(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return "Ключ не найден в словаре"

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)