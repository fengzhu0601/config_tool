
from queue import Empty
from string import Template
import os
import codecs
import common as common


class CodeGen(object):

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
        tpl = Template(common.read_file(self.templatePath + self.parser["tpl"]))

        if not "second_key_type" in self.parser:
            self.parser["second_key_type"] = "undefined"
        if not "second_key_name" in self.parser:
            self.parser["second_key_name"] = "undefined"

        if not "third_key_type" in self.parser:
            self.parser["third_key_type"] = "undefined"
        if not "third_key_name" in self.parser:
            self.parser["third_key_name"] = "undefined"

        package_name = self.parser["package_name"]
        c = tpl.substitute(
            package_name        = package_name,
            excel               = self.parser["excel"],
            cfg_name            = self.parser["cfg_name"],
            first_key_type      = self.parser["first_key_type"],
            first_key_name      = self.parser["first_key_name"],
            second_key_type     = self.parser["second_key_type"],
            second_key_name     = self.parser["second_key_name"],
            third_key_type     = self.parser["third_key_type"],
            third_key_name     = self.parser["third_key_name"],
            struct              = self.genSturct(),

            cfgListByIndex      = self.genCfgListByIndex(),
            tmpCfgListByIndex   = self.genTmpCfgListByIndex(),
            cfgListByIndexSet   = self.genCfgListByIndexSet(),
            cfgListByIndexSetValue = self.genCfgListByIndexSetValue(),
            getCfgsByIndex      = self.genGetCfgsByIndex()

            )

        subPath = self.outputPath + package_name
        if not os.path.exists(subPath):
            os.makedirs(subPath)
        common.write_file(subPath + "/"+package_name+".go", c)


    def genSturct(self):
        tpl = Template(common.read_file(self.templatePath + "/struct.tpl"))
        c = tpl.substitute(
            cfg_name = self.parser["cfg_name"],
            fields = self.genFields()
        )
        return c

    
    def genFields(self):
        str = ""
        fields = self.parser["fields"]
        FieldMaxLen = common.get_field_max_length(fields)
        TypeMaxLen = common.get_type_max_length(fields)
        for field in fields:
            field_name = field["name"]
            field_type = field["type"]
            str += "\n\t"+field_name+common.gen_space(FieldMaxLen - len(field_name)+1)+ field_type + common.gen_space(TypeMaxLen - len(field_type)+1) +"// "+field["desc"]
        return str


    def genCfgListByIndex(self):
        tpl = Template(common.read_file(self.templatePath + "/cfgListByIndex.tpl"))
        str = ""
        for field in self.parser["indexs"]:
            str += "\n"+tpl.substitute(
                field_name = field["field_name"],
                field_type = field["field_type"],
                cfg_name = self.parser["cfg_name"],
            )
        return str


    def genTmpCfgListByIndex(self):
        tpl = Template(common.read_file(self.templatePath + "/tmpCfgListByIndex.tpl"))
        str = ""
        for field in self.parser["indexs"]:
            str += "\t"+tpl.substitute(
                field_name = field["field_name"],
                field_type = field["field_type"],
                cfg_name = self.parser["cfg_name"],
            )+"\n"
        return str

    def genCfgListByIndexSet(self):
        tpl = Template(common.read_file(self.templatePath + "/cfgListByIndexSet.tpl"))
        str = ""
        for field in self.parser["indexs"]:
            str += "\n"+tpl.substitute(
                field_name = field["field_name"],
                field_type = field["field_type"],
                cfg_name = self.parser["cfg_name"],
            )+"\n"
        return str

    def genCfgListByIndexSetValue(self):
        tpl = Template(common.read_file(self.templatePath + "/cfgListByIndexSetValue.tpl"))
        str = ""
        for field in self.parser["indexs"]:
            str += "\n\t"+tpl.substitute(
                field_name = field["field_name"],
                field_type = field["field_type"],
                cfg_name = self.parser["cfg_name"],
            )
        return str


    def genGetCfgsByIndex(self):
        tpl = Template(common.read_file(self.templatePath + "/getCfgsByIndex.tpl"))
        str = ""
        for field in self.parser["indexs"]:
            str += "\n"+tpl.substitute(
                field_desc = field["field_desc"],
                field_name = field["field_name"],
                field_type = field["field_type"],
                cfg_name = self.parser["cfg_name"],
            ) + "\n"
        return str

