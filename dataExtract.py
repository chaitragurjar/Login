import pandas as pd

def getUser(username) :
    dataframe = pd.read_csv('UsersData.csv', header = None, names = ["username", "email", "password"])
    
    index = dataframe.index
    rows = len(index)

    password=""
    email=""

    for row in range(rows):
        #print(dataframe._get_value(row, "password"))
        check = dataframe._get_value(row, "username")
        #print(check)
        if check == username:
            password=dataframe._get_value(row, "password")
            email=dataframe._get_value(row, "email")
            #print("password = " + password)
            return (password, email)

    #print(password)
    
    return (password, email)