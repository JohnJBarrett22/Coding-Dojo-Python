#1
x[1][0] = 15
print(x)

students[0]['first_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

#2
def key_and_value(arr):
    for i in arr:
        print(i)

key_and_value(students)

#3
def iterate_dictionary(arr, key):
    for i in arr:
        print(i[key])

iterate_dictionary(students,'first_name')

#4
def dojo_info(arr):
    print((len(arr['locations'])), "LOCATIONS", (arr['locations']))
    print((len(arr['instructors'])), "INSTRUCTORS", (arr['instructors']))

dojo_info(dojo)