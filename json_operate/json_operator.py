import json

a = {'a': 'a', 'b': ['a', 'b']}
print(a)
json_a = json.dumps(a)
print(json_a)