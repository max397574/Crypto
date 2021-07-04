#Python code to demonstrate 
#conversion of list of ascii values
#to string
  
#Initialising list
ini_list= [118, 101, 114, 115, 101, 95, 115, 107, 95, 100, 101, 112, 108, 111, 121, 109, 101, 110, 116]  
# Printing initial list
print ("Initial list", ini_list)
  
# Using Naive Method
res = ""
for val in ini_list:
    res = res + chr(val)
  
# Printing resultant string
print ("Resultant string:", str(res))
