import pickle
import csv

def BinToCSV(fileName , CSVname = "CSVfile"):

    with open(fileName + ".dat", "rb") as f:

        File_Data = []

        try:
            while True:
                File_Data.append(pickle.load(f))
        except EOFError:
            pass

        
    #WRITING TITLE FOR THE CSV FILE

    with open(CSVname + ".csv", "w", newline="") as f:


        HeadingList = []
        for d in range(len(File_Data)): #3 Times => (0,3,1)


            for k in range(len(File_Data[d])):
                
                
                for h in File_Data[d]:

                    HeadingList.append(h)
                    
        
        CSVheading = HeadingList[0 : len(File_Data[d]) : 1]

        wobj = csv.writer(f)

        wobj.writerow(CSVheading)