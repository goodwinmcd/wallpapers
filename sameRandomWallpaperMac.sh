#/bin/bash

#Create an array of all files in my wallpaper directory
#and then get the array size

numFilesArray=(/Users/gradymcdonald/Pictures/wallpapers/Wallpapers/*)
numFiles=${#numFilesArray[@]}

#Get a random number between 0 and the array size

export randomNum=$(( ( RANDOM % ${numFiles} )  + 1 ))
# export randomNum=$(shuf -i 0-${numFiles} -n 1)

#Declare wallpaper variables as the random numbered
#array element

export wallpaper1=${numFilesArray[${randomNum}]}
export wallpaper2=${numFilesArray[${randomNum}]}

#Set the wallpapers
# feh --bg-scale ${wallpaper1} --bg-scale ${wallpaper2}
echo ${wallpaper1}
export command='tell application "System Events" to tell every desktop to set picture to '\"$wallpaper1\"
echo $command
osascript -e 'tell application "System Events" to tell every desktop to set picture to '\"${wallpaper1}\"