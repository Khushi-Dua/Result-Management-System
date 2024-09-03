
import mysql.connector as mysql
connection=mysql.connect(host="localhost",user="root",passwd="2005")
if connection.is_connected():
    print("Connection established")
else:
    print("Connection Error! Kindly check.")

cursor=connection.cursor()
cursor.execute("Create database Result")
cursor.execute("Use Result")
cursor.execute("Create table personalrecord (RollNo Integer,CandidateName Varchar(50), MotherName Varchar(50),FatherName varchar(50),DOB Date)")
cursor.execute("Create table examrecord(Stream varchar(30),TotalMarks integer,Grade char(2),RollNo Integer) ")

ch=1
while ch!=0:
    print("==============Menu===========")
    print("Enter 1 to add record")
    print("Enter 2 to show record")
    print("Enter 3 to edit record")
    print("Enter 4 to show list")
    print("Enter 0 to exit")
    print("=============================")
    ch=int(input("Enter your choice:"))

    if ch==1:
        RollNo=int(input("Enter Roll No.:"))
        Name=input("Enter candidate name:")
        FatherName=input("Enter Father's Name:")
        MotherName=input("Enter Mother's Name:")
        DOB=input("Enter Candidate's DOB:")
        query="Insert into personalrecord values({},'{}','{}','{}','{}')".format(RollNo,Name,FatherName,MotherName,DOB)
        cursor.execute(query)
        Stream=input("Enter your stream:")
        TotalMarks=float(input("Enter total Marks:"))
        Grade=input("Enter ur grade:")
        Query="Insert into examrecord values('{}',{},'{}',{})".format(Stream,TotalMarks,Grade,RollNo)
        cursor.execute(Query)
        connection.commit()

    elif ch==2:

        Candidatename=input("Enter Candidate Name:")
        Query="Select * from personalrecord,examrecord where CandidateName='{}' and personalrecord.RollNo=examrecord.RollNo".format(Candidatename)
        cursor.execute(Query)
        data=cursor.fetchall()
        print("RollNo CandidateName FatherName MotherName DOB Stream TotalMarks Grade RollNo")
        for i in data:
            print(i,end="\n")
        print("\n")
        

    elif ch==3:
        RollNo=int(input("Enter RollNo of candidate:"))
        
        ans="y"
        while ans!="n":
            print("===================Menu=================")
            print("Enter a to edit Candidate's name")
            print("Enter b to edit Candidate Father's name")
            print("Enter c to edit Candidate Mother's name")
            print("Enter d to edit DOB")
            print("Enter e to edit TotalMarks:")
            print("Enter f to edit Grade:")
            print("Enter g to edit full data")
            print("Enter n to exit")
            print("=========================================")
            ans=input("Enter your choice:")

            if ans=="a":
                Name=input("Enter candidate correct name:")
                Query="Update personalrecord set candidatename='{}' where RollNo={}".format(Name,RollNo)
                cursor.execute(Query)

            elif ans=="b":
                FatherName=input("Enter Candidate Father Correct Name:")
                Query="Update personalrecord set FatherName='{}' where RollNo={}".format(FatherName,RollNo)
                cursor.execute(Query)

            elif ans=="c":
                MotherName=input("Enter Candidate Mother Correct Name:")
                Query="Update personalrecord set MotherName='{}' where RollNo={}".format(MotherName,RollNo)
                cursor.execute(Query)

            elif ans=="d":
                DOB=input("Enter correct DOB:")
                Query="Update personalrecord set DOB='{}' where RollNo={}".format(DOB,RollNo)
                cursor.execute(Query)

            elif ans=="e":
                TotalMarks=float(input("Enter correct TotalMarks:"))
                Query="Update examrecord set TotalMarks={} where RollNo={}".format(TotalMarks,RollNo)
                cursor.execute(Query)
                connection.commit()
                query="Update examrecord set Grade='{}' where RollNo={}".format(Grade,RollNo)
                cursor.execute(query)
                connection.commit()

            elif ans=="f":
                Grade=input("Enter candidate's grade:")
                Query="Update examrecord set Grade='{}' where RollNo={}".format(Grade,RollNo)
                cursor.execute(Query)
                connection.commit()

            elif ans=="g":
                    Name=input("Enter candidate name:")
                    FatherName=input("Enter Father's Name:")
                    MotherName=input("Enter Mother's Name:")
                    DOB=input("Enter Candidate's DOB:")
                    Query="Delete from personalrecord where RollNo={}".format(RollNo)
                    cursor.execute(Query)
                    connection.commit()
                    Query="Insert into personalrecord values({},'{}','{}','{}','{}')".format(RollNo,Name,FatherName,MotherName,DOB)
                    cursor.execute(Query)
                    connection.commit()
                    Stream=input("Enter your stream:")
                    TotalMarks=float(input("Enter total Marks:"))
                    Grade=input("Enter candidate's Grade:")
                    Query="Delete from examrecord where RollNo={}".format(RollNo)    
                    cursor.execute(Query)
                    connection.commit()
                    Query="Insert into examrecord values('{}',{},'{}',{})".format(Stream,TotalMarks,Grade,RollNo)
                    cursor.execute(Query)
                    connection.commit()
                    
            elif ans=="n":
                print("Your edit is done successfully")

            else:
                print("Invalid choice chosen")
                
    elif ch==4:
        cursor.execute("Select * from personalrecord,examrecord where personalrecord.RollNo=examrecord.RollNo")
        data=cursor.fetchall()
        for i in data:
            print(i,end="\n")
            print("\n")
    else:
        print("Your Result Analysis is completed")
                    
            
