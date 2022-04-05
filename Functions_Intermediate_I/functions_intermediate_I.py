x = [[5, 2, 3], [15, 8, 9]] #change 10 to 15
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'}, # change jordan to bryant
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Andres', 'Ronaldo', 'Rooney'] # change andres to messi
}
z = [{'x': 10, 'y': 30}] # change y from 20 to 30

def interateDictionary(some_list: list): # giving a list of dictionaries and function loops each fictionary
    for i in some_list:
        if i:
            sorted_keys = sorted(list(i.keys()))
            pairs = [f"{k} - {i[k]}" for k in sorted_keys]
            s = ", ".join(pairs)
            print(s)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i.get(key_name))


def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{len(v)} {k.upper()}")
        for i in v:
            print(i)
        print()

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
