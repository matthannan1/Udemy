import os, datetime

#now = str(datetime.datetime.now())
# 2018-02-28 13:10:52.574494 needs to become 
# 2017-11-01-13-57-39-170965.txt
#now = now.replace(" ", "-")
#now = now.replace(":", "-")
#now = now.replace(".", "-")+".txt"
# 2018-02-28-13-14-26-241157.txt
#print(now)
#now = datetime.datetime.now()
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"), "a+") as new_file:
    for x in range(3):
        with open("file"+str(x+1)+".txt","r") as file:
            text = file.readline()
            new_file.write(text+"\n")
        
    

