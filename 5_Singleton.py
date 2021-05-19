class Photo:
    photo = None
    def __new__(cls, name):
        if cls.photo is None:
            cls.photo = object.__new__(cls)
        cls.name = name
        return cls.photo
p = Photo(12)
p_1 = Photo(1)
print(p is p_1)
