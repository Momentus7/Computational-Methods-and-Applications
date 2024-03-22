from scipy.fft import fft, ifft
import math


def Approx_Product(n,m):
    """
     find Approx Product of two large numbers in nlogn
    """
    # Counting total number of digits in both integer
    total_digits=len(str(a))+len(str(b))
    digits_n=[]
    digits_m= []
    for _ in range(total_digits):
        digits_n.append(n % 10)
        n=n // 10
        digits_m.append(m % 10)
        m=m // 10

    # Apply FFTs for converting time domain data to frequency domain data in form (Amplitude and phrase )
    #e^(iwt)=cos(wt)+isin(wt) w=frequency and t in time
    fft_n = fft(digits_n)
    fft_m = fft(digits_m)

    # Multiplcation of the FFTs is much faster 
    prod = fft_n * fft_m
    #print(prod)

    #Inverse FFT to get back to time domain data after multiplication
    prod = ifft(prod)
    #print(prod)

    # Computing  final product
    result = 0
    power = 0
    for num in prod:
        result += (num.real) * (10**power)
        power += 1
    result=int(result)
    print("Computed Product using fft: ",result)


n=int(input("Enter first Number :  "))
m=int(input("Enter Second Number : "))
Approx_Product(n,m)
print("Actual Product: ",n*m)