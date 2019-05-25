#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
def longestPalSubstr(string): 
    maxLength = 1
    start = 0
    length = len(string) 
    low = 0
    high = 0
    for i in xrange(1, length): 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
    return string[start:start + maxLength]
    
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout
    # Edit and remove this code as you like.

    max = 0
    palString = []
    for i, v in enumerate(lines):
        palString.append(longestPalSubstr(v))
    #print(palString)
    index=0
    for j in range(0,len(palString)):
        if(max < len(palString[j])):
            max=len(palString[j])
            index=j
    print str(palString[j] )

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
