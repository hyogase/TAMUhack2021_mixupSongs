from pydub import AudioSegment
from pydub.playback import play
import os,random  
disk=['E']    
def search_file(filename,search_path,pathsep=os.pathsep):  
    for path in search_path.split(pathsep):  
        candidate = os.path.join(path,filename)  
        if os.path.isfile(candidate):  
            return os.path.abspath(candidate)  
def random_play():  
    music=[]  
    found=False  
    for i in range(0,5):  
        for dirpath, dirnames, filenames in os.walk(disk[i]+':/new_tech/music'):  
            for filename in filenames:  
                if os.path.splitext(filename)[1] == '.mp3':  
                    filepath = os.path.join(dirpath, filename)  
                    if os.path.getsize(filepath)>1048576:#这里是为了防止打开一些非音乐音频，比如游戏配音  
                        music.append(filepath)  
                        found=True  
    if not found:  
        for dirpath, dirnames, filenames in os.walk('C:/Users'):  
            for filename in filenames:  
                if os.path.splitext(filename)[1] == '.mp3':  
                    filepath = os.path.join(dirpath, filename)  
                    if os.path.getsize(filepath)>1048576:  
                        music.append(filepath)  
                        found=True  
    if not found:  
        for i in range(0,5):  
            for dirpath, dirnames, filenames in os.walk(disk[i]+':/'):  
                for filename in filenames:  
                    if os.path.splitext(filename)[1] == '.wma':  
                        filepath = os.path.join(dirpath, filename)  
                        if os.path.getsize(filepath)>1048576:  
                            music.append(filepath)  
                            found=True  
    if not found:  
        for dirpath, dirnames, filenames in os.walk('C:/Users'):  
            for filename in filenames:  
                if os.path.splitext(filename)[1] == '.wma':  
                    filepath = os.path.join(dirpath, filename)  
                    if os.path.getsize(filepath)>1048576:  
                        music.append(filepath)  
                        found=True  
    random_music=random.choice(music)  
    os.startfile(random_music)  
    if not found:  
         
        return None
    return music
if __name__=='__main__':  
    songs=random_play()
    if len(songs) <= 0:
        print'No files found' 
    else:
        for s in songs:
            song = AudioSegment.from_wav(s)
            play(song)