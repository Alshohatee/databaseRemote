
'''
a remote MySQL databaseconnection '''


import MySQLdb

# Function for connecting to MySQL database
def mysqlconnect():
    port = 3306
    host_name, db_user_name, password, db_name = read_Auth_info()
    # print(host_name, db_user_name, password, db_name)
	# Trying to connect
    try:
        db_connection= MySQLdb.connect(host_name,db_user_name,password,db_name)
	
    # If connection is not successful
    except:
        print("Can't connect to database")
        return 0

	# If Connection Is Successful
    print("Connected")

	# Making Cursor Object For Query Execution
    cursor=db_connection.cursor()

	# Executing Query
    cursor.execute("SELECT CURDATE();")

	# Above Query Gives Us The Current Date
	# Fetching Data
    m = cursor.fetchone()

	# Printing Result Of Above
    print("Today's Date Is ",m[0])

	# Closing Database Connection
    db_connection.close()

# Get the Auth Info
def read_Auth_info():
    f=open("account.txt","r")
    lines=f.readlines()

    # Remove \n from the end
    host_name = lines[0][:-1]
    db_user_name = lines[1][:-1]
    password = lines[2][:-1]
    db_name = lines[3]  # last line no need to remove \n
    f.close()
    return host_name, db_user_name, password, db_name

# Function Call For Connecting To Our Database
mysqlconnect()

