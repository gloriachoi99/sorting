#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''

    newlist = []
    i = 0
    j = 0
       
    while i<len(xs) and j<len(ys):
        if cmp==cmp_standard:
            if cmp(xs[i],ys[j]) <= 0:
                newlist.append(xs[i])
                i+=1
            else:  #when cmp == 1
                newlist.append(ys[j])
                j+=1
        else: # when cmp = cmp_reverse
            if cmp(xs[i],ys[j]) <= 0:
                newlist.append(xs[i])
                i+=1
            else:  #when cmp == 1
                newlist.append(ys[j])
                j+=1
    return newlist + xs[i:] + ys[j:]
 




def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    if len(xs) <= 1:
        return xs
    else:
        left = xs[0:len(xs)//2]
        right = xs[len(xs)//2:]
        sorted_left = merge_sorted(left, cmp) # sort the left
        sorted_right = merge_sorted(right, cmp) # sort the right
        return _merged(sorted_left, sorted_right, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    list_less = []
    list_greater = []
    list_equal = []
   

    if len(xs) <= 1:
        return xs
    else:
        p = xs[0]
        for x in xs:
            if x<p:
                list_less.append(x)
            elif x>p:
                list_greater.append(x)
            else: # x == p
                list_equal.append(x)
        sorted_less = quick_sorted(list_less, cmp)
        sorted_greater = quick_sorted(list_greater, cmp)
        
        if cmp==cmp_standard:
            return sorted_less + list_equal + sorted_greater
        else: # if cmp=cmp_reverse
            return sorted_greater + list_equal + sorted_less

def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
    if len(xs) <= 1:
        return xs
    def helper(xs,lo,hi):
        if lo<hi:
            p = partition(xs,lo,hi,cmp)
            helper(xs,lo,p-1)
            helper(xs,p+1,hi)
            return xs
    return helper(xs,0,len(xs)-1)

def partition(xs,lo,hi,cmp=cmp_standard):
    pivot = xs[hi]
    i = lo

    for j in range(lo,hi):
        if (xs[j] < pivot and cmp == cmp_standard) or (xs[j] > pivot and cmp==cmp_reverse):
            xs[i], xs[j] = xs[j], xs[i]
            i += 1
    xs[i],xs[hi] = xs[hi],xs[i]
    return i
