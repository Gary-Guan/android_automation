# python for android test
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()


device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)