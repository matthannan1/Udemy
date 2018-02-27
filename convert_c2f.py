def convert_c2f(c):
    if c >= -273.15:
        return c * 9/5 + 32
    else:
        return "-273.15C is as cold as it gets, bro."


temperatures=[10,-20,-289,100]

for temp in temperatures:
    print(convert_c2f(float(temp)))
