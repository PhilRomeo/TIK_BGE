import bge

keyboard = bge.logic.keyboard
inputs = keyboard.inputs
number = 1

def Update():
    if inputs[bge.events.TKEY].values[-1]:
        global number
        number+= 1
        print(number)

def Walk():
    print("Walk")
    
def Run():
    print("Run")
    
def Stand():
    print("Stand")