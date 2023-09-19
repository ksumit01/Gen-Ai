
# Problem 1: Tuple Unpacking
data = [("John", 25), ("Jane", 30)]

for name, age in data:
    print(f"{name} is {age} years old.")


# Problem 2: Dictionary Manipulation

name_age_dict = {}

def add_name_age(name, age):
    name_age_dict[name] = age

def update_age(name, age):
    if name in name_age_dict:
        name_age_dict[name] = age

def delete_name(name):
    if name in name_age_dict:
        del name_age_dict[name]

add_name_age("John", 25)
print(name_age_dict)  # Output: {'John': 25}

update_age("John", 26)
print(name_age_dict)  # Output: {'John': 26}

delete_name("John")
print(name_age_dict)  # Output: {}

# Problem 3: Two Sum Problem

def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]



# Problem 4: Palindrome Check

def is_palindrome(word):
    cleaned_word = ''.join(word.split()).lower()
    return cleaned_word == cleaned_word[::-1]

word = "madam"
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")


# Problem 5: Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 64]


# Problem 6: Implement Stack using Queue

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        # Move all elements from queue1 to queue2
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        # Add the new item to queue1
        self.queue1.put(item)
        # Move elements back from queue2 to queue1
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())

    def pop(self):
        if not self.queue1.empty():
            return self.queue1.get()
        return None

stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1


# Problem 7: FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")


# Problem 8: File I/O

# Read the file
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words
word_count = len(content.split())

# Write the count to a new file
with open("output.txt", "w") as output_file:
    output_file.write(f"Number of words: {word_count}")


# Problem 9: Exception Handling

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

a = 5
b = 0
result = divide_numbers(a, b)
print(result)  # Output: "Cannot divide by zero."

