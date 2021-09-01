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


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            print("call function {}".format(func.__name__))
            return func(*args, **kwargs)
        except Exception as e:
            assert Exception("run function: {} error: {}".format(func.__name__, e))
    return wrapper


@log
@try_catch
def test(str1: str):
    print(str1)


@log1('start')
@try_catch
def test1(str1: str):
    print(str1)


test('213')
test1('213')
