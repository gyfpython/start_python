# dictionary key is static so it must be number/string/tuple
test_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
test_dict1 = {"address": "CD"}

print('dict length is %d' % len(test_dict))
print(test_dict['Class'])
print(test_dict.get('Class'))
print(test_dict.get('Class1'))

for item, value in test_dict.items():
    print('key: %s, value: %s' % (item, value))

print(str(test_dict))
print(type(test_dict))
print(isinstance(test_dict, dict))
test_dict.update(test_dict1)
print('dict length is %d' % len(test_dict))
print(str(test_dict))
print(test_dict)
# print(test_dict.has_key('Class'))