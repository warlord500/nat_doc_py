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
