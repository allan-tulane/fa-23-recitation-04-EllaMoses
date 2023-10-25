# CMPS 2200 Reciation 5
## Answers

**Name:** Ella Moses


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

If the lists are randomized, i get the following results: 
|     n |   qsort-fixed-pivot |   qsort-random-pivot |   selection-sort |
|-------|---------------------|----------------------|------------------|
|    10 |               0.015 |                0.018 |            0.012 |
|    50 |               0.057 |                0.076 |            0.082 |
|   100 |               0.147 |                0.167 |            0.278 |
|   200 |               0.300 |                0.357 |            1.007 |
|   500 |               0.815 |                0.979 |            5.892 |
|  1000 |               1.849 |                2.055 |           22.847 |
|  2000 |               3.796 |                4.627 |           90.538 |
|  5000 |              11.492 |               12.077 |          567.046 |
|  7500 |              16.922 |               18.877 |         1293.684 |
| 10000 |              22.494 |               26.286 |         2319.683 |

Both quicksort methods are significantly faster than the selection sort method, and the fixes pivot is slightly faster. 

If the lists are already sorted, i get the following results: 
|   n   |   qsort-fixed-pivot |   qsort-random-pivot |   selection-sort |
|-----  |---------------------|----------------------|------------------|
|    10 |               0.022 |                0.021 |            0.014 |
|    50 |               0.220 |                0.075 |            0.069 |
|   100 |               0.748 |                0.158 |            0.239 |
|   200 |               3.674 |                0.370 |            0.841 |
|   500 |              18.005 |                1.007 |            4.850 |
|  1000 |                     |                2.514 |           18.905 |
|  2000 |                     |                5.087 |           74.620 |
|  5000 |                     |               13.710 |          488.614 |
|  7500 |                     |               22.378 |         1057.160 |
| 10000 |                     |               29.406 |         1870.674 |

 

The fixed pivot reached the maximum recursion depth because the function had to be called n times since to reach the base case where the list of elements greater than the pivot is equal to one. This means that this method is the slowest. Selection sort is still significantly slower than random pivot quicksort, but it is faster than for a randomized list.

The work of selection sort is O(n^2). Both the randomized and sorted lists reflect this bound. 
The worst case work for quicksort is O(n^2) and the averge/best case is O(nlogn). When the list is already sorted, quicksort with a random pivot approximately follows nlogn and quicksort with a fixed pivot is approximately n^2 for the values less than 1000. When the list is randomized both quicksort methods are approximately nlogn.

In conclusion, if the list is sorted the fastest method is quicksort with a random pivot and the slowest is quick sort with a fixed pivot at the first index since it reaches the maximum recursion depth and does not finish for large lists. If the list is not sorted both quicksort methods are much faster than selection sort and quicksort with a fixed pivot is slightly faster than quicksort with a random pivot. 






- **1c.**

For a sorted list, the fastest of these sorting functions is quicksort with a random pivot. Comparing this to python's sorted function i get these results:
|     n |   qsort-random-pivot |   tim-sort |
|-------|----------------------|------------|
|    10 |                0.024 |      0.001 |
|    50 |                0.082 |      0.001 |
|   100 |                0.177 |      0.002 |
|   200 |                0.347 |      0.002 |
|   500 |                0.955 |      0.005 |
|  1000 |                2.013 |      0.008 |
|  2000 |                4.584 |      0.017 |
|  5000 |               11.638 |      0.043 |
|  7500 |               18.352 |      0.063 |
| 10000 |               25.653 |      0.085 |

so for sorted lists, tim sort is signficantly faster than quicksort

For a randomized list, the fastest of these sorting functions is quicksort with a fixed pivot. Comparing this to python's sorted function i get these results:
|     n |   qsort-fixed-pivot |   tim-sort |
|-------|---------------------|------------|
|    10 |               0.014 |      0.002 |
|    50 |               0.067 |      0.004 |
|   100 |               0.133 |      0.010 |
|   200 |               0.287 |      0.018 |
|   500 |               0.788 |      0.055 |
|  1000 |               1.739 |      0.116 |
|  2000 |               3.843 |      0.250 |
|  5000 |              10.389 |      0.703 |
|  7500 |              16.151 |      1.126 |
| 10000 |              22.916 |      1.563 |

while tim sort is slower for a randomized list than it is for a sorted list, it is still significantly faster than quicksort