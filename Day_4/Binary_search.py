def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
