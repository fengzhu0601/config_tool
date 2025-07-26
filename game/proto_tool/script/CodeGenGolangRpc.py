
from string import Template
import os
import codecs
import common as common
import fields_util as fields_util


class CodeGenGolangRpc(object):

    def __init__(self):
        pass
    
    def genServerGolangRpc(self, parser, templatePath, outputPath, tag):
        g = GenServerGolangRpc(parser, templatePath, outputPath, tag)
        return g.gen()
    
        
class GenServerGolangRpc(object):
    
    def __init__(self, parser, templatePath, outputPath,tag):
        self.parser = parser
        self.templatePath = templatePath
        self.outputPath = outputPath
        self.tag = tag
        
    def gen(self):
        self.genPt()    
        
    def genPt(self):
        tpl = Template(common.read_file(self.templatePath + "/pt_.go.tpl"))
        if self.parser.modName == "error":
            tpl = Template(common.read_file(self.templatePath + "/pt_error.go.tpl"))
        package_name = "rpc_"+self.parser.modName
        pb_name = "pb_"+self.tag+"_"+self.parser.modName
        handler_name = "I"+ common.CamelCase(self.parser.modName) +"Handler"
        c = tpl.substitute(
            package_name     = package_name,
            player_import    = self.genPlayerImport(self.parser.requests),
            router_import     = self.genRouterImport(self.parser.requests),

            tag              = self.tag,
            pb_name          = pb_name,
            handler_name     = handler_name,
            interface        = self.genInterface(self.parser.requests,handler_name),
            handler_fun      = self.genHandlerFuns(self.parser.requests,pb_name),

            requests         = self.genRequestFuns(self.parser.requests,pb_name),

            const_proto_recv = self.genPtConst(self.parser.requests,"RpcCS",self.parser.modName),
            const_proto_send = self.genPtConst(self.parser.responses,"RpcSC",self.parser.modName),
            regHandler       = self.genRegistFuns(self.parser.requests),
            recvMsgRegist    = self.genMessageRegist(self.parser.requests,"Req","RpcReqRegist","RpcCS"),
            sendMsgRegist    = self.genMessageRegist(self.parser.responses,"Rep","RpcRepRegist","RpcSC")
            )

        subPath = self.outputPath + "/proto/rpc/" + package_name
        if not os.path.exists(subPath):
            os.makedirs(subPath)
        common.write_file(subPath + "/"+package_name+".go", c)


    # 生成handler_interface
    def genInterface(self,structList,handlerName):
        tpl = Template(common.read_file(self.templatePath + "/interface.tpl"))
        return tpl.substitute(
            handler_name = handlerName,
            handler_funs = self.genInterfaceFun(structList)
            )

    def genPlayerImport(self,structList):
        if len(structList) == 0:
            return ""
        return "\n\t\"game/network\""

    def genRouterImport(self,structList):
        if len(structList) == 0:
            return ""
        return "\n\t\"game/network/router\"\n\t\"game/network/rpc\""



    def genInterfaceFun(self,structList):
        tpl = Template(common.read_file(self.templatePath + "/interface_fun.tpl"))
        return_tpl = Template(common.read_file(self.templatePath + "/interface_fun_return.tpl"))
        codeStr = ''
        for struct in structList:
            fun_return = 'error'
            rep = ''
            if struct.cmd in self.parser.responsesCmdDict:
                rep_struct = self.parser.responsesCmdDict[struct.cmd]
                rep = ", rep *"+return_tpl.substitute(
                    fun = common.CamelCase(rep_struct.name),
                    pb_name = "pb_"+self.tag+"_"+self.parser.modName
                )
            
            codeStr += "\n\t"+tpl.substitute(
                rep = rep,
                desc = struct.desc,
                fun = common.CamelCase(struct.name),
                pb_name = "pb_"+self.tag+"_"+self.parser.modName,
                fun_return = fun_return
            )
        return codeStr


    # pt 生成协议号常量
    def genPtConst(self,structList,prefixStr,modName):
        MaxNameLen = fields_util.get_golang_field_max_length(structList)
        MaxCmdLen = fields_util.get_golang_cmd_max_length(structList)
        codeStr = ''
        for struct in structList:
            if codeStr != '':
                codeStr += "\n"
            ptName = common.CamelCase(struct.name)
            codeStr += "\t" + prefixStr + ptName + common.gen_space(MaxNameLen-len(ptName)) + " uint32 = " + struct.cmd + common.gen_space(MaxCmdLen - len(struct.cmd)) + " // " + struct.desc
        if codeStr == '':
            return codeStr
        else:
            return "const(\n"+codeStr+"\n)"

    # pt 生成自定义常量
    def genConsts(self,constants):
        codeStr = ''
        for constant in constants:
            MaxNameLen = fields_util.get_golang_field_max_length(constant.fields)
            MaxValueLen = fields_util.get_golang_value_max_length(constant.fields)
            tmpStr = ''
            typeName = common.CamelCase(constant.name)
            for field in constant.fields:
                if tmpStr != '':
                    tmpStr += "\n"
                fieldName = common.CamelCase(field.name)
                tmpStr += "\t" + typeName + fieldName + common.gen_space(MaxNameLen-len(fieldName)) + " " + typeName +" = " + str(field.value) + common.gen_space(MaxValueLen - len(str(field.value))) + " // " + field.desc
            if tmpStr != '':
                tmpStr = "\n"+"\nconst(\n"+tmpStr+"\n)\n"
                tmpStr = "\n// "+constant.desc+"\ntype "+typeName+" " + constant.type + tmpStr
            codeStr += tmpStr
        return codeStr

        
    # pt 生成消息注册函数
    def genMessageRegist(self,structList,prefixStr,method,ptPrefixStr):
        template = Template(common.read_file(self.templatePath + "/message_regist.tpl"))
        codeStr = ''
        for struct in structList:
            codeStr += "\n" + template.substitute(
                desc = struct.desc,
                method = method,
                cmd = ptPrefixStr+common.CamelCase(struct.name),
                struct = prefixStr+common.CamelCase(struct.name),
                pb = "pb_"+self.tag+"_"+self.parser.modName
                )
        return codeStr

    # handler 生成接收函数注册
    def genRegistFuns(self,structList):
        template = Template(common.read_file(self.templatePath + "/handler_regist_fun.tpl"))
        codeStr = ''
        for struct in structList:
            if codeStr != '':
                codeStr += "\n"
            codeStr += template.substitute(
                cmd = "RpcCS"+common.CamelCase(struct.name),
                fun = "onRpc"+common.CamelCase(struct.name)
                )
        return codeStr

    # handler 生成接收函数
    def genHandlerFuns(self,structList,pb_name):
        template = Template(common.read_file(self.templatePath + "/handler_fun.tpl"))
        template_with_return = Template(common.read_file(self.templatePath + "/handler_fun_with_return.tpl"))
        return_tpl = Template(common.read_file(self.templatePath + "/interface_fun_return.tpl"))
        codeStr = ''
        for struct in structList:
            tpl = template
            rep = ""
            if struct.cmd in self.parser.responsesCmdDict:
                rep_struct = self.parser.responsesCmdDict[struct.cmd]
                rep = "&"+return_tpl.substitute(
                    fun = common.CamelCase(rep_struct.name),
                    pb_name = "pb_"+self.tag+"_"+self.parser.modName
                )+"{}"
                tpl = template_with_return
            codeStr += "\n\n" + tpl.substitute(
                desc = struct.desc,
                pb_name = pb_name,
                rep = rep,
                cmd = "RpcCS"+common.CamelCase(struct.name),
                fun = common.CamelCase(struct.name),
                req_sturct = "Req"+common.CamelCase(struct.name)
                )
        return codeStr


    # request 生成函数
    def genRequestFuns(self,structList,pb_name):
        template_cast = Template(common.read_file(self.templatePath + "/request_fun_cast.tpl"))
        template_call = Template(common.read_file(self.templatePath + "/request_fun_call.tpl"))

        codeStr = ''
        for struct in structList:
            tpl = template_cast
            rep = ""
            if struct.cmd in self.parser.responsesCmdDict:
                tpl = template_call
            codeStr += "\n\n" + tpl.substitute(
                desc = struct.desc,
                pb_name = pb_name,
                fun = common.CamelCase(struct.name),
                )
        return codeStr
