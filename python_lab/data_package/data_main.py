from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

user_input = input("Enter a comma-separated list of numbers: ")

try:
    data = user_input.split(",")
    data = strip_whitespaces(data)
    numbers = [float(x) for x in data]
    numbers = remove_duplicates(numbers)

    print("Cleaned and unique data:", numbers)
    print("--------------------")

    print(f"Mean: {calculate_mean(numbers):.2f}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")

except:
    print("Data Error: Please make sure you only enter numbers.")