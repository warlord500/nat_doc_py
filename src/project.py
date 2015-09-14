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
	#if(isinstance(fileTimes,dict)):
	    #for key ,value in fileTimes.items():
		#print "File:",key,"lastUpdated:",value;
	#else:
	   # fileTimes = {};
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
    for infile in curTimes:
	if (oldTimes.has_key(infile)):
	    if(oldTimes[infile] != curTimes[infile]):
		ParseList.append(infile);
	else:
	    ParseList.append(infile);
    return ParseList;
############################3
# function: UpdateModTimes
# take an existing dict of file to mod times 
# loop through each file and update all of the mod times
# after open file for dumping dict as json data
# 
# Params:
#  existing dict of file to modtimes
#
# returns: none 
################################################
def updateModTimes(curTimes,args):
    for infile in curTimes:
	curTimes[infile] = os.path.getmtime(infile);
    fileObject = open(os.path.join(args.project,fileNameMod),"w+");
    json.dump(curTimes,fileObject);
    fileObject.close();

def filterParseList(ParseList):
    ext = "";
    for file in ParseList:
	ext = os.path.splitext(file)[1]
	print ext,"\n";
	if(ext != ".py"):
	    ParseList.remove(file);
