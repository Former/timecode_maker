# -*- coding: utf-8 -*-

# Copyright © 2020 Alexei Bezborodov. Contacts: <AlexeiBv+timecode_maker@narod.ru>
# License: Public domain: http://unlicense.org/

import sys

def TimeCode_Maker(in_file):
    f = open(in_file, 'r')
    lines = f.readlines()
    f.close()

    f = open(in_file+"_out.txt", 'wb') #, encoding='utf-8')
    cur_utl = ''
    for line in lines:
        if line[0:4] == 'http':
           cur_utl = line.strip()
           continue

        str_time = line[0: line.find(" ")]
        str_desc = line[line.find(" ") + 1:]

        times = str_time.split(":")

        if len(times) == 0 or len(times) == 1:
            f.write(line.encode('utf-8'))
            continue

        time = ''
        app_time = ['s', 'm', 'h']
        for i in range(min(len(times), len(app_time))):
            t = times[len(times) - i - 1]
            time = t + app_time[i] + time

        out = '# [[' + cur_utl + '&t=' + time + ' ' + str_time + ']] ' + str_desc
        f.write(out.encode('utf-8'))
    f.close()


files_to_decode = []
if __name__ == "__main__":
    for i in range(len(sys.argv)):
        param = sys.argv[i]
        if i > 0:
            files_to_decode.append(param)

for f in files_to_decode:
    TimeCode_Maker(f)
