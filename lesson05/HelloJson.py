import json

x = '{"name":"John", "age":30}'
y = json.loads(x)
print(type(y))
print(y)
print(y['age'])

x2 = '[{"name":"John", "age":30},' \
     '{"name":"Mary", "age":20}]'

y2 = json.loads(x2)
print(type(y2))