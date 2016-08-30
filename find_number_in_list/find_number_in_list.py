#! /usr/bin/python3.4
'''
from the given list, find out the numbers (integer and floats)
'''

def find_nums_in_list(l):
    '''
    Given the list l, return the numbers present in the list
    '''
    return [i for i in l if isinstance(i, float) or isinstance(i, int)]

l = [23, 90.45, 'devil', 'RHEL', 'sentigo', 35, 'uni', 0.34, 'de90']
print (find_nums_in_list(l))
