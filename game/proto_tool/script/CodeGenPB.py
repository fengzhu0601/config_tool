
from string import Template
import os
import codecs
import common as common
import fields_util as fields_util


class CodeGenPB(object):

    def __init__(self):
        pass
    
    def genPB(self, parser, templatePath, outputPath, tag):
        g = GenPB(parser, templatePath, outputPath, tag)
        return g.gen()
    
        
class GenPB(object):
    
    def __init__(self, parser, templatePath, outputPath, tag):
        self.parser = parser
        self.templatePath = templatePath
        self.outputPath = outputPath
        self.tag = tag
        
    def gen(self):
        self.genPB()
      
        
    def genPB(self):
        tpl = Template(common.read_file(self.templatePath + "/pb.tpl"))
        package_name = "pb_"+self.tag+"_"+self.parser.modName
        c = tpl.substitute(
            tag              = self.tag,
            package_name     = package_name,
            imports          = self.genImports(self.parser.imports),
            sturcts          = self.genStruct(self.parser.structs),
            requests         = self.genStruct(self.parser.requests,"Req"),
            responses        = self.genStruct(self.parser.responses,"Rep"),
            const_define     = self.genEnums(self.parser.consts),
            )

        subPath = self.outputPath
        if not os.path.exists(subPath):
            os.makedirs(subPath)
        common.write_file(subPath + "/pb_"+self.tag+"_"+self.parser.modName+".proto", c)


    # pt 生成imports
    def genImports(self,structList):
        codeStr = ''
        for struct in structList:
            ptName = "pb_"+self.tag+"_"+struct.name
            codeStr += "import "+ "\"" + ptName +".proto\";\n"
        return codeStr


    # pt 生成自定义常量
    def genEnums(self,constants):
        codeStr = ''
        for constant in constants:
            if constant.public:
                codeStr += self.genEnum(constant,1)
        return codeStr

    def genEnum(self,constant,TabNum):
        tmpStr = ''
        typeName = common.CamelCase(constant.name)

        firstField = constant.fields[0]
        if firstField.value != 0:
            tmpStr += common.gen_tab(TabNum) + "UNDEFINED" +" = 0; // 未定义"
        for field in constant.fields:
            if tmpStr != '':
                tmpStr += "\n"
            fieldName = common.CamelCase(field.name)
            tmpStr += common.gen_tab(TabNum) + fieldName +" = " + str(field.value) + "; // " + field.desc
        if tmpStr != '':
            tmpStr = common.gen_tab(TabNum-1)+"enum "+ typeName + "{\n"+ tmpStr +"\n"+common.gen_tab(TabNum-1)+"}\n"
            tmpStr = "\n"+common.gen_tab(TabNum-1)+"// "+ constant.desc + "\n"+ tmpStr
        return tmpStr

    # pt 生成结构体
    def genStruct(self,structList,prefixStr=""):
        template = Template(common.read_file(self.templatePath + "/message.tpl"))
        codeStr = ''
        for struct in structList:
            fieldsStr = ''
            index = 1
            enumStr = ''
            for field in struct.fields:
                if field.vtype in self.parser.constDict:
                    const = self.parser.constDict[field.vtype]
                    if const.public == False:
                        enumStr += self.genEnum(const,2)
                        self.parser.memberConstDict[field.vtype] = const
                fieldName = common.CamelCase(field.name)
                fieldType = common.to_pb_type(field.vtype, self.tag, field.imp, field.isarray)
                fieldStr = "\t" + fieldType + " " + fieldName + "= " + str(index) + "; // " + field.desc
                fieldsStr += "\n" + fieldStr
                index += 1
            structStr = template.substitute(desc=struct.desc,name=prefixStr+common.CamelCase(struct.name), fields=fieldsStr, enums = enumStr)
            codeStr += "\n\n" + structStr
        return codeStr
        
