 
def nthRootBisection(n,a,esp):
    if a<0 and (a%2==0 and n%2==0): # Check condition 
        try:
            raise Exception(" Real root does not exist ")
        except Exception as e:
                print(type(e))
                print(e)
        return 0
    else:
        a1=a
        b=0
    def fun(x): # nth root means finding the solution of x^n-a
        res=x**n -a1
        return res
    while(abs(a-b) >esp): # Biection method to find nth root of a integer
        c=(a+b)/2
        if (fun(c)<0 and fun(a)<0) or (fun(c)>0 and fun(a)>0):
            a=c
        else:
            b=c
    print("Approximate ",n,"th root of",a1,"is",round((a+b)/2,2))
nthRootBisection(2,100,0.0001)