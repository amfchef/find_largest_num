# the `numbers` argument for this function will always be a list.
def find_largest(numbers):
    numbers.sort()
    #return numbers[-1]
    return numbers[len(numbers)-1]

def sorting(numbers):
    
    print(set(numbers))

some_numbers = [55, 34, 100, 32, 0, 88, 9,]
sorting(some_numbers)
largest = find_largest(some_numbers)

print(largest)
# the expected output here is: `100`
