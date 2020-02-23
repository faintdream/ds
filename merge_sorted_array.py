def merge_sorted_array(arr1, arr2):
    new_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1

    print(arr1)
    print(arr2)
    print(new_arr)


arr2 = [1, 3, 9, 99]
arr1 = [0, 1, 2, 3, 4, 5, 6]

merge_sorted_array(arr1, arr2)
