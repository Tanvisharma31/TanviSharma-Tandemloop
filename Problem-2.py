# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......



def generate_odd_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

try:
    a = int(input("Enter value of a: "))
    print("Output:", ', '.join(map(str, generate_odd_series(a))))
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")