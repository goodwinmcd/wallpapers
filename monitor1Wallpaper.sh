#/bin/bash
#Thiss script randomizes the right monitor while keeping the
#left monitor the same wallpaper

#Create an array of all files in my wallpaper directory
#and then get the array size
numFilesArray=(/home/goodwin/Media/Pictures/Wallpapers/*)
numFiles=${#numFilesArray[@]}

#Get a random number between 0 and the array size
export randomNum=$(shuf -i 0-${numFiles} -n 1)

#Declare wallpaper1 variable as the random numbered
#array element
export wallpaper1=${numFilesArray[${randomNum}]}

#wallpaper2 will be kept the same
export wallpaper2="$(awk '{print $2}' ~/.scripts/currentWallpapers.txt)"
feh --bg-scale ${wallpaper1} --bg-scale ${wallpaper2}

echo ${wallpaper1} ${wallpaper2} > ~/.scripts/currentWallpapers.txt
