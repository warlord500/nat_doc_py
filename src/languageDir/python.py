import  ../lang;
class pythonParser(base):
    def ParseFile():
	print "running python parser";

reg = langRegister();
reg.register(".py",PythonParser());
print "did this get imported";
