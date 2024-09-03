def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if the target is not found

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

target = int(input("Enter the number you want to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
