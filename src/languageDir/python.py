import  lang;
import sys;
import nativeParser;
class pythonParser(lang.base):
    def ParseFile(self,filename):
	print "running python parser";
	stringList =[];
	fileObj = open(filename,"r");
	fileLines = fileObj.readlines(); # generate the list of lines in file.
        oncomment = False; # are we currently parsing a topic.
	for string in fileLines: #
	    string = isCommentLine(string);
            if(string != ""):
                sys.stdout.write(string);
		stringList.append(string);


def isCommentLine(lineString):
    column = 0;
    char = lineString[column]
    while(char != "\n"):
        if(char.isalnum()):
            return "";
        if(char == "#"):
	    return lineString[column+1:];
        column += 1;
        char = lineString[column];
    return ""; # handle blank lines as lines with code.


reg = lang.langRegister();
reg.register(".py",pythonParser());
print "did this get imported";
                #if(oncomment == True):
        #            stringList.append(string);
         #       else:
           #         nativeParser.generateTopic(stringList);
            #        stringList = [];
