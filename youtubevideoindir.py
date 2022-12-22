from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("bi hata var")
    print("Indirme islemi tamamlandi")


link = input("video URL gir: ")
Download(link)
