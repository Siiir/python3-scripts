print("YT downloader started.")
from os import system as s
s("clear")
from pytube import YouTube

v= YouTube(input("Provide yt video link for downloading to start: "))

# yt.set_filename("foo")
st= v.streams
sou=  st.filter(type= "audio")
cho=  sou[-1]

print(f"Downloading:\n\tTrack: {cho.mime_type}, {cho.abr}")
from os import getcwd, chdir
chdir("/storage/emulated/0/Download")
print(f"To:\n\t{getcwd()}")
cho.download()
print(f"Completed!")

# print(*st, sep= "\n", end= "\n\n\n")
# print(*sou, sep= "\n", end= "\n\n\n")
