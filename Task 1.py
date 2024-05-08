
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if sorted(arr[j]) <= sorted(pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def find_anagrams(arr):
    quick_sort(arr, 0, len(arr) - 1)
    result = {}
    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]
    return list(result.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = find_anagrams(strs)
print(anagrams)
