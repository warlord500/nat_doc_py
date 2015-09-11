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


# Title: project.py
# this handles of the project stuff.
fileNameMod = "filetimes.json"
########################################
# function: files_to_parse
# 
# Params: None
#
# Return: 
#    dictiornay type object.
#    key - filename 
#    value - modification time
#############################################
import json;
import os.path;
import os;
def getOldFileTimes(args):
    filename = os.path.join(args.project,fileNameMod);
    if(os.path.exists(filename)):
	try:
	    fileObject = open(filename,"r");
	    fileTimes = json.load(fileObject);
	    fileObject.close();
	except ValueError:
	    fileTimes ={}
	    print "filetimes.json has become invalid please delete it.";
	    exit();
	if(isinstance(fileTimes,dict)):
	    for key ,value in fileTimes.items():
	       print "File:",key,"lastUpdated:",value;
	else:
	    fileTimes = {};
	return fileTimes;
    return {};

##############################################
# function: getFilesToCheck()
# purpose build dict of the newest file times.
#
# Depencies: 
#  os  module
#  json module
##########################################
def getCurrentFileTimes(args):
    fileTimes = {};
    listing = os.listdir(args.input);
    for infile in listing:
	infile =  os.path.abspath(os.path.join(args.input,infile));
	fileTimes[infile] = os.path.getmtime(infile);
    return fileTimes;


def cmpFileTimes(curTimes,oldTimes):
    ParseList = [];
    for infile in curTimes.items():
	if (oldTimes.has_key(infile)):
	    if(oldTimes[infile] != curTimes[infile]):
		ParseList.append(infile);
	else:
	    ParseList.append(infile);
    return ParseList;


def updateModTimes(curTimes,args):
    for infile in curTimes:
	curTimes[infile] = os.path.getmtime(infile);
    fileObject = open(os.path.join(args.project,fileNameMod),"w+");
    json.dump(curTimes,fileObject);
    fileObject.close();
