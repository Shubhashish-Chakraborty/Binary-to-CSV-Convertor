import pickle
import csv
import time
import os

def BinToCSV(FilePath , CSVfileName = "CSVfile"):

    with open(FilePath + ".dat", "rb") as f:

        global File_Data
        File_Data = []

        try:
            while True:
                File_Data.append(pickle.load(f))
        except EOFError:
            pass

        
    #WRITING TITLE FOR THE CSV FILE

    with open(CSVfileName + ".csv", "w", newline="") as f:


        HeadingList = []
        for d in range(len(File_Data)):


            for k in range(len(File_Data[d])):
                
                
                for h in File_Data[d]:

                    HeadingList.append(h)
                    
        
        CSVheading = HeadingList[0 : len(File_Data[d]) : 1]

        wobjH = csv.writer(f)

        wobjH.writerow(CSVheading)
    
    UploadData_to_CSV(FilePath,CSVfileName)


def UploadData_to_CSV(fileName , CSVfileName = "CSVfile"):

    #WRITING DATA FOR THE CSV FILE

    with open(CSVfileName + ".csv", "a", newline="") as f:

        wobjD = csv.writer(f)


        for data in range(len(File_Data)):

            AddDataList = []
            for key in File_Data[data]:

                AddDataList.append(File_Data[data][key])

            wobjD.writerow(AddDataList)


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
            time.sleep(1)            
            break
            

        else:

            print("Enter Valid Choice !!!\n")

    else:
        
        print("Enter Valid Choice !!!")