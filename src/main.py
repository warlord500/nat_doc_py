#!/usr/bin/python
#copyright (c) 2015,jadon belezos 
#All rights reserved.

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


# Title: main.py
# this is the main file of exectuion




# import file # imaginary import modeling code directly after perl version
import project
import settings # imginary import of settings 
import os;
from languageDir import *; # import all language parsers.
import lang;
#import topics
#import builder
if __name__ == "__main__":  # start point of python interpeter.
  args = settings.load();
  #   languages.load();
  #   topics.load();
  #   project.loadConfigFileInfo();
  #   print 'starting normal_docs' 
  oldTimes  = project.getOldFileTimes(args);
  curTimes = project.getCurrentFileTimes(args);
  ParseList = project.cmpFileTimes(curTimes,oldTimes);
  project.updateModTimes(curTimes,args);
  print("now filtering the ParseList");
  project.filterParseList(ParseList);
  print ParseList;
  for sourceFile in ParseList:
      lang_parser = lang.langRegister().languageOf(sourceFile);
      lang_parser.ParseFile(sourceFile);
      
#   builder.build();
