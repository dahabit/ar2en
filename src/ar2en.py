#!/usr/bin/env python
# coding: utf-8
# ar2en.py : Renames arabic files and directories into english recursively

import os
import sys
import shutil

chart = { "أ" : "a" ,
          "ا" : "a" ,
          "آ" : "a" ,
          "ء" : "2" ,
          "ئ" : "2" ,
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
          "ؤ" : "o2" ,
          "ي" : "y" ,
          " " : "_" ,
        }

def iterate( loc ):
    print "Checking : " + loc
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
    toren_en = item.split( '/' )[-1]

    for k in chart:
        toren_en = toren_en.replace( k , chart[k] )

    toren_en = "/".join( item.split( '/' )[0:-1] ) + os.path.sep + toren_en.lower()
    
    print "Renaming : " + item + " to " + toren_en
    os.rename( item , toren_en )

def usage():
    print "Usage:\n\tar2en.py <directory>|<file>"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loc = sys.argv[1]
        iterate( os.path.abspath( loc ) )
    else:
        usage()
        exit
