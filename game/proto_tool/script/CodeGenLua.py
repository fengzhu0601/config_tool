from string import Template
import os
import codecs
import common as common
import fields_util as fields_util


class CodeGenLua(object):

    def __init__(self):
        pass

    def genLua(self, parser, prefix):
        g = GenLua(parser, prefix)
        return g.gen()


class GenLua(object):

    def __init__(self, parser, prefix):
        self.parser = parser
        self.pb_prefix = prefix
        self.pbName = "{0}{1}.pb".format(self.pb_prefix, self.parser.modName)
        self.modNameCamel = common.CamelCase(self.parser.modName)

    def genStruct(self, structList, prefixStr=""):
        codeDes = []
        codeCmd = []  # pb_ReqID = \n{\n\t
        if len(structList) > 0:

            # codeCmd.append("--[[\n\t\t{0}\n\t]]".format(modNameCamel))
            for struct in structList:
                cmd = struct.cmd
                name = struct.name
                nameCamel = "{0}{1}".format(prefixStr, common.CamelCase(name))
                CmdDes = {
                    "cmd": int(cmd) or 0,
                    "des": "--{0}\n\t{1}_{2} = {3},".format(struct.desc, self.modNameCamel, nameCamel, cmd),
                }
                codeCmd.append(CmdDes)

                message = "{0}{1}.{2}".format(self.pb_prefix, self.parser.modName, nameCamel)
                codeDes.append("[{0}] = {{message='{1}',pb='{2}'}},".format(cmd, message, self.pbName))
        # print(codeDes)
        # print(codeCmd)
        return codeDes, codeCmd

    def genEnums(self, constants):
        codeEnumList = []
        for constant in constants:
            if constant.public:
                typeName = common.CamelCase(constant.name)
                codeEnum = "--{0}\npb_{1}_E{2} = \n{{\n".format(constant.desc, self.modNameCamel, typeName)
                for field in constant.fields:
                    fieldName = common.CamelCase(field.name)
                    codeEnum += "\t{0} = {1},--{2}\n".format(fieldName, field.value, field.desc)
                codeEnum += "}\n"
                codeEnumList.append(codeEnum)

        return codeEnumList

    def gen(self):
        codeReqDes, codeReqCmd = self.genStruct(self.parser.requests, "Req")
        codeResDes, codeResCmd = self.genStruct(self.parser.responses, "Rep")
        codeEnumList = self.genEnums(self.parser.consts)
        return codeReqDes, codeReqCmd, codeResDes, codeResCmd, self.pbName, codeEnumList

        # for field in struct.fields:
        #     fieldName = common.CamelCase(field.name)
        #     fieldType = common.to_pb_type(field.vtype, field.imp, field.isarray)
        #     fieldStr = "\t" + fieldType + " " + fieldName + "= " + str(index) + "; // " + field.desc
        #     fieldsStr += "\n" + fieldStr
        #     index += 1

    # def GenLua(self):
    #     tpl = Template(common.read_file(self.templatePath + "/pb.tpl"))
    #     package_name = "pb_"+self.tag+"_"+self.parser.modName
    #     c = tpl.substitute(
    #         package_name     = package_name,
    #         imports          = self.genImports(self.parser.imports),
    #         sturcts          = self.genStruct(self.parser.structs),
    #         requests         = self.genStruct(self.parser.requests,"Req"),
    #         responses        = self.genStruct(self.parser.responses,"Rep"),
    #         const_define     = self.genEnums(self.parser.consts),
    #         )
    #
    #     subPath = self.outputPath
    #     if not os.path.exists(subPath):
    #         os.makedirs(subPath)
    #     common.write_file(subPath + "/pb_"+self.tag+"_"+self.parser.modName+".proto", c)
    #
    #
    # # pt 生成imports
    # def genImports(self,structList):
    #     codeStr = ''
    #     for struct in structList:
    #         ptName = "pb_"+struct.name
    #         codeStr += "import "+ "\"pb/"+self.tag+"/" + ptName +"\";\n"
    #     return codeStr
    #
    #
    # # pt 生成自定义常量
    # def genEnums(self,constants):
    #     codeStr = ''
    #     for constant in constants:
    #         if constant.public:
    #             codeStr += self.genEnum(constant,1)
    #     return codeStr
    #
    # def genEnum(self,constant,TabNum):
    #     tmpStr = ''
    #     typeName = common.CamelCase(constant.name)
    #
    #     firstField = constant.fields[0]
    #     if firstField.value != 0:
    #         tmpStr += common.gen_tab(TabNum) + "UNDEFINED" +" = 0; // 未定义"
    #     for field in constant.fields:
    #         if tmpStr != '':
    #             tmpStr += "\n"
    #         fieldName = common.CamelCase(field.name)
    #         tmpStr += common.gen_tab(TabNum) + fieldName +" = " + str(field.value) + "; // " + field.desc
    #     if tmpStr != '':
    #         tmpStr = common.gen_tab(TabNum-1)+"enum "+ typeName + "{\n"+ tmpStr +"\n"+common.gen_tab(TabNum-1)+"}\n"
    #         tmpStr = "\n"+common.gen_tab(TabNum-1)+"// "+ constant.desc + "\n"+ tmpStr
    #     return tmpStr
    #
    # pt 生成结构体
    # def genStruct(self, structList, prefixStr=""):
    #     template = Template(common.read_file(self.templatePath + "/message.tpl"))
    #     codeStr = ''
    #     for struct in structList:
    #         fieldsStr = ''
    #         index = 1
    #         enumStr = ''
    #         for field in struct.fields:
    #             if field.vtype in self.parser.constDict:
    #                 const = self.parser.constDict[field.vtype]
    #                 if const.public == False:
    #                     enumStr += self.genEnum(const, 2)
    #                     self.parser.memberConstDict[field.vtype] = const
    #             fieldName = common.CamelCase(field.name)
    #             fieldType = common.to_pb_type(field.vtype, field.imp, field.isarray)
    #             fieldStr = "\t" + fieldType + " " + fieldName + "= " + str(index) + "; // " + field.desc
    #             fieldsStr += "\n" + fieldStr
    #             index += 1
    #         structStr = template.substitute(desc=struct.desc, name=prefixStr + common.CamelCase(struct.name),
    #                                         fields=fieldsStr, enums=enumStr)
    #         codeStr += "\n\n" + structStr
    #     return codeStr
