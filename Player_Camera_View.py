import bge
from bge import render

debugMode = True

canLook = True

def mouse_view():
    if canLook == False:
        return
    
    cont = bge.logic.getCurrentController()
    owner = cont.owner
    mouse_sensor = cont.sensors["Always"] # Using Always sensor

    if not mouse_sensor.positive:
        return

    # Get the game window center coordinates
    width = render.getWindowWidth()
    height = render.getWindowHeight()
    center_x = width // 2
    center_y = height // 2

    # Get the current mouse position
    mouse_x, mouse_y = bge.logic.mouse.position
    # Mouse position from 0.0 to 1.0, convert to pixel values
    mouse_x *= width
    mouse_y *= height

    # Calculate the mouse movement offset from the center
    # The mouse movement is inverted for Y axis in Blender
    move_x = center_x - mouse_x
    move_y = center_y - mouse_y

    # Sensitivity (adjust as needed)
    sensitivity = 0.002

    # Apply rotation based on the object
    if owner.name == "Camera": # Replace "Camera" with your camera's object name
        # Pitch (up/down) rotation for the camera (local X-axis)
        owner.applyRotation([move_y * sensitivity, 0.0, 0.0], True)
    elif owner.name == "Player": # Replace "Player" with your player's object name
        # Yaw (left/right) rotation for the player (local Z-axis)
        owner.applyRotation([0.0, 0.0, move_x * sensitivity], True)

    # Recenter the mouse cursor
    render.setMousePosition(center_x, center_y)

    # Optional: ensure mouse is hidden
    # bge.render.showMouse(False) # Mouse is hidden by default in game mode
    
# Custom Debug function.    
def debug(text):
    if debugMode != True:
        return
    
    print(text)