"""
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat
        swapped = false
        for i = 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap( A[i-1], A[i] )
                swapped = true
            end if
        end for
    until not swapped
end procedure
"""


from random import sample


def random_list(max_num=50, length_l=10):
    """ Create list of random chosen unical digits
    from the range from 0 to max_num."""
    res_list = sample(range(max_num), length_l)
    return res_list


def bubble_sort(list_in):
    """ Process list_in with bubble sort algorithm and return updated list."""
    swapped = True
    while swapped:
        swapped = False  # To know that swapp was happend
        for idx in range(1, len(list_in)):
            if list_in[idx-1] > list_in[idx]:
                list_in[idx], list_in[idx-1] = list_in[idx-1], list_in[idx]
                swapped = True
    return list_in


def is_sorted(list_in):
    """ Return True if list is sorted. """
    sorted_l = list_in.sort()
    print (list_in)
    print (sorted_l)
    print (sorted_l == list_in)


test = random_list()
print (test)
bubble_sort(test)
print (test)
print (is_sorted(test))
print (is_sorted(random_list()))
