# python3

from random import randint

def partition3(array, left, right):
    x = array[left] # pivot element
    # group all x values together on the far lest of the array
    j = left
    for i in range(left+1, right+1):
        if array[i] == x:
            j += 1
            array[j], array[i] = array[i], array[j]
    x_count = j - left + 1

    # group all values < x and value > x to the right of the pivot values
    # the elements in the array should appear in this order (left to right):
    # pivot values > values smaller than pivot values > values greater than pivot values
    k = j
    for i in range(j+1, right+1):
        if array[i] < x:
            k += 1
            array[k], array[i] = array [i], array[k]
    under_x_count = k - j

    # swap all values < x to the beginning of the array and x values to the middle of the array
    # the elements in the array should appear in this order (left to right):
    # values smaller than pivot values > pivot values > values greater than pivot values
    for i in range(0, (k-left)//2+1):
        array[left+i], array[k-i] = array[k-i], array[left+i]

    # return m1 and m2 so that
    # for all left <= k <= m1-1, array[k] < x with x = pivot value
    # for all m1 <= k <= m2, array[k] = x
    # for all m1+1 <= k <= right, array[k] > x
    #
    m1 = left + under_x_count
    m2 = m1 + x_count - 1

    return m1, m2


def randomized_quick_sort(array, left, right):
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
