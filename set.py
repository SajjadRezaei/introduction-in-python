st = {'amir', 'kevin', 'jac', 'jac'}

print(st)

st.add('majid')
st.update('d')

st.update(('c', 'v'), {'bo', 'op'})

print(st)

if 'amir' in st:
    print('yes')

leters = set("test")

print(leters)

################### dictionary


ages = {'amir': 20, 'jac': 12, 'kevin': 30}

ages2 = dict([('amir2', 20), ('kevin2', 12)])
print(ages2)

print(ages)

ages['ana'] = 43

print(ages)

del ages['jac']

print(ages)

print('amir' in ages)

print('Om' not in ages)

print(ages.items())

for i, item in ages.items():
    print(i, item, end=',')
