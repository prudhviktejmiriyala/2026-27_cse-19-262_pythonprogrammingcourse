def simple_intrest(principal, time, rate =5):
    si =(principal*time*rate)/100
    return si

intrest1= simple_intrest(10000,2)
print("simple intrest:", intrest1)
intrest2= simple_intrest(10000,2 ,8)
print("simple intrest:",intrest2)