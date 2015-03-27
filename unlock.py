# python for android test
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()
device.drag((360,914),(355,1176),1,10)