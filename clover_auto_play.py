# python for game test
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

# VARIABLE DEFINATION
package = 'com.tencent.clover'
mainActivity='/.Clover'
runComponent=package+mainActivity
inGame=False

# botton location
notice_loc=(258,684,"DOWN_AND_UP")
endless_loc=(150,838,"DOWN_AND_UP")
world_loc=(332,830,"DOWN_AND_UP")
match1_loc=(270,336,"DOWN_AND_UP")
launch_loc=(270,836,"DOWN_AND_UP")
match_loc=(270,836,"DOWN_AND_UP")
end_loc=(170,500,"DOWN_AND_UP")
getItem_loc=(268,648,"DOWN_AND_UP")
continue_loc=(155,796,"DOWN_AND_UP")
back_loc=(491,848,"DOWN_AND_UP")

# matrix of image
folder_path="c:\\eqiggun\\android_auto\\image\\"
main_activity_sub_tupe=(189,664,158,34)
end_activity_sub_tupe=(96,484,160,38)
main_activity_sub_image_name="main_activity_sub_image.png"
end_activity_sub_image_name="end_activity_sub_image.png"
main_activity_sub_image=MonkeyRunner.loadImageFromFile(folder_path+main_activity_sub_image_name)
end_activity_sub_image=MonkeyRunner.loadImageFromFile(folder_path+end_activity_sub_image_name)

def playEndlessMode():
	# Launch Endless World Match
	print("Launch Endless")
	MonkeyRunner.sleep(5.0)
	device.touch(125,838,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(332,830,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(270,336,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(270,836,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(270,836,"DOWN_AND_UP")

	# Waiting while playing
	print("Game is going, sleeping 300s")
	MonkeyRunner.sleep(200.0)

	# Check if end
	print("300s pass, check if end or not")
	isEnd=False

	while isEnd is not True:
		device.takeSnapshot()
		current_image=device.takeSnapshot()
		current_sub_image=current_image.getSubImage(end_activity_sub_tupe)
		isEnd=current_sub_image.sameAs(end_activity_sub_image,0.8)
		MonkeyRunner.sleep(10.0)
		print("Still playing, sleep 10s more ......")
		
	print("Game is end!!")
	device.touch(170,500,"DOWN_AND_UP")
	MonkeyRunner.sleep(10.0)
	device.touch(268,648,"DOWN_AND_UP")
	MonkeyRunner.sleep(10.0)
	device.touch(155,796,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(491,848,"DOWN_AND_UP")

	print("------>THANKS FOR PLAYING!!!")
	
# Runs the component
def launchGame():
	device.startActivity(component=runComponent)
	print("Starting game, please wait 120s...")
	MonkeyRunner.sleep(20.0)

	# Check if enter to main activity, once
	isEnterGame=False

	while isEnterGame is not True:
		main_image=device.takeSnapshot()
		button_image=main_image.getSubImage(main_activity_sub_tupe)
		isEnterGame=button_image.sameAs(main_activity_sub_image,0.8)
		print("Sleep 5s more...")
		MonkeyRunner.sleep(5.0)
		
	print("Enter main acitivity to the game")

	# kickout 3 notice
	device.touch(258,684,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(258,684,"DOWN_AND_UP")
	MonkeyRunner.sleep(5.0)
	device.touch(258,684,"DOWN_AND_UP")
	inGame=True


device=MonkeyRunner.waitForConnection()
# Start Game
if inGame is not True:
	launchGame()
else:
	print("Already in game, just start endless mode.")
# Play Endless Mode
playEndlessMode()





