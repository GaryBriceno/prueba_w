def get_happiness(numbers, like_numbers, dislike_numbers):
    """
    This function get the happiness, consider all the element
    in the array
    """
    happines = 0
    for element in numbers:
        if element in like_numbers:
            happines += 1
        if element in dislike_numbers:
            happines -= 1
    return happines


def get_happiness_without_repetition(numbers, like_numbers, dislike_numbers):
    """
    This function get the happiness, consider only the unique numbers
    """
    numbers = set(numbers)
    happines = 0
    for element in numbers:
        if element in like_numbers:
            happines += 1
        if element in dislike_numbers:
            happines -= 1
    return happines


# To get multiple values
# reference: https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python
n, m = input().split()
n = int(n)
m = int(m)

listado = list(map(int, input().split()))[:n]
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(n, m)
print(listado)

print(get_happiness(listado, a, b))
