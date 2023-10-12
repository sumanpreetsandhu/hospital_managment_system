import mysql.connector
from tabulate import tabulate
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pyhton"
  )

mycursor = mydb.cursor() 
def newentry():
    name = input("Enter Name: ")

    name = name.strip()

    if len(name)==0:
        print("Enter a valid name: ")
        quit()  
        
    name = name.capitalize()

    father = input("Enter father's name: ")

    father = father.strip()

    if len(father)==0:
        print("Enter a valid name: ")
        quit()  
        
    father = father.capitalize()


    mobile  = int(input("Enter Phone Number: "))

    age  = int(input("Enter Age: "))

    address  = (input("Enter Address: "))

    sym = (input("Enter the Symptoms of the Patient: "))

    pres = (input("Enter Prescription: "))

    fees = float(input("Enter the Fees: "))

    cmd = "INSERT INTO patient (name, father, mobile, age, address) VALUES (%s, %s, %s, %s, %s)"
    values =(name, father, mobile, age, address)

    mycursor.execute(cmd, values)

    mydb.commit()   
    sql= "SELECT * FROM patient order by p_id DESC limit 1 "

    mycursor.execute(sql)
   
    myresult = mycursor.fetchall()
    for x in myresult:
        pid = x[0]
    #print(pid)     

    x = datetime.datetime.now()
    dt= str(x.day)+"/"+str(x.month)+"/"+str(x.year)

    tm= (x.strftime("%X"))

    cmd = "INSERT INTO patient_history (p_id, date, time, symptoms, prescription, fees) VALUES (%s, %s, %s, %s, %s, %s)"
    values =(pid, dt, tm, sym, pres, fees)

    mycursor.execute(cmd, values)

    mydb.commit()
    #---------------------------------------------------------------------------------------------------------------------------
def repeatentry():

    pid= int(input("Enter Patient ID: "))

    sym = (input("Enter the Symptoms of the Patient: "))

    pres = (input("Enter Pescription: "))

    fees = float(input("Enter the Charges: ")) 

    x = datetime.datetime.now()
    dt= str(x.day)+"/"+str(x.month)+"/"+str(x.year)

    tm= (x.strftime("%X"))

    cmd = "INSERT INTO patient_history (p_id, date, time, symptoms, prescription, fees) VALUES (%s, %s, %s, %s, %s, %s)"
    values =(pid, dt, tm, sym, pres, fees)

    mycursor.execute(cmd, values)

    mydb.commit()

#------------------------------------------------------

def showresult():
    
    cmd ="SELECT * FROM patient"
    
    mycursor.execute(cmd)

    myresult = mycursor.fetchall()
    data=[]
    if len(myresult)>0:

        for x in myresult:
           data.append(x) 
         
        print(tabulate(data) )
    
    else:
        print("no record found")

#------------------------------------------------------

def patienthistory():

    pid= int(input("Enter Patient ID: "))
    
    cmd ="SELECT * FROM patient_history where p_id = %s"
    values= (pid,)
    
    mycursor.execute(cmd, values)

    myresult = mycursor.fetchall()
    data=[]
    print("Patient ID")
    if len(myresult)>0:

        for x in myresult:
           data.append(x) 
         
        print(tabulate(data) )
    
    else:
        print("no record found")

#----------------------------------------------------------

def searchresult():

    name = input("Enter Name, Mobile Number or Patient ID to search: ")
    '''cmd ="SELECT * FROM employees where address = %s;
    values = (adr,)
    mycursor.execute(cmd, values)

     SELECT * FROM employees where address = '%adr%' '''
    cmd ="SELECT * FROM patient where name like '%"+name+"%' or mobile like '%"+name+"%' or p_id like '%"+name+"%' " 

    
    mycursor.execute(cmd)    

    
   
    myresult = mycursor.fetchall()
    data=[]

    if len(myresult)>0:

        for x in myresult:
           data.append(x) 
         
        print(tabulate(data) )
    else:
        print("no record found")    
    
#----------------------------------------------------------

def delete():

    name = input("Enter name: ")
   
    cmd ="DELETE FROM patient where name = %s"
    values = (name,)
   
   
    mycursor.execute(cmd, values)          

    mydb.commit()  
    
    if mycursor.rowcount>0:                     
        print("Entry deleted successfully")
    else:
        print("Name not macthed, try again..")  
         

