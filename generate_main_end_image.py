# for android monkeyrunner use
# save subimage to ./image folder

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

# matrix of image
folder_path="c:\\eqiggun\\android_auto\\image\\"
main_activity_sub_tupe=(189,664,158,34)
end_activity_sub_tupe=(96,484,160,38)
main_activity_image_name="main_activity_image.png"
end_activity_image_name="end_activity_image.png"
main_activity_sub_image_name="main_activity_sub_image.png"
end_activity_sub_image_name="end_activity_sub_image.png"

device=MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(10.0)

main_activity_image=device.takeSnapshot()
main_activity_image.writeToFile(folder_path+main_activity_image_name,"png")
MonkeyRunner.sleep(10.0)

print("### Main activity saved! ###")
print("### Please change to end_activity_image now!!! ###")
MonkeyRunner.sleep(60.0)
print("10s left")
MonkeyRunner.sleep(10.0)

end_activity_image=device.takeSnapshot()
#end_activity_image.writeToFile(folder_path+end_activity_image_name,"png")
MonkeyRunner.sleep(10.0)

main_activity_sub_image=main_activity_image.getSubImage(main_activity_sub_tupe)
main_activity_sub_image.writeToFile(folder_path+main_activity_sub_image_name,"png")
MonkeyRunner.sleep(2.0)
end_activity_sub_image=end_activity_image.getSubImage(end_activity_sub_tupe)
#end_activity_sub_image.writeToFile(folder_path+end_activity_sub_image_name,"png")
MonkeyRunner.sleep(2.0)

print("### Thanks god, finish!! ###")




