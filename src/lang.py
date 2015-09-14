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

# title: langauge module
import os.path;
# class: base 
#   the langauge base class which is used when parsing file.
class base:
    def ParseFiles(self):
	pass;
    def ParsePrototype(self):
	pass;
    def typeBeforeParamter(self):
       pass;


class langRegister():
    LanguageDict = {};
    def register(self,fileExt,function):
	self.LanguageDict[fileExt] = function;

#################################################33
# function: languageof
#  figure out the langauge of a file.
#
# params:
#   filename - the file that need the language to be figured out.
#   
#   ".py": pythonParser
    def languageOf(self,filename):
	return self.LanguageDict[os.path.splitext(filename)[1]];
