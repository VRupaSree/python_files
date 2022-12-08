# data = [{'id': '10', 'animal' : 'cat'},{'id': '11', 'animal' : 'dog'},{'id': '3', 'animal' : 'pigeon'},{'id': '10', 'color' : 'yellow'},{'id': '11', 'color' : 'brown'},{'id': '3', 'color' : 'grey'},{'id': '10', 'type' : 'furry'},
# {'id': '11', 'type' : 'fluffy'},
# {'id': '3', 'type' : 'dirty'}]
# from collections import defaultdict
# ids = defaultdict(dict)
# for d in data:
#     ids[d["id"]].update(d)
#
#
#
# list(ids.values())
# print(ids)

l = [{'empid': 1, 'net': '3k'}, {'empid': 1, 'gross': '5k'}, {'empid': 1, 'pay': '6k'}, {'empid': 2, 'gross': '3k'},
     {'empid': 3, 'gross': '5k'}, {'empid': 3, 'net': '3k'}, {'empid': 4, 'pay': '3k'}]

print([{**l[0],**l[1],**l[2]},{**l[3]},{**l[4],**l[5]},{**l[6]}])

# def key_func(k):
#     return k['empid']
#
#
# l = sorted(l, key=key_func)
# l1 = { }
# for i in range(0, len(l)):
#      if (l[i]['empid'] not in l1):
#          l1.append(l[i]['empid'])
# # for j in range(0, len(l)):
# #     d = l[j]
# #     l[d['empid']].update(l[j])
# # print(l[j])
# # l2 = []
# # for i in l1:
# #     l2.append(l[i])
# print(l1)
