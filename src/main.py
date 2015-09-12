#!/usr/bin/python
#copyright (c) 2015,jadon belezos 
#All rights reserved.

#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

#2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation 
#and/or other materials provided with the distribution.

#3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software 
#without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
#LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
#GOODS 
#OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
#LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH 
#DAMAGE.

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
  project.filterParseList(ParseList);
  print ParseList;
  for sourceFile in ParseList:
      lang_parser = lang.langRegister().languageOf(sourceFile);
      
#   builder.build();
