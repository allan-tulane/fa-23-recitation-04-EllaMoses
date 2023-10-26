# CMPS 2200 Reciation 5
## Answers

**Name:** Ella Moses


Place all written answers from `recitation-05.md` here for easier grading.



- **1b.**

If the lists are randomized, i get the following results: 
|   n |   qsort-fixed-pivot |  qsort-random-pivot |   selection-sort |
|-----|---------------------|---------------------|------------------|
|   5 |               0.008 |               0.008 |            0.009 |
|  10 |               0.012 |               0.013 |            0.009 |
|  25 |               0.031 |               0.036 |            0.026 |
|  50 |               0.064 |               0.078 |            0.081 |
| 100 |               0.141 |               0.177 |            0.290 |
| 200 |               0.306 |               0.387 |            0.996 |
| 350 |               0.539 |               0.636 |            2.934 |
| 500 |               0.903 |               1.060 |            5.833 |
| 750 |               1.330 |               1.523 |           12.779 |
| 900 |               1.562 |               1.963 |           18.389 |
| 950 |               1.707 |               1.998 |           20.551 |
| 990 |               1.920 |               2.391 |           22.474 |
| 994 |               1.735 |               2.127 |           22.751 |


If the lists are already sorted, i get the following results: 
|   n |   qsort-fixed-pivot |   qsort-random-pivot |   selection-sort |
|-----|---------------------|---------------------|------------------|
|   5 |               0.009 |               0.012 |            0.009 |
|  10 |               0.017 |               0.012 |            0.008 |
|  25 |               0.060 |               0.035 |            0.024 |
|  50 |               0.212 |               0.075 |            0.068 |
| 100 |               0.711 |               0.162 |            0.236 |
| 200 |               3.501 |               0.350 |            0.846 |
| 350 |               8.505 |               0.700 |            2.500 |
| 500 |              16.747 |               0.998 |            4.875 |
| 750 |              36.379 |               1.590 |           10.829 |
| 900 |              51.097 |               2.009 |           15.524 |
| 950 |              59.981 |               2.008 |           17.083 |
| 990 |              61.562 |               2.023 |           18.805 |
| 994 |              64.873 |               2.031 |           19.201 |

 
 I modified the sizes of the lists because if the list size was greater than 994, the maximum recursion depth was reached for quicksort with a fixed pivot when the list was already sorted. This is because if the pivot is the first element and the every element to the right is greater, then the list of elements greater than the pivot only decreases by one and it takes almost a thousand recursive calls to reach the base case. 

 For a randomzied list, the two quicksort algorithms are significantly faster than the selection sort algorithm, and the fixed pivot is slightly faster than the randomized pivot. For a sorted list, quicksort with a random pivot is faster than both selection sort and quicksort with a fixed pivot. quicksort with a fixed pivot is significantly slower for large inputs because it takes a large number of recursive calls to reach the base case. 


The work of selection sort is O(n^2). Running selection sort on both the randomized and sorted lists reflect this bound. The worst case work for quicksort is O(n^2) and the averge/best case is O(nlogn). When the list is already sorted, quicksort with a random pivot approximately follows nlogn and quicksort with a fixed pivot is approximately n^2. When the list is randomized both quicksort methods are approximately nlogn.

 

- **1c.**

For a sorted list, the fastest of these sorting functions is quicksort with a random pivot. Comparing this to python's sorted function i get these results:
|   n |   qsort-random-pivot |   tim-sort |
|-----|----------------------|------------|
|   5 |                0.016 |      0.001 |
|  10 |                0.015 |      0.001 |
|  25 |                0.038 |      0.000 |
|  50 |                0.097 |      0.001 |
| 100 |                0.170 |      0.001 |
| 200 |                0.360 |      0.002 |
| 350 |                0.668 |      0.003 |
| 500 |                0.974 |      0.004 |
| 750 |                1.560 |      0.006 |
| 900 |                1.945 |      0.008 |
| 950 |                1.919 |      0.008 |
| 990 |                2.115 |      0.008 |
| 994 |                1.962 |      0.008 |

so for sorted lists, tim sort is signficantly faster than quicksort

For a randomized list, the fastest of these sorting functions is quicksort with a fixed pivot. Comparing this to python's sorted function i get these results:
|   n |   qsort-fixed-pivot |   tim-sort |
|-----|---------------------|------------|
|   5 |               0.007 |      0.002 |
|  10 |               0.010 |      0.001 |
|  25 |               0.037 |      0.002 |
|  50 |               0.060 |      0.004 |
| 100 |               0.137 |      0.023 |
| 200 |               0.345 |      0.019 |
| 350 |               0.605 |      0.036 |
| 500 |               0.855 |      0.053 |
| 750 |               1.362 |      0.081 |
| 900 |               1.782 |      0.102 |
| 950 |               1.672 |      0.107 |
| 990 |               1.724 |      0.112 |
| 994 |               1.919 |      0.112 |

while tim sort is slower for a randomized list than it is for a sorted list, it is still significantly faster than quicksort