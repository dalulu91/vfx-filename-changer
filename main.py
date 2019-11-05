import os
import sys

# Number of digits in your file type name (dpx is 3, tiff is 4, png is also 3, etc.)
# This wont work if you have filetypes with 3 and 4 digits together. But you shouldn't really have that in your shot anyway.
filetypeDigits = 3

# Specify frame digits. 4 should be enough unless you have a 7min (if 24fps) long shot
# If 24 fps and your shot is less than 41 seconds, 3 digits is enough.
frameDigits = 4

#Specify start frame count.
startFrame = 1

# Checking if there's any argument in the execute of the python file
if len(sys.argv) > 1:
    dir = sys.argv[1]
    element = sys.argv[2]
    shotcode = sys.argv[3]
    shotnumber = sys.argv[4]
    version = sys.argv[5]
# If there's no arguments, let the user type them in manually
else:
    dir = raw_input("Image sequence directory: ")
    print "[" + dir + "]"
    element = raw_input("i/o/e: ")
    print "[" + element + "]"
    shotcode = raw_input("Shot code: ")
    print "[" + element + "_" + shotcode + "]"
    shotnumber = raw_input("Shot number: ")
    print "[" + element + "_" + shotcode + "_" + shotnumber + "]"
    version = raw_input("Version number: ")
    print "[" + element + "_" + shotcode + "_" + shotnumber + "_" + version + "]"


frame = startFrame
filetypeDigits +=1

for filename in os.listdir(dir):

    src = dir + "/"+filename
    filetype = filename[-filetypeDigits:] #It would be safer to use regex here

    # If you wanna specify the filetype yourself, remove the hastag # in the line under:
    #filetype = ".dpx"
    dst = dir + "/" + element + "_" + shotcode + "_" + str(shotnumber) + "_v" + version + "_" + str(frame).zfill(frameDigits) + filetype

    # THIS IS SPARTA
    os.rename(src, dst)
    frame += 1

print "Renaming successful!"
print "[" + element + "_" + shotcode + "_" + shotnumber + "_" + version + "_####" + filetype + "]"
