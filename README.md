# nat_doc_py
a new general purporse documentation generation tool.
designed to be easily extendable for new programming languages and 
written in entirely python.
design to clone in NaturalDocs using less lines of code.
and simpler parsing systen for easy extension of building 
a parser for new programming languages.

this program is heavily inspired the existing Natural_Docs project
<http://www.naturaldocs.org/>

##how to install and use quick start.
--git repo
copy git repo into directory of your choice.
set path or alias for the src/main.py file
run main.py with the command line arguments for project
example commands  for building docs for nat_doc_py project
```
~/Desktop $ git clone https://github.com/warlord500/nat_doc_py.git --depth=1
~/Desktop $ cd nat_doc_py
~/Desktop/nat_doc_py $ src/main.py 
building docs
parsing files (list of files below)
main.py
lang.py
```
o 
### command line options
--source where to get the files for the project
--output where to put the documentation files.
--project where project specific data is stored.


