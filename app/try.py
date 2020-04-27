from app import app,db
from app.database.models import MergedAdCategory

_sortedClassDict={0: 'bottle', 1: 'cup', 2: 'person', 3: 'pottedplant', 4: 'umbrella', 5: 'cell phone', 6: 'chair', 7: 'bird', 8: 'clock', 9: 'tie'}

_allResultsWithTupleList = 



db.session.query(exists().where(User.email==email)).scalar()







def returnList(_sortedClassDict,_allResultsWithTupleList):

    finalJsonArray = []
    eachJsonObject = dict()

    counter=0

    for eachkey in range(len(_sortedClassDict)):
        eachJsonObject["Rank"]=eachkey
        eachJsonObject["ItemName"]=_sortedClassDict[eachkey]
        
        timeStampList =[]
        
        for currentTupleList in _allResultsWithTupleList:
            listofDetectedObject = currentTupleList[0]
            timeFrame= currentTupleList[1]

            for eachDetectedobject in listofDetectedObject:
                if eachJsonObject["Item"]==eachDetectedobject["label"]:
                    eachTimeStampObject=dict()
                    eachTimeStampObject["timeInMilliSec"]=timeFrame
                    eachTimeStampObject["x"]=(eachDetectedobject["topleft"]["x"]+eachDetectedobject["bottomright"]["x"])/2
                    eachTimeStampObject["y"]=(eachDetectedobject["topleft"]["y"]+eachDetectedobject["bottomright"]["y"])/2
                    
                    timeStampList.append(eachTimeStampObject)

        eachJsonObject["TimeStamp"]=timeStampList
        # print("EachObject in Array")
        # print(eachJsonObject)
        finalJsonArray.append(eachJsonObject.copy())
    # print("Final list length is {:d} may not be the accurate order".format(len(finalJsonArray)))
    # print(finalJsonArray)

    mainOutput = dict()
    mainOutput["dataPerObject"]=finalJsonArray
    mainOutput["dataPerTimestamp"]=returnTimeStampsList(_sortedClassDict,_allResultsWithTupleList)

    print("\nmainOutput")
    print(mainOutput)
    return mainOutput

def returnTimeStampsList(_sortedClassDict,_allResultsWithTupleList):

    # print("For reference: ")
    # print(_allResultsWithTupleList[0])

    allDataInSimplerFormArray=[]
    uniqueTimeStamps=[]
    uniqueLabels=[]
    for index in range(len(_allResultsWithTupleList)):
        allDataObject=dict()

        eachresult=_allResultsWithTupleList[index]
        objectsInThatFrameList=eachresult[0]

        allDataObject["TimeinMilliSec"]=eachresult[1]

        #Unique TimeStamps
        if eachresult[1] not in uniqueTimeStamps:
            uniqueTimeStamps.append(eachresult[1])


        for eachObject in objectsInThatFrameList:
            allDataObject["Label"]=eachObject["label"]
            if eachObject["label"] not in uniqueLabels:
                uniqueLabels.append(eachObject["label"])

            allDataObject["x"]=(eachObject["topleft"]["x"]+eachObject["bottomright"]["x"])/2
            allDataObject["y"]=(eachObject["topleft"]["y"]+eachObject["bottomright"]["y"])/2
            allDataInSimplerFormArray.append(allDataObject.copy())
    # print("\nuniqueTimeStamps")
    # print(uniqueTimeStamps)

    # print("\nuniqueLabels")
    # print(uniqueLabels)

    # print("\nallDataInSimplerFormArray")
    # print(allDataInSimplerFormArray)

    # print("\n_sortedClassDict")
    # print(_sortedClassDict.values())

    #This line makes the code search for only those labels inside the _sortedClassDict
    #If this line is removed ,all labels will be searched
    uniqueLabels=list(_sortedClassDict.values())

######################Use SimplerDataForm##############################
    finalTimeJsonArray = []
    eachTimeJsonObject = dict()

    for index in range(len(uniqueTimeStamps)):
        eachTimeJsonObject["timeInMilliSec"]=uniqueTimeStamps[index]

        objectsWithCoordinates=[]

        for index1 in range(len(uniqueLabels)):
            currentLabel=uniqueLabels[index1]
            eachObjectWithCoordinate=dict()

            allCoordinates=[]

            for index2 in range(len(allDataInSimplerFormArray)):
                simplerDataObject=allDataInSimplerFormArray[index2]

                if(simplerDataObject["Label"]==currentLabel and simplerDataObject["TimeinMilliSec"]==uniqueTimeStamps[index]):
                    eachObjectWithCoordinate["label"]=currentLabel

                    eachXYObject=dict()

                    eachXYObject["x"]=simplerDataObject["x"]
                    eachXYObject["y"]=simplerDataObject["y"]
                    allCoordinates.append(eachXYObject.copy())


                    eachObjectWithCoordinate["allCoordinates"]=allCoordinates


            if (eachObjectWithCoordinate):
                objectsWithCoordinates.append(eachObjectWithCoordinate)




        eachTimeJsonObject["objectsWithCoordinates"]=objectsWithCoordinates
        finalTimeJsonArray.append(eachTimeJsonObject.copy())
    print("\nfinalTimeJsonArray")
    print(finalTimeJsonArray)

    return finalTimeJsonArray