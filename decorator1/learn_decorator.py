def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text: str):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def test(str1: str):
    print(str1)


@log1('start')
def test1(str1: str):
    print(str1)


test('213')
test1('213')
