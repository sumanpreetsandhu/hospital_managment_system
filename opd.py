import mysql.connector
import maskpass
import patient_entry 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pyhton"
  )
mycursor = mydb.cursor() 

def login():
    username=input("Enter Username:")
    password=maskpass.askpass() 
    
    sql="SELECT * FROM login WHERE username= %s and password = %s "
    values = (username, password)

    mycursor.execute(sql,values)

    myresult=mycursor.fetchall()

    if len(myresult)>0:
        return True
    else:
        return False
       

log = login()

if log:
    y = 'y'
    while y=='y' or y=='Y':
        print("Enter 1 for New Patient: ")
        print("Enter 2 for Old patient: ")
        print("Enter 3 for Patient List: ")
        print("Enter 4 for Patient History: ")
        print("Enter 5 for Search for Patient: ")
        print("Enter 6 for Delete the Record: ")
        choice = int(input())
        if choice==1:
            patient_entry.newentry()
        elif choice==2:
             patient_entry.repeatentry()
        elif choice==3:
             patient_entry.showresult()
        elif choice==4:
             patient_entry.patienthistory()
        elif choice==5:
             patient_entry.searchresult()
        elif choice==6:
             patient_entry.delete()
          

        y= input("y to continue / any key to exit")
else:
    print("incorrect username or password")

