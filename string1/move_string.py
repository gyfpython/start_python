def move_a_string(str1: str, str2: str):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1 == str2:
                print('True')
                return True
            else:
                str1 = str1[1:] + str1[0]
            if i == len(str1)-1:
                print("False")
                return False
    else:
        print("False")
        return False


move_a_string('weqweqweqwe123q', 'qweqweqweqwe123')
