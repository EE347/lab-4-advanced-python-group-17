import csv  

with open("/home/pi/ee347/lab-4-advanced-python-group-17/task5.csv" , "w") as f:
    names =""
    while (1):

        names = input("Add a Name:")
        if names == "quit":
            break  
        f.write(names +"\n")
    
    f.close()