import pytube
"""Make sure that you turn on the data and copy your desired youtube link"""
url = input("Enter your YouTube url: ")
video = pytube.YouTube(url)
youtube = video.streams.last()
youtube.download(r'C:\Users\Shalet\Downloads')  """Your Location Path directory"""
print("Downloaded Successfully....")
