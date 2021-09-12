import vlc
dirname=r"C:\\Users\\lvkai\\Downloads\\music"
song = vlc.MediaPlayer('{0}\\01 When You Wish Upon a Star.mp3'.format(dirname))
song.play()
song.set_time(10000) 
#song.set_position(0.5)