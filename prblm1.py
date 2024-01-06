# Write a Python program to find a list of integers with exactly two occurrences
#of nineteen and at least three occurrences of five. Return True otherwise False.
def check_occurrences(lst):
    # Count occurrences of nineteen and five
    count_nineteen = lst.count(19)
    count_five = lst.count(5)

    # Check conditions
    return count_nineteen == 2 and count_five >= 3

# Example usage
input_list = [5, 19, 5, 19, 5, 5, 10, 15]
result = check_occurrences(input_list)
print(result)
