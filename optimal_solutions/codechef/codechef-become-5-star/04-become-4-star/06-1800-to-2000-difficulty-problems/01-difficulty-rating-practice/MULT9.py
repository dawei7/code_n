


def solve():
    def rish():

        n = int(input())
        String = input()
        cnt = summ = 0
        for i in String:
            if(i == "?"):          # cnt is the number of '?'
                cnt += 1 
            else:
                summ += int(i)     # summ is the sum of digits 

        if(String[0] == "?"):            # ex (?9 99) & (?? 18 27 36 45 54 63 72 81 90 99)
            print("1" + (cnt - 1) * "0")   

        elif ((summ % 9) == 0):           # sum of all digits is divisible by 9 ex (9? 90 99)
            print(((cnt-1)*"1")+"2")    #ex (9?? 900 909 990 918 927 936 945 954 963 972 981)

        elif((summ % 9) != 0):      # If the sum is not divisible by 9  ex (71? 711)
            print((cnt)*"1")

    for _ in range(int(input())):
        rish()


if __name__ == "__main__":
    solve()
