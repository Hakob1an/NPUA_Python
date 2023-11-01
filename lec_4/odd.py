def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

if __name__ == "__main__":
    while True:
        input_str = input("Enter a list of numbers separated by spaces (or 'exit' to quit): ")

        if input_str.lower() == "exit":
            break

        try:
            numbers = [int(x) for x in input_str.split()]
            even_nums, odd_nums = classify_numbers(numbers)
            print("Even numbers:", even_nums)
            print("Odd numbers:", odd_nums)
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by spaces.")
