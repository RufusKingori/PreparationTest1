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

print("divisible by 7 & 3:",list1)
print("\n divisible by 7 and not 3:",list2)
print("\n odd numbers divisible by 7 and not 3:",list3)
print("\n divisinle by sum of it's digits:",list4)
print("equal to the square of the sum of it's digits:",list5)
