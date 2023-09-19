# Anagram Check:

def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

word1 = "cinema"
word2 = "iceman"
result = are_anagrams(word1, word2)
print(result)  # Output: True


# Bubble Sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]


# Longest Common Prefix:

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for word in strs:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]
    return prefix

strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)  # Output: "fl"


# String Permutations:

from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

s = "abc"
result = string_permutations(s)
print(result)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']



# Implement Queue using Stack:

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.enqueue(3)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3



# Missing Number:

def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total - actual_sum

nums = [3, 0, 1]
result = missing_number(nums)
print(result)  # Output: 2


# Power of Two:

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = 16
result = is_power_of_two(n)
print(result)  # Output: True


# Contains Duplicate:

def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

nums = [1, 2, 3, 1]
result = contains_duplicate(nums)
print(result)  # Output: True


# Binary Search:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

arr = [1, 2, 3, 4, 5, 6]
target = 4
result = binary_search(arr, target)
print(result)  # Output: 3



# Single Number

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 1, 2, 1, 2]
result = single_number(nums)
print(result)  # Output: 4
