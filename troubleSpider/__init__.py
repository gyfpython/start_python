import multiprocessing
from time import sleep

test = []


class A(object):

    test2 = []

    def __init__(self, test12: list):
        self.test12 = test12

    def test1(self, string):
        global test
        test.append(string)
        print(len(test))
        print(test)
        # sleep(10)

    def test3(self, string):
        self.test2.append(string)
        print(len(self.test2))
        print(self.test2)
        sleep(5)


if __name__ == '__main__':
    lala = A([])
    pool = multiprocessing.Pool(processes=3)
    pool.map_async(lala.test3, ['a', 'a', 'b'])
    # print(test)
    pool.close()
    pool.join()
    # print(test)
    print('----close----')