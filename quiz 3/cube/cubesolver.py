from termcolor import cprint
from rotates import *
from states import *
from update import *
from render import render

selectedFace = "fullyuz"
print("selectedFace is:",selectedFace)
render(selectedFace)

def selectFace():
    value = str(input("Type which face you want."))
    return value

while True:
    commands = str(input("command:"))
    print("selectedFace is:",selectedFace)
    
    if commands == "selectFace":
        selectedFace = selectFace()    
    if commands == "RF":
        Rotates.Rotate.rotateRight("A")
    if commands == "RS":
        Rotates.Rotate.rotateRight("B")
    if commands == "RT":
        Rotates.Rotate.rotateRight("C")

    if commands == "LF":
        Rotates.Rotate.rotateLeft("A")
    if commands == "LS":
        Rotates.Rotate.rotateLeft("B")
    if commands == "LT":
        Rotates.Rotate.rotateLeft("C")

    if commands == "UF":
        Rotates.Rotate.rotateUp("A")
    if commands == "US":
        Rotates.Rotate.rotateUp("B")
    if commands == "UT":
        Rotates.Rotate.rotateUp("C")

    if commands == "DF":
        Rotates.Rotate.rotateDown("A")
    if commands == "DS":
        Rotates.Rotate.rotateDown("B")
    if commands == "DT":
        Rotates.Rotate.rotateDown("C")

    if commands == "cutLF":
        Rotates.Rotate.RotateCut.rotateCutLeft("C")
    if commands == "cutLS":
        Rotates.Rotate.RotateCut.rotateCutLeft("B")
    if commands == "cutLT":
        Rotates.Rotate.RotateCut.rotateCutLeft("A")

    if commands =="cutRF":
        Rotates.Rotate.RotateCut.rotateCutRight("A")
    if commands =="cutRS":
        Rotates.Rotate.RotateCut.rotateCutRight("B")
    if commands =="cutRT":
        Rotates.Rotate.RotateCut.rotateCutRight("C")

    if commands == "getUnsolvedCube":
        print("olcak dersten sonra")
    render(selectedFace)
    if commands == "exit":
        break

    


