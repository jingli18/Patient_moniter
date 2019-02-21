nums1 = [1,4,8]
nums2 = [2,5,9]
dic = {}
fin = []
res_fin = []
for i in range(2):
    for j in range(2):
        m = ''
        m = str(i)+str(j)
        dic[m] = nums1[i]+nums2[j]
new_dic = {v:k for k,v in dic.items()}
#print(new_dic)
adds = sorted(dic.items(), key = lambda item:item[1])
for i in range(2):

    k = list(adds[i][0])
    print(k)
    fin = [k[0], k[1]]
    res_fin.append(fin)
#print(res_fin)
        