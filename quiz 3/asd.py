
commands = list(open("commands.txt").readlines())

nodeDict = dict()

neighborhoodDict = dict()

splittedCommands = []
for command in commands:
    newValue = command.split("\t")
    splittedCommands.append(newValue)


def operations(command):
    givenCommand = command[1]
    if givenCommand == "CRNODE":
        commandDict = {
            "Command": command[1],
            "Name": command[2],
            "Location": command[3],
            "TransmissionRange": command[4],
            "ResidualBatteryLevel": command[5].removesuffix("\n"),
        }
        commandParameters.createNode(commandDict)
    if givenCommand == "SEND":
        commandDict = {
            "Command": command[1],
            "Name_1": command[2],
            "Name_2": command[3],
            "BYTE": command[4]
        }
        commandParameters.sendInformation(commandDict)
    if givenCommand == "MOVE":
        commandDict = {
            "Command": command[1],
            "Name": command[2],
            "Location": command[3],
        }
        commandParameters.moveNode(commandDict)
    if givenCommand == "CHBTTRY":
        commandDict = {
            "Command": command[1],
            "Name": command[2],
            "ResidualBatteryLevel": command[3],
        }

        commandParameters.changeBattery(commandDict)
    if givenCommand == "RMNODE":
        commandDict = {
            "Command": command[1],
            "Name": command[2].removesuffix("\n"),
        }
        commandParameters.removeNode(commandDict)
    if givenCommand == "INTRUDE":
        commandDict = {  # we will come back here
            "Command": command[1],
            "Name": command[2].removesuffix("\n"),
        }
        commandParameters.intrudeNode(commandDict)


class Node:
    def __init__(self, name, location, transmissionRange, residualBatteryLevel):
        self.name = name
        self.location = location
        self.transmissionRange = transmissionRange
        self.residualBatteryLevel = residualBatteryLevel

    def showNode(self):
        print("name:", self.name)
        print("location:", self.location)
        print("transmissionRange:", self.transmissionRange)
        print("residualBatteryLevel:", self.residualBatteryLevel)


class Nodes(Node):
    def __init__(self, name, location, transmissionRange, residualBatteryLevel):
        super().__init__(name, location, transmissionRange, residualBatteryLevel)


def getNeighborhood():
    for node1 in nodeDict:
        nodeObject = nodeDict.get(node1)
        location = nodeObject.location.split(";")
        transmissionRange = nodeObject.transmissionRange.split(
            ";")  # x1, x2, y1, y2
        transmissionRangeAtSpace = (int(location[0]) + int(transmissionRange[0])
                                    ), (int(location[0]) - int(transmissionRange[1])
                                        ), (int(location[1]) + int(transmissionRange[2])), (int(location[1]) - int(transmissionRange[3]))
        neighborhoodList = list()
        for node in nodeDict:
            nodeObject = nodeDict.get(node)
            location_x, location_y = nodeObject.location.split(";")
            location_x, location_y = int(location_x), int(location_y)
            if (location_x < transmissionRangeAtSpace[0] and location_x > transmissionRangeAtSpace[1]) or location_x == transmissionRangeAtSpace[0] or location_x == transmissionRangeAtSpace[1]:
                if (location_y < transmissionRangeAtSpace[2] and location_y > transmissionRangeAtSpace[3]) or location_y == transmissionRangeAtSpace[2] or location_y == transmissionRangeAtSpace[3]:
                    if node != node1:
                        neighborhoodList.append(node)
                    neighborhoodDict.update({node1: neighborhoodList})


def checkPath(neighboor2, node2, count):

    for d in func(neighboor2, node2):

        for a in d[0]:

            if node2 in neighborhoodDict.get(a):
                # print(a, neighborhoodDict.get(a)[0],"ads")
                # print(node2constant,neighborhoodDict.get(a))
                # if node2constant in neighborhoodDict.get(a):
                #     print(func(a))
                if node2constant in neighborhoodDict.get(a):

                    return a, node2constant
            elif node2 == a:

                return d[1], a
            else:
                # print("calısıyo mu")

                getPaths(neighboor2, node2, count)


def func(node1, node2):

    qwe = list()
    for path in neighborhoodDict.get(node1):

        qwe.append((neighborhoodDict.get(path), path))

    return qwe
    # paths.update({node1:(neighborhoodDict.get(node1),textofdict)})


listof = list()


def getPaths(node1, node2, count):
    count += 1
    somelist = list()
    if count > 2:
        pass

    else:
        listOfNeighboors = func(node1, node2)

        def funcas(x,counter):
            if counter<3:
                for a in getPath(x):
                    print(a)
                    if a == node2:
                        print(node2,"var")
                        # if not (node1,x) in somelist:
                        #     somelist.append((node1, x))
                        # print(somelist)
                    else:
                        counter+=1
                        funcas(a,counter)
        for neighboor1 in listOfNeighboors:
            try:
                counter = 0
                funcas(neighboor1[1],counter)
            except RecursionError:
                print(somelist)
                print("hata cıktı")

            # if neighboor1[1] == node2:
            # print(node1, neighboor1[1])
            # else:

            # for neighboor2 in neighboor1[0]:
            # if neighboor2 == node2:
            #     print(node1, neighboor1[1], neighboor2)
            # else:

            #     for x in getPath(neighboor2):
            #         if x == node2:
            #             print(node1, neighboor1[1], neighboor2, x)
            #         else:
            #             for y in getPath(x):
            #                 if y == node2:
            #                     print(
            #                         node1, neighboor1[1], neighboor2, x, y)
            #                 else:
            #                     for k in getPath(y):
            #                         if k == node2:
            #                             print(
            #                                 node1, neighboor1[1], neighboor2, x, y, k)
            #                         else:
            #                             for a in getPath(k):
            #                                 if k == node2:
            #                                     print(
            #                                         node1, neighboor1[1], neighboor2, x, y, k,a)

        return listof


def getPath(node):
    return neighborhoodDict.get(node)


def iteration(node, node2, counter, realnode1, realnode2):
    # print("iteration")
    counter += 1
    # print(node)
    for a in getPath(node):

        if realnode2 in getPath(a):
            print("var ve", node, getPath(node), a, getPath(a))
            for n in getPath(a):
                if n == node2:
                    print(n, "asd", node, a, n)

        else:
            print(node, getPath(node), a, getPath(a))
            if counter > 5:
                return print("done bcs of counter")

            iteration(a, node2, counter, realnode1, realnode2)

        # if a != node2:
        #     if node not in getPath(a):
        #         liste.append(a)
        #         iteration(a,node2,counter,lista,liste)
        # else:
        #     if node not in getPath(a):
        #         liste.append(a)
        #         lista.append(liste)
        #         print(lista)
        #         liste = list()
        #         print("done")
        #         iteration(a,node2,counter,lista,liste)

            # iteration(a,node2,counter,liste)


# def getPaths(node1,node2):
#     for neighbor1 in neighborhoodDict:
#         if node2 in getPath(neighbor1):
#             print(neighbor1,getPath(neighbor1))
#             print("*******")
#             for neighbor2 in getPath(neighbor1):
#                 if neighbor1 in getPath(neighbor2):
#                     print(neighbor2,getPath(neighbor2))
#                     print("*******")
#                 for neighbor3 in getPath(neighbor2):
#                     if neighbor2 in getPath(neighbor3):
#                         print("*******")
#                         print(neighbor3,getPath(neighbor3))

            # print(neighbor2,getPath(neighbor2))

            # for neighbor3 in neighborhoodDict:
            #     if neighbor3 in getPath(neighbor2):
            #         print("99999")
            #         print(neighbor3,getPath(neighbor3))
    # lista = list()
    # liste = list()
    # counter = 0
    # print("getpaths in ")
    # iteration(node1,node2,counter,node1,node2)
    # print(lista)


class commandParameters:
    def createNode(commandDict):
        nodeObject = Nodes(name=commandDict["Name"],  # create a new object
                           location=commandDict["Location"],
                           transmissionRange=commandDict["TransmissionRange"],
                           residualBatteryLevel=commandDict["ResidualBatteryLevel"])
        # create a new node with object

        nodeDict.update({commandDict["Name"]: nodeObject})
        getNeighborhood()
        print(
            f"COMMAND *{commandDict['Command']}*: New node {commandDict['Name']} is created")

    def sendInformation(commandDict):
        global listof, node1constant, node2constant
        node1 = commandDict.get("Name_1")
        node2 = commandDict.get("Name_2")
        node1constant = node1
        node2constant = node2
        print(
            f"COMMAND *{commandDict['Command']}*: Data is ready to send from {commandDict['Name_1']} to {commandDict['Name_2']}")
        print(neighborhoodDict)
        # print(getPaths(node1, node2,0))
        a = getPaths(node1, node2, 0)
        for s in a:
            if s[0] == node1:
                print(s)

        listof = list()

    def moveNode(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])
        # update the location of that node
        nodeObject.location = commandDict["Location"]
        print(
            f"COMMAND *{commandDict['Command']}*: The location of node {commandDict['Name']} is changed")
        getNeighborhood()

    def changeBattery(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])  # get the object
        # update the battery level of that node
        nodeObject.residualBatteryLevel = commandDict["ResidualBatteryLevel"]
        print(
            f"COMMAND *{commandDict['Command']}*: Battery level of node {commandDict['Name']} is changed to 90")

    def removeNode(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])  # removing
        del nodeDict[commandDict['Name']]  # delete the node from dict
        del nodeObject  # delete object
        print(
            f"COMMAND *{commandDict['Command']}*: Node {commandDict['Name']} is removed")

    def intrudeNode(commandDict):
        print(
            f"COMMAND *{commandDict['Command']}*: Node {commandDict['Name']} has become a malicious node")


for command in splittedCommands:
    operations(command)
