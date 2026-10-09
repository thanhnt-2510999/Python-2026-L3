# 1
def calc_circle_radius():
    r = float(input("Enter radius: "))
    print(f"Area: {3.14 * r * r}")

# 2
def c_to_f():
    c = float(input("Enter temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {c * 1.8 + 32}")

# 3
def find_prime():
    num = int(input("Enter number: "))
    i = 1
    while (i * i <= num):
        i += 1
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
    print(f"{num} is a prime number")

# 4
def find_perfect_num():
    num = int(input("Enter number: "))
    setOfDivisor = find_divisor(num)
    sum = 0
    for divisor in setOfDivisor:
        sum += divisor
    sum =sum - num
    if sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

# 5
def favorite_color():
    colors = ["red", "green", "blue", "yellow", "black", "white"]
    my_color = input("Enter your favorite color: ")
    for index, color in enumerate(colors):
        if my_color == color:
            print(f"Your color is at index {index} in my list")
            return
        
    print(f"Sorry, I could not find your color")

# 6
def print_loop():
    for i in range(0, 7):
        print(i, end=", ")
    print()

    for i in range(1, 11, 3):
        print(i, end=", ")
    print()

    for i in range(5, 0, -1):
        print(i, end=", ")
    print()

    for i in range(6, -3, -2):
        print(i, end=", ")
    print()

# 7
def remove_char(str, char):
    print(str.replace(char, ''))

# 8
def extract_even(list):
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

# 9
def calc_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# 10
def find_divisor(num):
  setOfDivisor = {1, num}
  i = 1
  while (i * i <= num):
    i += 1
    if num % i == 0:
      setOfDivisor.add(i)
      setOfDivisor.add(num // i)
  return setOfDivisor

# 11
def calc_distance(x1, y1, x2, y2):
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 12
def print_rectangle(rowLength, colLength) -> None:
  print('* ' * rowLength)
  for _ in range(0, colLength-2):
    print(('* ' + '  ' * (rowLength-2) + '*'))
  print('* ' * rowLength)

def main() -> None:
    # calc_circle_radius()
    # c_to_f()
    # find_prime()
    # find_perfect_num()
    # favorite_color()
    # print_loop()
    # remove_char("abc$$$", "$")
    # print(calc_factorial(6))
    # print(find_divisor(6))
    print(calc_distance(0, 0, 3, 4))
    # print_rectangle(6, 4)
