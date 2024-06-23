#assetto corsa hud drift specific
#rpms, gear, speed, tyre wear?, fuel

#appName = "HUD"

import ac
import acsys
from third_party.sim_info import *

appName = "Car HUD"
width, height = 200, 100 # Adjust the size to your needs

simInfo = SimInfo()

def acMain(ac_version):
    global appWindow, speedLabel, rpmLabel

    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)

    # Create labels for speed and RPM
    speedLabel = ac.addLabel(appWindow, "Speed: 0 km/h")
    rpmLabel = ac.addLabel(appWindow, "RPM: 0")

    # Position the labels in the app window
    ac.setPosition(speedLabel, 10, 30)
    ac.setPosition(rpmLabel, 10, 60)

    # Register the update function
    ac.addRenderCallback(appWindow, appGL)

    return appName

def appGL(deltaT):
    # Update the display with the latest data
    speed = simInfo.physics.speedKmh
    rpm = simInfo.physics.rpms

    ac.setText(speedLabel, f"Speed: {speed:.1f} km/h")
    ac.setText(rpmLabel, f"RPM: {rpm:.0f}")

def acUpdate(deltaT):
    # This can be used for non-OpenGL updates if necessary
    pass

