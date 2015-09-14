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

# Title: load_options
# this uses the argparse module to parse the options

import argparse # the argument parsing module
import os;
#####################################################################
# function: load                                                   #
# load command line and config settings up                         #
#                                                                  # 
# Returns:                                                         # 
# args- dicitionary list of values.                                #
######################################################################
def load():
    """
    parse command line options
    compare old settings
    """
    Parser = argparse.ArgumentParser();
    Parser.add_argument("-o","--output",help="output directory",default="./docs");
    Parser.add_argument("-p","--project",help="project directory",default="./proj");
    Parser.add_argument("-i","--input",help=" pass input directory ",default="./src");
    args = Parser.parse_args();
    print args.input;
    print args.output;
    print args.project;
    if os.path.exists(args.input):
	print "input direcotory exits";
    if os.path.exists(args.input):
	print "output direcotry exists";
    if os.path.exists(args.input):
	print "project directory exist";
    return args;
