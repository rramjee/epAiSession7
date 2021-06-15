import random
import string
from functools import partial
import session7
import pytest
import re
import math
import os
import inspect
import unittest

README_CONTENT_CHECK_FOR = ["global","local","non local","free variable","closure","cell"]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
def test_fibonnaci():
    assert session7.getnextfibonacci()(24) == 34,"Fibonnaci function not working proper"

    
def test_fibonnaci_negative():
    assert session7.getnextfibonacci()(-24) == 0,"Fibonnaci function not working properly for negative numbers"

def test_closure_fibcheck():
    fn=session7.getnextfibonacci()
    assert True == (fn.__closure__ != "") ,"use closure"

def test_check_free_var():
    fn=session7.getnextfibonacci()
    assert ('fibonacci',) == fn.__code__.co_freevars,"free variable needed"

def test_closure_doc_func():
    a1 = session7.docstringcounter(session7.add)
    assert True == (a1.__closure__ != "") ,"use closure"

def addnum(a,b):
    return a+b

def mulnum(a,b):
    '''This is for testing doc string value returned correctly or not in assignment function'''
    return a*b

def test_nodocstring_1():
    assert session7.docstringcounter(session7.mul)(1,2,3) == False,"Unable to handle no doc string"

def test_nodocstring_2():
    assert session7.docstringcounter(session7.add)(1,2) == True,"count logic need to be fixed"

def test_check_free():
    fn=session7.docstringcounter(session7.mul(1,2,3))
    assert ('cnt', 'fn') == fn.__code__.co_freevars,"free variable needed"

def test_fucntion_counter_add():
    
    for i in range(5):
        session7.outer_track(session7.add)()
    assert session7.func_counter['add'] == 5,"There is a counting error "

def test_fucntion_counter_mul():
    
    for i in range(9):
        session7.outer_track(session7.mul)()
    assert session7.func_counter['mul'] == 9,"There is a counting error "

def test_fucntion_counter_div():
    
    for i in range(10):
        session7.outer_track(session7.div)()
    assert session7.func_counter['div'] == 10,"There is a counting error "

def test_outer_track_function_notpresent():
    with pytest.raises(ValueError) as e_info:
        session7.outer_track(session7.merge)()

def test_outer_track_no_param():
    with pytest.raises(TypeError) as e_info:
        session7.outer_track()()

def test_fucntion_counter_2_add():
    counters_test = {'add':10,'mul':0,'div':1}
    for i in range(5):
        session7.counter(session7.add,session7.counters)()
    assert session7.counters['add'] == 5,"There is a counting error "

def test_diff_fucntion_add_counter():
    counters_test = {'add':10,'mul':0,'div':1}
    for i in range(10):
        session7.counter(session7.add,counters_test)()
    assert counters_test['add'] == 20,"There is a counting error "

def test_diff_function_div_notpresent():
    counters_test = {'add':10,'mul':0}
    with pytest.raises(ValueError) as e_info:
        session7.counter(session7.div,counters_test)()

def test_diff_function_empty_dict():
    counters_test = {}
    with pytest.raises(ValueError) as e_info:
        session7.counter(session7.add,counters_test)()

def test_diff_function_not_present():
    counters_test = {'add':0,'mul':0,'div':1}
    with pytest.raises(ValueError) as e_info:
        session7.counter(session7.merge,counters_test)()

def test_diff_fucntion_div_counter():
    counters_test = {'add':0,'mul':0,'div':1}
    for i in range(5):
        session7.counter(session7.div,counters_test)()
    assert counters_test['div'] == 6,"There is a counting error "


def test_function_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_function_annotations():
    """
    Test case to check the function typing are implemented in the function
    definition.
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__


