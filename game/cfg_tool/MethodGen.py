
from string import Template
import os
import codecs
import common as common


class MethodGen(object):

    def __init__(self):
        pass
    
    def gen(self, parser, templatePath, outputPath):
        g = gen(parser, templatePath, outputPath)
        return g.gen()
    
        
class gen(object):
    
    def __init__(self, parser, templatePath, outputPath):
        self.parser = parser
        self.templatePath = templatePath
        self.outputPath = outputPath
        
    def gen(self):
        tpl = Template(common.read_file(self.templatePath + "/methods.tpl"))
        package_name = self.parser["package_name"]
        c = tpl.substitute(
            package_name = package_name,
            methods      = self.genMethods(),
            imp          = self.getImport(),
            )

        subPath = self.outputPath + package_name
        if not os.path.exists(subPath):
            os.makedirs(subPath)
        common.write_file(subPath + "/"+package_name+"_m.go", c)


    def genMethods(self):
        tpl = Template(common.read_file(self.templatePath + "/method.tpl"))
        str = ""
        fields = self.parser["fields"]
        for field in fields:
            str += tpl.substitute(
                cfg_name = self.parser["cfg_name"],
                field = field["name"],
                type = field["type"],
            )+"\n"
        return str

    def getImport(self):
        fields = self.parser["fields"]
        for field in fields:
            type = field["type"]
            if type[0:3] =="cfg":
                return "import \"game/cfg\"\n"
        return ""
