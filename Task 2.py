import random
import string
import time
import matplotlib.pyplot as plt


def generate_anagram_strs(size: int, length: int) -> [str]:
    anagrams = []
    for _ in range(size):
        anagram = ''.join(random.choices(string.ascii_lowercase, k=length))
        anagrams.append(anagram)
    return anagrams


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


def measure_performance(size_values, length):
    execution_times = []
    for size in size_values:
        start_time = time.time()
        generate_anagram_strs(size, length)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times


def plot_performance(size_values, execution_times):
    plt.plot(size_values, execution_times, marker='o', linestyle='-')
    plt.title('Performance of Anagram Generation')
    plt.xlabel('Number of Anagrams')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()


size_values = [100, 200, 500, 1000, 2000, 5000, 10000]
length = 4

execution_times = measure_performance(size_values, length)

plot_performance(size_values, execution_times)
'''
Складність даного алгоритму складається з кількох частин:

Генерація анаграм: 
Генерація одного анаграму займає час O(length), де length - це довжина кожного анаграму. 
Це виконується size разів для згенерування всього списку анаграм, тому загальна складність для генерації списку анаграму - O(size * length).

Сортування: 
Сортування виконується за допомогою швидкого сортування, 
яке в середньому має складність O(n log n), де n - це кількість елементів у масиві. 
У цьому випадку n = size, тому складність сортування - O(size log size).

Отже, загальна складність алгоритму становить O(n * k + n log n), 
де n - це кількість анаграм у вхідному списку, а k - це середня довжина кожного анаграму.

При збільшені кількості анаграм у згенерованому списку та довжини анаграми, складність буде зростати, як логарифмічно + n*k.
'''
