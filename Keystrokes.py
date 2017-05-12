import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def PressAltTab():

    PressKey(0x012) #Alt
    PressKey(0x09) #Tab
    time.sleep(0.1) 
    ReleaseKey(0x09) #Tab
    ReleaseKey(0x012) #~Alt
    time.sleep(0.1)
    
    
def TypePassword():
	
	PressKey(0x43)
	ReleaseKey(0x43)
	PressKey(0x41)
	ReleaseKey(0x41)
	PressKey(0x52)
	ReleaseKey(0x52)
	PressKey(0x4F)
	ReleaseKey(0x4F)
	PressKey(0x4C)
	ReleaseKey(0x4C)
	PressKey(0x49)
	ReleaseKey(0x49)
	PressKey(0x4E)
	ReleaseKey(0x4E)
	PressKey(0x45)
	ReleaseKey(0x45)
	PressKey(0x0D)
	ReleaseKey(0x0D)


if __name__ =="__main__":

     PressAltTab()
     TypePassword()
