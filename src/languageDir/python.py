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
            if(isCommentLine(string)):
                sys.stdout.write(string);
                oncomment = True;
def isCommentLine(lineString):
    column = 0;
    char = lineString[column]
    while(char != "\n"):
        if(char.isalnum()):
            return False;
        if(char == "#"):
            return True;
        column += 1;
        char = lineString[column];
    return False; # handle blank lines as lines with code.


reg = lang.langRegister();
reg.register(".py",pythonParser());
print "did this get imported";
                #if(oncomment == True):
        #            stringList.append(string);
         #       else:
           #         nativeParser.generateTopic(stringList);
            #        stringList = [];
