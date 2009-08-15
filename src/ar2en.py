#!/usr/bin/env python
# coding: utf-8
# ar2en.py : Renames arabic files and directories into english recursively

import os
import sys

chart = { "أ" : "a" ,
          "ا" : "a" ,
          "آ" : "a" ,
          "إ" : "e" ,
          "ى" : "a" ,
          "ب" : "b" ,
          "ت" : "t" ,
          "ة" : "t" ,
          "ث" : "th" ,
          "ج" : "g" ,
          "ح" : "7" ,
          "خ" : "7'" ,
          "د" : "d" ,
          "ذ" : "th" ,
          "ر" : "r" ,
          "ز" : "z" ,
          "س" : "s" ,
          "ش" : "sh" ,
          "ص" : "s" ,
          "ض" : "d" ,
          "ط" : "t" ,
          "ظ" : "th" ,
          "ع" : "3" ,
          "غ" : "3'" ,
          "ف" : "f" ,
          "ق" : "k" ,
          "ك" : "k" ,
          "ل" : "l" ,
          "م" : "m" ,
          "ن" : "n" ,
          "ه" : "h" ,
          "و" : "w" ,
          "ي" : "y" ,
          " " : "_" ,
        }

def iterate( loc ):
    loc = os.path.abspath( loc )
    if os.path.exists( loc ):
        if os.path.isdir( loc ):
            entries = os.listdir( loc )
            for entry in entries:
                iterate( loc + os.path.sep + entry )
        rename( loc )
    else:
        print "Error : Encountered a non-existent path : " + loc
        return

def rename( item ):
#    print "From:\t" + item
    item_en = item
    for k in chart:
        item_en = item_en.replace( k , chart[k] )
    
    print "To:\t" + item_en.lower()

def usage():
    print "Usage:\n\tar2en.py <directory>|<file>"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loc = sys.argv[1]
        iterate( loc )
    else:
        usage()
        exit
