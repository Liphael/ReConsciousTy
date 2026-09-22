

"""issue 1"""
print("\n\n\n------issue 1------")
def QuadraticEquation(a, b, c):
    """解一元二次方程 ax^2 + bx + c = 0 的函数；输入变量 a, b, c 依序为方程的系数，返回方程的实数根（如果存在）。"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)

QuadraticEquation(1, -5.86, 8.5408)
print(QuadraticEquation(1, -5.86, 8.5408))  



"""issue 2"""
print("\n\n\n------issue 2------")
def ReverseprintFactorial(n):
    """计算 n 的阶乘并以逆序排列结果的函数；输入变量 n 为非负整数。"""
    if n < 0:
        raise ValueError("输入参数n必须是一个非负整数！")
    issue2_output = []
    for i in range(n,0,-1):
        factorial = i
        for ii in range(i-1, 0, -1):
            factorial *= ii
        issue2_output.append(str(factorial))
    return issue2_output

ReverseprintFactorial(10)
print(ReverseprintFactorial(10))



"""issue 3"""
print("\n\n\n------issue 3------")
def SumFactionalFactorial(n):
    """计算从 1 到 n 的阶乘之倒数的和的函数；输入变量 n 为非负整数，返回阶乘之倒数的和的值。"""
    if n < 0:
        raise ValueError("输入参数n必须是一个非负整数！")
    factorial_sum = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        factorial_sum += 1 / factorial
    return factorial_sum

SumFactionalFactorial(10)
print(SumFactionalFactorial(10))
print(SumFactionalFactorial(100))



"""issue 4"""
print("\n\n\n------issue 4------")
def MatrixMultiplication(A, B):
    """计算两个矩阵 A 和 B 的乘积的函数；输入变量 A 和 B 为二维列表，返回矩阵乘积的二维列表。"""
    if len(A[0]) != len(B):
        raise ValueError("轶不对齐，矩阵 A 的列数必须等于矩阵 B 的行数！")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

MatrixMultiplication([[1, 2], [3, 4],[5, 6]], [[7, 8, 9], [10, 11, 12]])
print(MatrixMultiplication([[1, 2], [3, 4],[5, 6]], [[7, 8, 9], [10, 11, 12]]))
MatrixMultiplication([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
print(MatrixMultiplication([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
try:
    MatrixMultiplication([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
except ValueError as e:
    print("Error:", e)
try:
    print(MatrixMultiplication([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]))
except ValueError as e:
    print("Error:", e)



"""issue 5"""
print("\n\n\n------issue 5------")
def ListDivisible(lst, divisor1, divisor2):
    """返回列表中所有能被指定整数参数1整除、且不能被指定整数参数2整除的元素的函数；输入变量 lst 为整数列表，divisor 为指定的整数，返回能被整除的元素列表。"""
    if divisor1 == 0 or divisor2 == 0:
        raise ValueError("分母参数不能为零！")
    divisible_elements = [num for num in lst if num % divisor1 == 0 and num % divisor2 != 0]
    return divisible_elements

listExample = [i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0]
print(listExample)
list1 = [i for i in range(2000, 3200) ]
ListDivisible(list1, 7, 5)
print(ListDivisible(list1, 7, 5))



"""issue 6"""
print("\n\n\n------issue 6------")
def VerifyAllDigitsEvenNumber(number):
    """验证一个整数的所有位数是否都是偶数的函数；输入变量 number 为整数，返回布尔值 True 或 False。"""
    if not isinstance(number, int):
        raise ValueError("输入参数必须是一个整数！")
    else:
        str_number = str(abs(number))
        if all(int(digit) % 2 == 0 for digit in str_number):
            return True
        else:
            return False

issue6_output = []
for i in range(1000, 3000):
    if VerifyAllDigitsEvenNumber(i)==True:
        issue6_output.append(i)
print(issue6_output)



"""issue 7"""
print("\n\n\n------issue 7------")
def CalculateAlphabeticalCharValue(string):
    """计算一个字符串中所有字母的字母值之和的函数；输入变量 string 为字符串，返回字母值之和的整数。"""
    if not isinstance(string, str):
        raise ValueError("输入参数必须是一个字符串！")
    else:
        alphabetical_Char_value = 0
        for character in string:
            if character.isalpha():
                alphabetical_Char_value += 1
        return alphabetical_Char_value

def CalculateDigitalCharValue(string):
    """计算一个字符串中所有数字字符的数字值之和的函数；输入变量 string 为字符串，返回数字值之和的整数。"""
    if not isinstance(string, str):
        raise ValueError("输入参数必须是一个字符串！")
    else:
        digital_Char_value = 0
        for character in string:
            if character.isdigit():
                digital_Char_value += int(character)
        return digital_Char_value
        
test_string_1 = "!!!"
test_string_2 = "   "
test_string_3 = "___"
print("Alphabetical Characters:", CalculateAlphabeticalCharValue(test_string_1), "Digital Characters:", CalculateDigitalCharValue(test_string_1))
print("Alphabetical Characters:", CalculateAlphabeticalCharValue(test_string_2), "Digital Characters:", CalculateDigitalCharValue(test_string_2))
print("Alphabetical Characters:", CalculateAlphabeticalCharValue(test_string_3), "Digital Characters:", CalculateDigitalCharValue(test_string_3))
issue7_input = "Hello World! 123"
print("issue7_input:", issue7_input)
print("Alphabetical Characters:", CalculateAlphabeticalCharValue(issue7_input), "Digital Characters:", CalculateDigitalCharValue(issue7_input))



"""issue 8"""
print("\n\n\n------issue 8------")
def CalculateSumOfFormedNumbers(n):
    """计算由n形成的 n+nn+nnn+nnnn 形式的数字之和的函数；输入变量 n 为整数，返回计算结果的整数。"""
    if not isinstance(n, int):
        raise ValueError("输入参数必须是一个整数！")
    else:
        issue8_sum = n + int(str(n)*2) + int(str(n)*3) + int(str(n)*4)
        return issue8_sum

CalculateSumOfFormedNumbers(9)
print(CalculateSumOfFormedNumbers(9))

# or:

def CalculateSumOfFormedNumbers_2(n):
    """计算由n形成的 n+nn+nnn+nnnn 形式的数字之和的函数；输入变量 n 为整数，返回计算结果的整数。"""
    if not isinstance(n, int):
        raise ValueError("输入参数必须是一个整数！")
    else:
        issue8_sum = 0
        n0 = n
        n1 = int( "%s" % n0 )
        n2 = int( "%s%s" % (n0,n0) )
        n3 = int( "%s%s%s" % (n0,n0,n0) )
        n4 = int( "%s%s%s%s" % (n0,n0,n0,n0) )
        issue8_sum = n1 + n2 + n3 + n4
        return issue8_sum

CalculateSumOfFormedNumbers_2(9)
print(CalculateSumOfFormedNumbers_2(9))
