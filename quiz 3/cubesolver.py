from termcolor import cprint



onyuz = {}
arkayuz = {}
ustyuz = {}
altyuz = {}
sagyuz = {}
solyuz = {}

lineStart = int()
lineEnd = int() 

for square in range(1,10):
    onyuz.update({square:"green"})
    arkayuz.update({square:"blue"})
    ustyuz.update({square:"white"})
    altyuz.update({square:"yellow"})
    sagyuz.update({square:"red"})
    solyuz.update({square:"magenta"})

#onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz
def update(square,a = onyuz,b = sagyuz,c = arkayuz,d = solyuz,e = altyuz,f = ustyuz):
    onyuz.update({square: a.get(square) })
    sagyuz.update({square: b.get(square) })
    arkayuz.update({square: c.get(square) })
    solyuz.update({square: d.get(square) })
    altyuz.update({square: e.get(square) })
    ustyuz.update({square: f.get(square) })

def getDirectionX(direction):
    if direction == "A":
        lineStart = 1
        line = 4
    elif direction == "B":
        lineStart=4
        line = 7
    elif direction == "C":
        lineStart = 7
        line = 10

    return lineStart, line
def getDirectionY(direction):
    if direction == "A":
        lineStart = 1
        line = 8
    elif direction == "B":
        lineStart=2
        line = 9
    elif direction == "C":
        lineStart = 3
        line = 10

    return lineStart, line

def copyFaces():
    onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = onyuz.copy(), sagyuz.copy(), arkayuz.copy(), solyuz.copy(), altyuz.copy(), ustyuz.copy()
    return onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy

class Rotates():
    class Rotate():
        def threeLineChangerRight():
            Rotates.Rotate.rotateRight("A")
            Rotates.Rotate.rotateRight("B")
            Rotates.Rotate.rotateRight("C")
        def threeLineChangerLeft():
            Rotates.Rotate.rotateLeft("A")
            Rotates.Rotate.rotateLeft("B")
            Rotates.Rotate.rotateLeft("C")
        class RotateCut():
            def rotateCutLeft(direction):
                Rotates.Rotate.threeLineChangerRight()
                Rotates.Rotate.rotateDown(direction)
                Rotates.Rotate.threeLineChangerLeft()
                
            def rotateCutRight(direction):
                Rotates.Rotate.threeLineChangerLeft()
                Rotates.Rotate.rotateDown(direction)
                Rotates.Rotate.threeLineChangerRight()

        def rotateUp(direction):
            lineStart, line = getDirectionY(direction)
            onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()
    
            for square in range(lineStart,line,3):
                square 
                update(square, altyuzCopy, sagyuzCopy, ustyuzCopy, solyuzCopy, arkayuzCopy, onyuzCopy)

        def rotateRight(direction):

            lineStart, line = getDirectionX(direction)

            onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()

            for square in range(lineStart,line):
                update(square, solyuzCopy, onyuzCopy, sagyuzCopy, arkayuzCopy, altyuzCopy, ustyuzCopy)
    #onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz



        def rotateDown(direction):
        
                lineStart, line = getDirectionY(direction)

                onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()

                for square in range(lineStart,line,3):
                
                    update(square, ustyuzCopy, sagyuzCopy, altyuzCopy, solyuzCopy, onyuzCopy, arkayuzCopy)
        #onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz

        def rotateLeft(direction):
    
            lineStart, line = getDirectionX(direction)

            onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()

            for square in range(lineStart,line):
                update(square, sagyuzCopy, arkayuzCopy, solyuzCopy, onyuzCopy, altyuzCopy, ustyuzCopy)
                #onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz



#onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz

selectedFace = "onyuz"
print("selectedFace is:",selectedFace)
if selectedFace == "onyuz":
    for square in range(0,3):    
        cprint(f"□",f"{onyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+3)}")

def selectFace():
    value = str(input("Type which face you want."))
    return value

def render():
    if selectedFace == "onyuz":
        for square in range(0,3):
            
            cprint(f"□",f"{onyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+3)}")
    if selectedFace == "arkayuz":
        for square in range(0,3):
            
            cprint(f"□",f"{arkayuz.get(square*3+1)}",end =" "),cprint(f"□",f"{arkayuz.get(square*3+2)}",end =" "),cprint(f"□",f"{arkayuz.get(square*3+3)}")
    if selectedFace == "sagyuz":
        for square in range(0,3):
            
            cprint(f"□",f"{sagyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+3)}")
    if selectedFace == "solyuz":
        for square in range(0,3):
            
            cprint(f"□",f"{solyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+3)}")
    if selectedFace == "altyuz":
        for square in range(0,3):
            
            cprint(f"□",f"{altyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{altyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{altyuz.get(square*3+3)}")
    if selectedFace == "ustyuz":
        for square in range(0,3):
            
            cprint(f"□",f"{ustyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{ustyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{ustyuz.get(square*3+3)}")
        


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
        Rotates.Rotate.RotateCut.rotateCutLeft("A")
    if commands == "cutLS":
        Rotates.Rotate.RotateCut.rotateCutLeft("B")
    if commands == "cutLT":
        Rotates.Rotate.RotateCut.rotateCutLeft("C")

    if commands =="cutRF":
        Rotates.Rotate.RotateCut.rotateCutRight("A")
    if commands =="cutRS":
        Rotates.Rotate.RotateCut.rotateCutRight("B")
    if commands =="cutRT":
        Rotates.Rotate.RotateCut.rotateCutRight("C")
    render()
    if commands == "exit":
        break

    


