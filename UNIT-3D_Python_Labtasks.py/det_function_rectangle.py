def rectangle_area_perimerter(l , b): 
    a =  l * b 
    p = 2 * (l + b)
    return a,p

length=5
breadth=7
area, perimeter = rectangle_area_perimerter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)
