from datetime import datetime
from functools import wraps

def odd_sec(fn):
    """
    This decorator helps to execute the funtions at odd secs only.
    """
    def inner(*args,**kwargs):
        now = datetime.now()
        current_time = now.strftime("%S")
        if int(current_time)%2 != 0 :
            result = fn(*args, **kwargs)
            return result
        else:
            return 'even_sec'
    return inner

@odd_sec
def print_time():
    """
    This function return the time at which the function is executed.
    But since the odd_cec decorator is add to  the function.
    This funtion will be execcuted in the only during the odd secs
    """
    now = datetime.now()
    current_time = now.strftime("%S")
    return current_time


def logged(fn):
    """
    This decorator helps to log the time at which the funtions is executed.
    """
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        return result , f'{run_dt}: called {fn.__name__}'
    return inner

@logged
def div(a,b):
    """
    This division of the inputs 
    """
    c = a/b
    return c


def set_password():
    password = ''
    def inner():
        nonlocal password
        if password == '':
            password = input()
        return password
    return inner
current_password = set_password()

def authenticate(fn,current_password = '123' , user_password = '123'):
    """ 
    This decorator check for the authentication.
    It takes the user password and checks with the current password.
    """
    cnt = 0
    
    if user_password == current_password:
#         @wraps(fn)
        def inner(*args, **kwargs):
            nonlocal cnt
            cnt += 1
            print(f'{fn.__name__} was called {cnt} times')
            return fn(*args, **kwargs)
        return inner
    else:
        print('You scamster!!')

@authenticate
def add(a, b ):
    return a + b

def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn) 
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args) # now it is comma delimited

        print(f'{fn.__name__}({args_str}) took {elapsed} seconds')

        return result
    # inner = wraps(fn)(inner)
    return inner

@timed
def mul(a,b):
    c = a*b
    return c

