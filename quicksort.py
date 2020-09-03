# python3

from random import randint

def partition3(array, left, right):
    """
    This function is part of a QuickSort algo that uses 3-way partition.
    The function rearranges the elements in the input (sub)array from index "left" to "right"
    and returns index m1 and m2 so that:
    all elements of index less than m1 is less than the pivot element
    all elements of index between m1 and m2 is equal to the pivot element
    all elements of index greater than m2 is greater than the pivot element
    Example:
    input:
    un-partitioned array = [3, 1, 5, 3, 2, 1]
    left = 0
    right = 5
    output:
    m1 = 3
    m2 = 4
    explanation:
    pivot = 3
    partitioned array = [1, 1, 2, 3, 3, 5]
    """
    # choose pivot element
    pivot = array[left]

    # assuming array contains all values equal to pivot
    m1 = left
    m2 = right

    # scan the array from left to right and rearrange the elements so that:
    # all elements less than pivot are on the far left
    # all elements greater than pivot are on the far right
    # all elements equal to pivot are in the middle
    i = left
    while i <= m2:
        if array[i] < pivot:
            array[i], array[m1] = array[m1], array[i]
            m1 += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[m2] = array[m2], array[i]
            m2 -= 1
        else:
            i += 1

    return m1, m2


def randomized_quick_sort(array, left, right):
    """
    This function sorts a (sub)array from index "left" to "right" using randomized. 3-way partition quicksort
    to better handle array with multiple equal values
    """
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
