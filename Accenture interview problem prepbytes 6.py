

def solution(num, divi):
    string = ""
    while num != 0:
        rem = int(num % divi)
        num = int(num/divi)
        if rem > 9:
            string += chr(55+rem)
        else:
            string += str(rem)
    print(string[::-1])


solution(5678, 21)
