def find_greatest_number(numbers):
    if not numbers:
        return None
    greatest = numbers[0]
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest

# Input from user
try:
    user_input = input("Enter numbers separated by spaces: ")
    number_list = list(map(int, user_input.split()))
    greatest_number = find_greatest_number(number_list)
    
    if greatest_number is not None:
        print(f"The greatest number in the list is: {greatest_number}")
    else:
        print("The list is empty.")
except ValueError:
    print("Please enter only valid integers separated by spaces.")
