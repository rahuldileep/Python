def decorator_func(original_func):
    def wrapper_func(*args,**kwargs):
        print('Wrapper function ran this before {}() function'.format(original_func.__name__))
        return original_func(*args,**kwargs)
    return wrapper_func
@decorator_func
def display():
    print('display function ran')
@decorator_func
def display_info(name,age):
    print('Name: {0}\nAge: {1}'.format(name,age))

display()
display_info('Rahul',25)
