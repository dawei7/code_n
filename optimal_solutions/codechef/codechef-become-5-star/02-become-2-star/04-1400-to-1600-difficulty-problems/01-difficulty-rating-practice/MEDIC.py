# cook your dish here


def solve():
    def leap(year):
        if (year%4 == 0 and year % 100 != 0) or (year % 400 == 0) :
            return 1
        return 0



    months = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30, 
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    for _ in range(int(input())):
        s = input()
        year = int(s[0 : 4])
        month = int(s[5 : 7])
        day = int(s[8 :])


        if (leap(year)):
            months[2] = 29
        else:
            months[2] = 28

        odd = 1
        if (day % 2 == 0):
            odd = 0 

        cnt = 0 

        while 1:
            day += 2 
            cnt += 1 
            if(day > months[month]):
                day -= months[month]
                month += 1 
                if month > 12:
                    month = 1 
                    year += 1 
                    if leap(year):
                        months[2] = 29
                    else:
                        months[2] = 28
            if ( day % 2 != odd ):
                break
        print(cnt )


if __name__ == "__main__":
    solve()
