import pytest
from session9 import *
from datetime import datetime
import os


def test_odd_sec_dec():
    now = datetime.now()
    current_time = now.strftime("%S")
    
    ret = print_time()
    if int(current_time)%2 != 0:
        ret != 'even_sec'
    else:
        ret == 'even_sec'
    
def test_log_div():
    ret = div(a= 21,b = 3)
    assert type(ret) == tuple 


def test_auth_add():
    # ret = add(3,5)
    auth_add = authenticate(add, current_password  = 'secret', user_password = 'secret')
    ret = auth_add(2,3)
    assert ret == 5

def test_mul_timed():
    ret = mul(2,3)
    ret == 6