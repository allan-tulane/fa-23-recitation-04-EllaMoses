import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a) <= 1: #base case: if a is empty or size 1 it doesn't need to be sorted, return it
        return a
    else: #recursive case: if a has more than 1 element continue to call qsort until the base case is reached
        p = pivot_fn(a) #find pivot using provided pivot function on list a
        a1 = [] # will hold elements less than p, starts as an empty list
        a2 = [] # will hold elements equal to p, starts as an empty list
        a3 = [] # will hold elements greater than to p, starts as an empty list
        for element in a: #for each element in a, add it to one of the lists
            if element < p:
                a1.append(element)
            elif element == p:
                a2.append(element)
            else:
                a3.append(element)
        s1 = qsort(a1, pivot_fn) #sort list of elements smaller than p using qsort
        s2 = qsort(a3, pivot_fn) #sort list of elements greater than p using qsort
        return s1 + a2 + s2 #combine the sorted sublists
    
def qsort_fixed_pivot(a): 
    return qsort(a, lambda a: a[0])
    
def qsort_random_pivot(a):
    return qsort(a, lambda a: random.choice(a))

#provided in slides
def selection_sort(L):
    for i in range(len(L)):
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[5, 10, 25, 50, 100, 200, 350, 500, 750, 900, 950, 990, 994]): 
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            #time_search(qsort_random_pivot, mylist),
            #time_search(selection_sort, mylist)
            time_search(sorted, mylist)
        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'tim-sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())


random.seed()
test_print()

