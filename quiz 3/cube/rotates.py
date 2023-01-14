
from update import *
from copyFunction import copyFaces


def getDirectionX(direction):
    if direction == "A":
        lineStart = 1
        line = 4
    elif direction == "B":
        lineStart = 4
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
        lineStart = 2
        line = 9
    elif direction == "C":
        lineStart = 3
        line = 10

    return lineStart, line


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

            if direction == "B":
                for square in range(lineStart, line, 3):
                    square
                    update(square, altyuzCopy, sagyuzCopy, ustyuzCopy,
                           solyuzCopy, arkayuzCopy, onyuzCopy)

        def rotateRight(direction):

            lineStart, line = getDirectionX(direction)


            onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()
            
                    

            for square in range(lineStart, line):
                update(square, solyuzCopy, onyuzCopy, sagyuzCopy,
                       arkayuzCopy, altyuzCopy, ustyuzCopy)
    # onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz



        def rotateDown(direction):
        
                lineStart, line = getDirectionY(direction)

                onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()

                for square in range(lineStart,line,3):
                
                    update(square, ustyuzCopy, sagyuzCopy, altyuzCopy, solyuzCopy, onyuzCopy, arkayuzCopy)
        # onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz

        def rotateLeft(direction):
    
            lineStart, line = getDirectionX(direction)

            onyuzCopy, sagyuzCopy, arkayuzCopy, solyuzCopy, altyuzCopy, ustyuzCopy = copyFaces()

            for square in range(lineStart,line):
                update(square, sagyuzCopy, arkayuzCopy, solyuzCopy, onyuzCopy, altyuzCopy, ustyuzCopy)
                # onyuz, sagyuz, arkayuz, solyuzi altyuz, ustyuz
