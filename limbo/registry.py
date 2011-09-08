from limbo.classes import Singleton

__author__ = 'gdoermann'

class RegistryBase:
    def _1st_init(self, *args, **kwds):
        self.reg= {}
        self.reg.update(kwds)

    def register(self, name, value):
        self.reg[name] = value

    def unregister(self, name):
        del self.reg[name]

    def is_registered(self, name):
        return self.reg.has_key(name)

    def get(self, name):
        return self.reg.get(name)

    def set(self, name, value):
        self.register(name, value)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.set(key, value)

    def all(self):
        return self.values()

    def values(self):
        return self.reg.values()

    def names(self):
        return self.keys()

    def keys(self):
        return self.reg.keys()


class Registry(Singleton):
    pass

generic = Registry()