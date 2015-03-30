__all__ = ["hook", "delete"]

Hooks = {}
Commands = {}

class hook(type):
    def __new__(cls, name, hookid=None):
        self = type.__new__(cls, name, (), {})
        def inner(func):
            if name not in Hooks:
                Hooks[name] = []
            Hooks[name].append(func)
            self.func = func
            return self
        self.hookid = hookid
        return inner

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class cmd(type):
    def __new__(cls, *names, **kwargs):
        self = type.__new__(cls, name, (), {})
        def inner(func):
            for name in names:
                if name not in Commands:
                    Commands[name] = []
                Commands[name].append(func)
            self.func = func
            return self
        self.__dict__.update(kwargs)
        return inner

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def delete(hookid):
    if hookid is not None:
        for name in list(Hooks):
            for func in Hooks[name][:]:
                if func.hookid == hookid:
                    Hooks[name].remove(func)
            if not Hooks[name]:
                del Hooks[name]
