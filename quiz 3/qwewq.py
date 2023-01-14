
commands = list(open("commands.txt").readlines())

nodeDict = dict()

node1 = None
node2 = None

timer = 0
byte = 0
packageSize = 0
np = 0
neighborhoodDict = dict()

splittedCommands = []
for command in commands:
    newValue = command.split(" ")
    splittedCommands.append(newValue)


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

counter = 0
addlist = list()

def getPaths(node1, node2):
    global counter,addlist
    thelistWillRemove = []
    addlist = list()
    thelistWillAppend = [[node1]]

    def recurseGetPaths(thelist):
        for liste in thelist:
            for neighboor in getPath(liste[-1]):
                thelist.append([liste[-1]])
                thelist[-1] = [liste,neighboor]
        for paths in thelist:
            if node2 in paths:
                addlist.append(paths)

    recurseGetPaths(thelistWillAppend.copy())
    liste = []
    def localGetPaths(path):
        if path[0] == node1:
            return liste.append(path[0])
        liste.append(path[1])


        return localGetPaths(path[0])

    for path in addlist:
        a = localGetPaths(path)
        liste = list(reversed(liste))
        if liste not in thelistWillRemove:
            thelistWillRemove.append(liste)
        liste = []
        
                
                
    return thelistWillRemove


def getPath(node):
    if type(node) == list:
        return neighborhoodDict.get(node[-1])
    else:
        return neighborhoodDict.get(node)



def costCalculator(paths):
    minOfDistanceList = list()
    print(paths)
    counter = 0
    for path in paths:
        costList = list()
        for node in range(1, len(path)+1):
            nodeObjectFirst = nodeDict.get(path[-node])
            locationFirst = (nodeObjectFirst.location).split(";")
            try:
                nodeObjectSecond = nodeDict.get(path[-node-1])
            except IndexError:  # means that we reached the limit of list indexes
                nodeObjectSecond = nodeDict.get(path[0])
                continue
            locationSecond = (nodeObjectSecond.location).split(";")

            distance = (((int(locationFirst[0]) - int(locationSecond[0]))**2)
                        + ((int(locationFirst[1]) - int(locationSecond[1]))**2))**0.5
            cost = distance/int(nodeObjectFirst.residualBatteryLevel)
            costList.append(cost)
        minOfDistanceList.append((sum(costList), path, counter))
        counter += 1
    return minOfDistanceList


def printFuncOfSend(paths):

    print(f"NODES & THEIR NEIGHBORS:{neighborhoodDict}")
    print(f"{len(paths)} ROUTE(S) FOUND:")
    pathsWithCosts = costCalculator(paths)
    for path in pathsWithCosts:
        print(f"ROUTE {path[2]+1}: {path[1]} COST: {(path[0]):.4f}")
    selectedRoute = min(pathsWithCosts)
    print(f"SELECTED ROUTE (ROUTE {selectedRoute[2]+1}): {selectedRoute[1]}")


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
        global listof, node1constant, node2constant, timer, np, byte, packageSize, node1, node2
        node1 = commandDict.get("Name_1")
        node2 = commandDict.get("Name_2")
        node1constant = node1
        node2constant = node2
        paths = getPaths(node1, node2)
        byte = int(commandDict.get("BYTE"))
        packageSize = 15
        np = int(byte/packageSize)
        # for package in range(np):
        #     byte -= packageSize
        #     timer += 1
        #     print("simüle time",timer,byte)
        byte -= packageSize
        try:
            print(
                f"COMMAND *{commandDict['Command']}*: Data is ready to send from {commandDict['Name_1']} to {commandDict['Name_2']}")
            print(f"PACKET {timer+1} HAS BEEN SENT")
            print(f"REMAINING DATA SIZE: {byte} BYTE")
            printFuncOfSend(paths)
        except ValueError:
            print(
                f"NO ROUTE FROM {commandDict['Name_1']} TO {commandDict['Name_2']} FOUND.")
        return byte, packageSize, np

    def moveNode(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])
        # update the location of that node
        nodeObject.location = commandDict["Location"]
        print(
            f"COMMAND *{commandDict['Command']}*: The location of node {commandDict['Name']} is changed")
        getNeighborhood()
        paths = getPaths(node1, node2)
        printFuncOfSend(paths)

    def changeBattery(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])  # get the object
        # update the battery level of that node
        nodeObject.residualBatteryLevel = commandDict["ResidualBatteryLevel"]
        print(
            f"COMMAND *{commandDict['Command']}*: Battery level of node {commandDict['Name']} is changed to 90")
        getNeighborhood()
        paths = getPaths(node1, node2)
        printFuncOfSend(paths)

    def removeNode(commandDict):
        nodeObject = nodeDict.get(commandDict["Name"])  # removing
        del nodeDict[commandDict['Name']]  # delete the node from dict
        del nodeObject  # delete object
        getNeighborhood()  # for update the neighborhood of nodes because we have deleted one of them
        print(
            f"COMMAND *{commandDict['Command']}*: Node {commandDict['Name']} is removed")
        paths = getPaths(node1, node2)
        printFuncOfSend(paths)

    def intrudeNode(commandDict):
        global intrudedTime, intrudedNode
        intrudedTime = timer+2
        intrudedNode = commandDict["Name"]

        print(
            f"COMMAND *{commandDict['Command']}*: Node {commandDict['Name']} has become a malicious node")


intrudedTime = 1000000000
intrudedNode = None


def commandFunction(command):

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


print("""********************************
AD-HOC NETWORK SIMULATOR - BEGIN
********************************""")
print("SIMULATION TIME: 00:00:00")
countOfIntruded = 0
while True:

    if timer == 0:
        for command in splittedCommands:
            givenCommand = command[1]
            if int(command[0]) == 0:
                commandFunction(command)
        

    if byte > 0:
        if intrudedTime == timer:
            countOfIntruded += 1
            intrudedTime = timer+3
            timer += 1
            if countOfIntruded == 2:
                if len("0"+str(timer)) > 2:
                    print(f"SIMULATION TIME: 00:00:{timer}")
                else:
                    print(f"SIMULATION TIME: 00:00:0{timer}")
                print(f"""PACKET {timer+1} HAS BEEN DROPPED! 
REMAINING DATA SIZE: {byte} BYTE""")
                print(f"A POSSIBLE ROUTING ATTACK IS DETECTED! FINDING A NEW ROUTE EXCLUDING THE NODE {intrudedNode}")
                print(neighborhoodDict)
                routes = getPaths(node1,node2)
                for route in routes:
                    if intrudedNode in route:
                        routes.remove(route)
                routesWithCosts = costCalculator(routes)
                for route in routesWithCosts:
                    print(f"ROUTE {route[2]+1}: {route[1]} COST: {(route[0]):.4f}")
                selectedRoute = min(routesWithCosts)
                print(f"SELECTED ROUTE (ROUTE {selectedRoute[2]+1}): {selectedRoute[1]}")
            else:
                if len("0"+str(timer)) > 2:
                    print(f"SIMULATION TIME: 00:00:{timer}")
                else:
                    print(f"SIMULATION TIME: 00:00:0{timer}")
                print(f"""PACKET {timer+1} HAS BEEN DROPPED!
REMAINING DATA SIZE: {byte} BYTE""")
            timer -= 1

        else:
            byte -= packageSize
            timer += 1
            if len("0"+str(timer)) > 2:
                print(f"SIMULATION TIME: 00:00:{timer}")
            else:
                print(f"SIMULATION TIME: 00:00:0{timer}")

            if byte > 0:
                print(f"""PACKET {timer+1} HAS BEEN SENT
REMAINING DATA SIZE: {byte} BYTE""")
            else:
                print(f"""PACKET {timer+1} HAS BEEN SENT
REMAINING DATA SIZE: {0} BYTE""")

    else:
        break
    for command in splittedCommands:
        givenCommand = command[1]
        if int(command[0]) == timer:
            commandFunction(command)
print("""******************************
AD-HOC NETWORK SIMULATOR - END
******************************""")