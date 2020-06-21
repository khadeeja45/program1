

def SIGMA2 (n):
    total=0;
    for i in range(1,n+1):

        for  j in range(1,i+1):
            if i%j ==0:
                sum=j*j;
                total=total+sum;
    return total;





answer=SIGMA2(1015)%109;
print(answer)
