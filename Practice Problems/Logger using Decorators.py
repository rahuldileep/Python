def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__),level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper
@my_logger
def display(name,age):
    print('Name: {0}\nAge: {1}'.format(name,age))
    

display('Rahul',25)
