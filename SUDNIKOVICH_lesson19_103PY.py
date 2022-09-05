import inspect


def debug(func):
    def wrapper(a):
        print(f'Имя функции: {func.__name__}')
        print(f'Аргументы функции: {inspect.getfullargspec(func)}\n'
              f'args -- имена позиционных параметров\n'
              f'varargs -- имя аргумента со звёздочкой * или None\n'
              f'varkw -- имя аргумента с двемя звездочками ** или None\n'
              f'defaults -- n-tuple со значениями по умолчанию, соответствуют последним n элементам из args\n'
              f'kwonlyargs -- имена только именованных аргументов (которые идут после * или **)\n'
              f'kwonlydefault -- значения по умолчанию для только именованных аргументов\n'
              f'annotations -- маппинг значений аргументов на аннотации')
        print(f'Значение, которое возвращает функция: {func(a)}')

    return wrapper


@debug
def func_(x):
    b = x
    return b


func_(2)