def display_names():
    infile = open("names.txt", "r")
    for s in infile:
        if s[0].lower().lower() == "a":
            print(s)



def search_name():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter:")
    for s in infile:
        if s[0].lower() == first_letter[0].lower():
            print(s)



def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age:")
    for s in infile:
        if age in s:
            print(s)


def main():
    search_creteria = input("Enter your search criteria choice: \n1 for search with name  \n2 for search with age\n:")
    if int(search_creteria) == 1:
        search_name()
    elif int(search_creteria) == 2:
        search_age()
    else:
        print("Invalid Choice")

main()