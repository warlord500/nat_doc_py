import  lang;
class pythonParser(lang.base):
    def ParseFile(self,filename):
	print "running python parser";

reg = lang.langRegister();
reg.register(".py",pythonParser());
print "did this get imported";
