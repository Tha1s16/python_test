import math

#print(math.factorial(5))

def calc_factorial(n):
    result = math.factorial(n)
    return result

def test_calc_factorial():
    input_n = 5
    result = calc_factorial(input_n)
    assert result == 120
    print("Passou no teste! O fatorial de " + str(input_n) + " é " + str(result))


