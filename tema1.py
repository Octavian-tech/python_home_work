a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# prima solutie

new_list1 = []

for elem1 in set(a):
    for elem2 in set(b):
        if elem1 == elem2:
            new_list1.append(elem2)

# [1,2,3,5,8,13]
print(new_list1)

# a doua solutie
new_list2 = []

for elem1 in set(a):
    if elem1 in set(b):
        new_list2.append(elem1)
#
# # [1,2,3,5,8,13]
print(new_list2)

# a treia solutie
# a treia solutie mi se pare ca este ce mai rapida fiindca foloseste cumva functii build in
print(list(set(a).intersection(set(b))))
