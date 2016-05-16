import json

obj = {'a': 'b', 'c': 'd'}
fp = open('obj.json', 'w')
json.dump(obj, fp)
fp.close()
s = json.dumps(obj)
x = json.load(open('obj.json', 'r'))
y = json.loads(s)
