number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 89]
for number in number_list:

    if number < 5:
        print(number)

def print_hi():
    # Use a breakpoint in the code line below to debug your script.

#a task 1
    number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 89]
    for number in number_list:
        if number < 5:
            print(number)


#a task 2
numbers1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

numbers3 = set()
numbers3.update(numbers1)
numbers3.update(numbers2)
for a in numbers3:
    if a in numbers1 and a in numbers2:
        print(a)

print(type(numbers3))

f= "jfdfgdhsj"
d= {}
for i in f:
    d.update({i:f.count(i)})
print(d)

#a task 3
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_elem = sample_list[-1]
first_elem = sample_list[-9]
print('Last Element: ', last_elem)
print('First Element: ', first_elem)

