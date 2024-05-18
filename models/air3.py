class rogue:

    def __init__(self, *args, **kwargs):
        for arg in args:
            print(arg)
        for kwarg in kwargs.items():
            print(kwarg)

one = rogue(36, 37, 39, name="semo")
print(one)
