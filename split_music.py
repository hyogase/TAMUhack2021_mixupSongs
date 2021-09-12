from pydub import AudioSegment
from pydub.silence import split_on_silence
 
sound = AudioSegment.from_mp3(r"..\02 Beauty and the Beast.mp3")
AudioSegment.ffmpeg = r"D:\ProgramData\Anaconda2\Lib\site-packages\ffmpeg\bin"
#AudioSegment.converter = r"D:\ProgramData\Anaconda2\Lib\site-packages\ffmpeg\bin\ffmpeg.exe"
#AudioSegment.ffmpeg = r"D:\ProgramData\Anaconda2\Lib\site-packages\ffmpeg\bin\ffmpeg.exe"
#AudioSegment.ffprobe =r"D:\ProgramData\Anaconda2\Lib\site-packages\ffmpeg\bin\ffprobe.exe"
loudness = sound.dBFS
#print(loudness)
 
chunks = split_on_silence(sound,
    # must be silent for at least half a second,
    min_silence_len=430,
 
    # consider it silent if quieter than -16 dBFS
    silence_thresh=-45,
    keep_silence=400
 
)
print('len(chunks):', len(chunks))
 
# 
for i in list(range(len(chunks)))[::-1]:
    if len(chunks[i]) <= 2000 or len(chunks[i]) >= 10000:
        chunks.pop(i)
print('chunck>2s < 10s:', len(chunks))
 
'''
for x in range(0,int(len(sound)/1000)):
    print(x,sound[x*1000:(x+1)*1000].max_dBFS)
'''
 
for i, chunk in enumerate(chunks):
    chunk.export(r"cutFilter300\chunk{0}.mp3".format(i), format="mp3")
    #print(i)