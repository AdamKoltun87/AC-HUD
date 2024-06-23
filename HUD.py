#appName = "HUD"

import ac
import acsys

appWindow=0
speed=0
rpm=0

def acMain():
    global appWindow
    appWindow=ac.newApp("HUD")
    ac.setsize(appWindow,200,150)
    ac.drawBorder(appWindow,0)
    ac.setBackgroundOpacity(appWindow,0)
    ac.setBackgroundTexture(appWindow, "apps/python/hud/hudbg.png")
    speed = (appWindow,22,100,"km/h")
    rpm = (appWindow,22,100,"rpm")
    return "HUD"
