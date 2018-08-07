#!/usr/bin/python3

# usage: python3 list_emojis.py > output.txt

import codecs
from urllib.request import urlopen

if __name__ == '__main__':
    f = urlopen('https://unicode.org/Public/emoji/11.0/emoji-data.txt')

    for line in f:
        parts = line.decode().split()
        if len(parts) > 2 and not parts[0].startswith('#'):
            points = parts[0]
            property = parts[2]
            if property not in ('Emoji_Presentation', 'Emoji_Modifier_Base', 'Extended_Pictographic#'):
                continue
            if '..' in points:
                from_, to_ = points.split('..')
                from_int = int(from_, 16)
                to_int = int(to_, 16)
                for i in range(from_int, to_int + 1):
                    print(hex(i) + ',')
            else:
                print('0x' + points + ',')
