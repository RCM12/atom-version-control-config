# Sum function
def calculate_sum(a, b):
    answer = a + b
    return answer

def main():
    operand1 = int(input("Enter the first number: "))
    operand2 = int(input("Enter the second number: "))
    sum_result = calculate_sum(operand1, operand2)
    print(sum_result)

main()
