# When we are bulding complex programs, we need a
# way to pass data that is NOT always
# from the user.  

# Function Arguments - and parameters are ways to 
# pass in data to a function from possibilty 
# another function
# Function Parameters - this is PLACEHOLDER DATA for
# A function . variables in side the curly brackets 

# memory trick- PARAMETER AND PLACE HOLDER BOTH
#  START WITH P
def check_water_depth(depth):
    print(depth)
    print(depth >10) # true if depth is greater than10 feet
    # return depth

#Function Arguments - This is real data that we pass in to 
# the function call 
#Memory trick - if yu make a real world argument






def username(name):
    print("this data is coming from another function")
    return name 

def confirmLogin():
    name = username("Keyon")
    print (name)