box_list = [['cm', 'mc'], ['ccm', 'mcc'], ['pc', 'mc'], ['pmc', 'mcp']]
count = 0
for box in box_list:
    print(set(box[0]))
    print(set(box[1]))
    if set(box[0]) == set(box[1]):
        count+=1
print(count)
