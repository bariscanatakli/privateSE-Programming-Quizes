
commands = list(open("commands.txt").readlines())

nodeDict = dict()

timer = 0

neighborhoodDict = dict()

splittedCommands = []
for command in commands:
    newValue = command.split("\t")
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


listof = list()


def recursionFunc(node1, node2, addlist,counter):
    if counter >= 10:
        return "done"
    else:
        for neighboor1 in getPath(node1):
            # print(neighboor1)
            if neighboor1 == node2:
                addlist.append(((addlist[-1]+neighboor1)))
            else:
                counter += 1
                print(counter)
                recursionFunc(neighboor1, node2, addlist,counter)
                


def getPaths(node1, node2):
    addlist = [node1]
    counter = 0
    recursionFunc(node1, node2, addlist,counter)
    return addlist


def getPath(node):
    return neighborhoodDict.get(node)


def costCalculator(paths):
    minOfDistanceList = list()
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
                        - ((int(locationFirst[1]) - int(locationSecond[1]))**2)**0.5)
            cost = distance/int(nodeObjectFirst.residualBatteryLevel)
            costList.append(cost)
        minOfDistanceList.append((sum(costList), path))

    print(min(minOfDistanceList))


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
        global listof, node1constant, node2constant, timer
        node1 = commandDict.get("Name_1")
        node2 = commandDict.get("Name_2")
        node1constant = node1
        node2constant = node2
        paths = getPaths(node1, node2)
        print(paths)
        byte = int(commandDict.get("BYTE"))
        packageSize = 15
        np = int(byte/packageSize)
        try:
            print(
                f"COMMAND *{commandDict['Command']}*: Data is ready to send from {commandDict['Name_1']} to {commandDict['Name_2']}")

            costCalculator(paths)
        except ValueError:
            print(
                f"NO ROUTE FROM {commandDict['Name_1']} TO {commandDict['Name_2']} FOUND.")

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
    givenCommand = command[1]
    if int(command[0]) == timer:
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
