#!/user/bin/env python
# _*_coding:utf-8_*_
from pydub import AudioSegment
import re


with open(r"..\lyric\02 Beauty and the Beast.txt",'r',encoding='utf-8') as f: 
    time_list = []
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip('\n')
        p = '(?<=\[)[^]]+'
        b = re.findall(p,line)
        time_list.append(b[0])

print(time_list)
cout =0
for i in range(len(time_list)):
    cout += 1
    start_time = time_list[i] 

    print(start_time)
    if i < len(time_list)-1:

        stop_time = time_list[i+1]
        print(stop_time)


        file_name = "..\02 Beauty and the Beast.mp3" 
        sound = AudioSegment.from_mp3(file_name)

        print("time:", start_time, "~", stop_time)
        start_time = (float(start_time.split(':')[0]) * 60 + float(start_time.split(':')[1])) * 1000 + float(
            '0.{}'.format(start_time.split('.')[-1])) * 100 

        stop_time = (float(stop_time.split(':')[0]) * 60 + float(stop_time.split(':')[1])) * 1000 + float(
            '0.{}'.format(stop_time.split('.')[-1])) * 100 

        print("ms:", start_time, "~", stop_time)

        word = sound[start_time:stop_time]

        word.export('{}.mp3'.format(cout), format="mp3", 
                    tags={'artist': 'AppLeU0', 'album': cout})
