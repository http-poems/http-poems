from django.db.models.enums import ChoicesMeta


class MappedChoicesMetaClass(ChoicesMeta):
    def __new__(mcs, classname, bases, classdict, **kwds):
        cls = super().__new__(mcs, classname, bases, classdict, **kwds)
        cls.map = {c[0]: c[1] for c in cls.choices}
        cls.get_by_key = {c[1]: c[0] for c in cls.choices}
        return cls
