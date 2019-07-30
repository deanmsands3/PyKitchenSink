__author__ = 'Dean M. Sands, III (deanmsands3@gmail.com)'


# Borrowed code from: https://stackoverflow.com/a/307263/234826
class start_and_end(object):
    _debugging = False

    @classmethod
    def _print(cls, message):
        print(cls, message)

    _logging_function = _print

    @classmethod
    def do_nothing(cls, func):
        pass

    @classmethod
    def start_func_debugging(cls, func):
        cls._logging_function("Function {0} started".format(func))

    @classmethod
    def end_func_debugging(cls, func):
        cls._logging_function("Function {0} ended".format(func))

    start_func = do_nothing
    end_func = do_nothing

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, type=None):
        return self.__class__(self.func.__get__(obj, type))

    def __call__(self, *args, **kw):
        start_and_end.start_func(self.func)
        func_self = self.func(*args, **kw)
        start_and_end.end_func(self.func)
        return func_self

    @classmethod
    def update_logging_function(cls, logging_function):
        cls._logging_function = logging_function


    @classmethod
    def update_debugging(cls, debugging=None):
        if debugging is not None:
            cls._debugging = debugging
        else:
            cls._debugging = ('DEBUGGING' in globals() and globals().get('DEBUGGING'))
        cls._update_debugging_functions()

    @classmethod
    def _update_debugging_functions(cls):
        if cls._debugging:
            cls.start_func = cls.start_func_debugging
            cls.end_func = cls.end_func_debugging
        else:
            cls.start_func = cls.do_nothing
            cls.end_func = cls.do_nothing


start_and_end.update_debugging()
