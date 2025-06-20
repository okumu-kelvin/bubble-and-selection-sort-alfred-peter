def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        # Track whether a swap was made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap the elements
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        # If no swaps happened, the list is already sorted
        if not swapped:
            break
    return unsorted_list

nums = [5, 4, 3, 2, 1, 0]
sorted_nums = bubble_sort(nums)
print(sorted_nums)  
