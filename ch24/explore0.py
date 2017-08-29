from collections import abc

class FrozenJSON:
    '''
    一个只读接口，使用属性表示法访问JSON类对象
    '''
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getitem__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj