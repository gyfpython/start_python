class LearnList(object):

    def __init__(self, input_list: list):
        self.input_list = input_list

    def remove_duplicate(self):
        return list(set(self.input_list))

    def sort_list(self):
        return sorted(self.input_list)

    def get_length(self):
        return len(self.input_list)

    def get_first_value(self):
        return self.input_list[0]

    def get_last_value(self):
        return self.input_list[-1]

    def get_index(self, index: int):
        try:
            return self.input_list[index]
        except Exception as e:
            print('%s' % e)

    def append_value(self, value):
        self.input_list.append(value)
        return self.input_list

    def pop_element(self, index: int):
        return self.input_list.pop(index)

    def del_element(self, index: int):
        del self.input_list[index]
        return self.input_list

    def remove_value(self, value):
        return self.input_list.remove(value)

    def get_min(self):
        return min(self.input_list)

    def get_max(self):
        return max(self.input_list)


if __name__ == '__main__':
    list1 = [2, 1, 3, 5, 8, 1, 2]
    test = LearnList(list1)
    print(test.remove_duplicate())
    print(test.sort_list())
    print(test.get_length())
    print(test.get_index(2))
    print(test.get_min())
    print(test.get_max())
    print(test.append_value(10))
    print(test.get_max())
