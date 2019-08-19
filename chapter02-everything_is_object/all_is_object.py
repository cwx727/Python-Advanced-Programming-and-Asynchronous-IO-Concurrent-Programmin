def ask(name='bobby'):
    print(name)

class Person():
    def __init__(self):
        print('bobby2')

list_objs = [ask, Person]
for list_obj in list_objs:
	list_obj()

def decorate_func():
	print('bobby3')
	return ask

my_ask = decorate_func()
my_ask('Tom')




my_func = ask
my_func('bobby')
my_class = Person
my_class()