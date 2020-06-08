"""
获取字符串中连续最长的数字串，包含小数
长度相同取较大的
"""


def get_max_number(str2):
    max1 = ""
    if str2[0] == '.':
        str2 = str2[1:]
    list1 = str2.split('.')
    if len(list1) == 1:
        return list1[0]
    elif len(list1) == 2:
        if list1[-1] == '':
            return list1[0]
        else:
            return str2
    else:
        for i in range(len(list1)-1):
            tmp = list1[i] + '.' + list1[i+1]
            if len(tmp) > len(max1):
                max1 = tmp
            elif len(tmp) == len(max1):
                if float(tmp) >= float(max1):
                    max1 = tmp
        return max1


while True:
    try:
        str1 = input()
        str1 = str1 + 'A'
        temp = ''
        all_num1 = []
        for i in str1:
            if i.isdigit() or i == '.':
                temp = temp + i
            else:
                if temp != "":
                    if temp == '.':
                        temp = ''
                        continue
                    if temp[-1] == '.':
                        all_num1.append(temp[:-1])
                        temp = ''
                    else:
                        all_num1.append(temp)
                        temp = ''
        print(all_num1)
        maxlen = ''
        for test in all_num1:
            maxlentmp = get_max_number(test)
            if len(maxlentmp) > len(maxlen):
                maxlen = maxlentmp
            elif len(maxlentmp) == len(maxlen):
                if float(maxlentmp) >= float(maxlen):
                    maxlen = maxlentmp
                else:
                    pass
            else:
                pass
        print(maxlen)
    except:
        break
