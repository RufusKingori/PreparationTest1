def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age:")
    for s in infile:
        if age in s:
            print(s)



def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age:")
    for s in infile:
        name_age = s.split()
        if int(name_age[1]) == int(age):
            print(s)

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

for i in range (1,100):
    if i%7==0 and i%3==0:
        list1.append(i)
    if i%7==0 and i%3!=0:
        list2.append(i)
        if i%2!=0:
            list3.append(i)
    sum_of_digits = sum(int(digit) for digit in str(i))
    if i%sum_of_digits==0:
        list4.append(i)
    if (pow(sum_of_digits, 2)) == i:
        list5.append(i)


print(list1)


