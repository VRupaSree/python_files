lst = [1,2,3,3,5,4,3,2,1,5,4,3,2,1,0,4,6,5,3,1,5,2]
uniq = set(lst)
result = {}
for kk in uniq:
    count = 0
    for ll in lst:
        if kk == ll:
            count += 1
    result[kk] = count

print(result)





