import pickle
import csv
import os

def BinToCSV(FilePath , CSVfileName = "CSVfile"):

    with open(FilePath + ".dat", "rb") as f:

        File_Data = []

        try:
            while True:
                File_Data.append(pickle.load(f))
        except EOFError:
            pass

        
    #WRITING TITLE FOR THE CSV FILE

    with open(CSVfileName + ".csv", "w", newline="") as f:


        HeadingList = []
        for d in range(len(File_Data)): #3 Times => (0,3,1)


            for k in range(len(File_Data[d])):
                
                
                for h in File_Data[d]:

                    HeadingList.append(h)
                    
        
        CSVheading = HeadingList[0 : len(File_Data[d]) : 1]

        wobj = csv.writer(f)

        wobj.writerow(CSVheading)



#Read the Binary File

def ReadBinFile(FilePath):

    with open(FilePath + ".dat", "rb") as f:

        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            pass


while True:

    options = ['1 -> Convert Binary File to CSV' , '2 -> Display Data' , '3 -> Exit']

    for opt in options:

        print(opt)
    print()

    getChoice = input("Enter your Choice:")
    print()

    if (getChoice.isdigit()):

        if (int(getChoice) == 1):


            pathMain = input("Enter the Binary File Path and Name:")
            
            askforCSVname = input("Want to give a Custom name for your CSV file(y/n):[By Default: 'CSVfile']")

            if (askforCSVname.lower() == "y"):

                CSVname = input("Enter the name for the CSV file:")

                BinToCSV(pathMain,CSVname)

            else:
                
                
                BinToCSV(pathMain)




        elif (int(getChoice) == 2):

            pathRead = input("Enter the Binary File Path and Name:")

            ReadBinFile(pathRead)


        elif (int(getChoice) == 3):

            print("Program Successfully Terminated !")
            break

        else:

            print("Enter Valid Choice !!!\n")

    else:
        
        print("Enter Valid Choice !!!")