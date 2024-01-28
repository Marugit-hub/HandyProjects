
# Install pytube and other required packages
from pytube import YouTube
from sys import argv

# here argv[1] takes the second postional argument from the terminal , as the first argument would be the current file name.py 
# and then we pass the link as the second argument
link = argv[1]

# here we create YouTube object from the given link
yt = YouTube(link)

#  get video stream information (optional)
print("title : ",yt.title)
print("views : ",yt.views)

# downloading the highest resolution  available video stream 
yd = yt.streams.get_highest_resolution()

# defining the download location
yd.download('C:/Users/marut/Desktop')