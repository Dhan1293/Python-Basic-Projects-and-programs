def number_reverse(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num*10 + num % 10
        num = num//10
    return rev_num


number = int(input("Enter number to calculate reverse - "))
print("Reverse of number {} is equal to {} ".format(
    number, number_reverse(number)))