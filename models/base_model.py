import json

class person:

    def __init__(self, position, level):
        self.position = position
        self.level = level

    def __str__(self):
        return f"I like {self.position} {self.level}"

one = person("anal", "rough")
print(one)
one1 = one.__dict__
print(one1)
one2 = json.dumps(one1)
print(one2)

with open("person.json", "w") as file:
    file.write(one2)

with open("person.json", "r") as f:
    one3 = f.read()

one4 = json.loads(one3)
print(one4)

def create(person, data):
    one5 = person.__new__(person)
    for key, value in data.items():
        setattr(one5, key, value)
    return one5

one6 = create(person, one4)
print(one6)
