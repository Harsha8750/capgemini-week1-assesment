def find_second_largest(numbers):
    # Remove duplicates from the list
    unique_numbers = list(set(numbers))
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None
    
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # Return the second largest number
    return unique_numbers[1]

def main():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(number) for number in numbers]
    
    second_largest = find_second_largest(numbers)
    
    if second_largest is None:
        print("The list does not have a second largest number.")
    else:
        print(f"The second largest number is {second_largest}.")

if __name__ == "__main__":
    main()
