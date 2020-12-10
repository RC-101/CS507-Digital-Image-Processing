def get_pivot_by_partition(numList: list, start: int, end: int) -> int:
    pivot = start
    for index in range(start + 1, end + 1):
        if numList[index] <= numList[start]:
            pivot += 1
            numList[index], numList[pivot] = numList[pivot], numList[index]
    numList[pivot], numList[start] = numList[start], numList[pivot]
    return pivot

def quicksort(numList: list, start = 0, end = None):
    if end is None:
        end = len(numList) - 1

    def recursive_quicksort_helper(numList, start, end):
        if start >= end:
            return

        pivot = get_pivot_by_partition(numList, start, end)
        recursive_quicksort_helper(numList, start, pivot - 1)
        recursive_quicksort_helper(numList, pivot + 1, end)
    return recursive_quicksort_helper(numList, start, end)

# Given array in assignment Question
array = [3, 6, 8, 10, 1, 2, 1]
quicksort(array)
print(array)