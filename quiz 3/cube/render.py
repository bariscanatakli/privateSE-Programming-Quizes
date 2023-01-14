from termcolor import cprint
from states import *


def render(selectedFace):
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
        
    if selectedFace == "fullyuz":
        for square in range(0,3):
            print(end="      ")
            
            cprint(f"□",f"{ustyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{ustyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{ustyuz.get(square*3+3)}")
            
        
        for square in range(0,3):
            if square == 2:
                cprint(f"□",f"{solyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+3)}",end = " ")
                cprint(f"□",f"{onyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+3)}",end = " ")
                cprint(f"□",f"{sagyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+3)}",end = "\n")
            else:

                cprint(f"□",f"{solyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{solyuz.get(square*3+3)}", end = " "),
                cprint(f"□",f"{onyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{onyuz.get(square*3+3)}", end = " ") 
                cprint(f"□",f"{sagyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{sagyuz.get(square*3+3)}") 
        for square in range(0,3):
            print(end="      ")
            
            cprint(f"□",f"{altyuz.get(square*3+1)}",end =" "),cprint(f"□",f"{altyuz.get(square*3+2)}",end =" "),cprint(f"□",f"{altyuz.get(square*3+3)}")
        