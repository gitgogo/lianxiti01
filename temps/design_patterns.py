# Python实现多线程单例模式
import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


class Singleton(object):
    instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == '__main__':
    a = Singleton(1)
    b = Singleton(2)
    print(id(a), id(b))
