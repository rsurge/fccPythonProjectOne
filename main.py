# some things on strings just for your notes


name = 'bongo'
print('hello, ' + name)
print('hello, {}'.format(name))
print(f'hello, {name}')


# project starts below
# madlib


verb = input('Enter present tense verb: ')
adjective = input('Enter adjective with -er: ')
noun = input('Enter a career position: ')

madlib = f'I need to keep {verb}. \nIt is the only way I will get {adjective}. \nI must become a {noun}.'

print(madlib)
