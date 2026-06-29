# Taking the input of t and running the loop


def solve():
    for _ in range(int(input())):
        D, d, P, Q = map(int,input().split())
        # quo is the total number of cluster of days
        quo=D//d
        # rem is the remaining days
        rem=D%d
        # Initializng the ans to 0
        ans=0
        # Using the formula of sum = n/2[2a+(n-1)d)] calculating the answer only for clusters
        ans=(quo)*(2*P+(quo-1)*Q)//2
        # Now each of the cluster has d days so multiplying by d
        ans=ans*d
        # Now adding the contribution for the remaining days 
        # For the remaining days we have quo as the coeff. of Q
        # Sum will be P + quo*Q and it will be multiplied with no of remaining days
        a=((P+quo*Q)*rem)
        # Adding it to the answer
        ans+=a
        # Printing the final answer
        print(int(ans))


if __name__ == "__main__":
    solve()
