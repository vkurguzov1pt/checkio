import json
from collections import OrderedDict

d = {}
#
print(d)

with open('/opt/pythontests/mkb10/mkb/A00-B99_1.json') as j_data:
	result = json.load(j_data)
j_data.close()

# print(len(result))
# print(len(code_urls))
print("-----------------------------------------------")


#print((result))

# for category_number in range(0,len(result)):
# 	sub = {}
# 	for j in range(0,len(result[category_number]['the_code'])):
# 		sub[result[category_number]['the_code'][j]] = result[category_number]['the_desc'][j]
# 	d[code_urls[category_number]] = sub

# print(d)

for i in result:
	sub = OrderedDict()
	for j in range(0, len(i['code'])):
		sub[i['code'][j]] = [i['description'][j]]
	#print(sub)
	#print("------------------------------------------------------------------------------------")
	#print("{}-{}".format(sub.keys()[0],sub.keys()[-1]))
	list_keys = list(sub.keys())
	d["{}-{}".format(list_keys[0], list_keys[-1])] = sub
#print(d)

with open('/opt/pythontests/mkb10/mkb/A00-B99_1_4.json', 'w') as r_data:
	json.dump(d, r_data, sort_keys=True, ensure_ascii=False)
r_data.close()
