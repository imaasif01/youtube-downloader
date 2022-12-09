from pytube import YouTube
from sys import argv

link = argv[1]
youtube = YouTube(link)

print("Title: ", youtube.title)
print("View: ", youtube.views)
print("description: ", youtube.description)
print("Author: ", youtube._author)
print("captions: ", youtube.captions)
print("Publish-Date: ", youtube._publish_date)
print("keywords: ", youtube.keywords)

Download_Yt = youtube.streams.get_highest_resolution()
Download_Yt.download(r"PATH_NAME_FOLDER")