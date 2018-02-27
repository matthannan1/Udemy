temperatures=[10,-20,-289,100]

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

#for t in temperatures:
#    print(c_to_f(t))

with open("temperature_log.txt", "a+") as file:
    for temp in temperatures:
        if c_to_f(temp) != "That temperature doesn't make sense!":
            file.write("\n"+str(c_to_f(temp)))
    