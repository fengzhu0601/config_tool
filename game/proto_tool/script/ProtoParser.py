
import string
import xml.etree.ElementTree as ET
from data.struct import Struct
from data.const import Const
from data.imp import Import
from data.interface import Interface
from data.field import Field
from data.module import Module


class ProtoParser(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.modules = []
        self.moduleDict = {}
        self.structs = []
        self.structDict = {}

        self.records = []
        self.recordDict = {}

        self.reqRecords = []
        self.reqRecordDict = {}

        self.requests = []
        self.requestDict = {}
        self.responses = []
        self.responsesDict = {}
        self.responsesCmdDict = {}
        self.consts = []
        self.imports = []
        self.constDict = {}
        self.memberConstDict = {}
        self.importDict = {}
        self.commonConsts = None
        self.modName = None
        
        '''
    def setCmdsNo(self, outputPath):
        SCMD_INDEX = 1
        CCMD_INDEX = 1
        for request in self.requests:
            request.cmd = SCMD_INDEX
            SCMD_INDEX += 1
            
        for response in self.responses:
            response.cmd = CCMD_INDEX
            CCMD_INDEX += 1
            '''
            
        
    def parserModule(self, xmlPath, name):

        tree = ET.parse(xmlPath)
        root = tree.getroot()
        moduleName = root.attrib['name'].lower()
        self.modName = moduleName
        module = Module(moduleName)
        for child in root:
            if child.tag == 'constants':
                self._parseConst(module, child)
            elif child.tag == 'structs':
                self._parseStruct(module, child)
            elif child.tag == 'requests':
                self._parseInterface(module, child)
                self._parseRecordReq(module, child)
            elif child.tag == 'responses':
                self._parseInterface(module, child, False)
                self._parseRecord(module, child)
            elif child.tag == 'imports':
                self._parseImport(module, child)
            else :
                print ("Error Tag:"+child.tag)
        self.modules.append(module)
        self.moduleDict[module.name] = module


    def _parseRecordReq(self, module, xml):
        for child in xml.findall('request'):
            name = ''
            desc = ''
            cmd = 0
            if 'name' in child.attrib:
                name = child.attrib['name']
                if name in self.reqRecordDict:
                    return False
            else:
                return False
            if 'desc' in child.attrib:
                desc = child.attrib['desc']
            if 'cmd' in child.attrib:
                cmd = child.attrib['cmd']
            St = Struct(module,name,desc,cmd)
            for fl in child.findall('field'):
                field = self._parseField(fl)
                if St.addField(field) == False:
                    return False
            self.reqRecords.append(St)
            self.reqRecordDict[name] = St



    def _parseRecord(self, module, xml):
        for child in xml.findall('response'):
            name = ''
            desc = ''
            cmd = 0
            iszip = False
            if 'name' in child.attrib:
                name = child.attrib['name']
                if name in self.recordDict:
                    return False
            else:
                return False
            if 'desc' in child.attrib:
                desc = child.attrib['desc']
            if 'cmd' in child.attrib:
                cmd = child.attrib['cmd']
            if "zip" in child.attrib:
                if child.attrib['zip'] == "true":
                    iszip = True
            St = Struct(module,name,desc,cmd,iszip)
            for fl in child.findall('field'):
                field = self._parseField(fl)
                if St.addField(field) == False:
                    return False
            self.records.append(St)
            self.recordDict[name] = St
    
    
    def _parseStruct(self, module, xml):
        for child in xml.findall('struct'):
            name = ''
            desc = ''
            if 'name' in child.attrib:
                name = child.attrib['name']
                if name in self.structDict:
                    return False
            else:
                return False
            if 'desc' in child.attrib:
                desc = child.attrib['desc']
            St = Struct(module,name,desc,0)
            for fl in child.findall('field'):
                field = self._parseField(fl)
                if St.addField(field) == False:
                    return False
            self.structs.append(St)
            self.structDict[name] = St
                
    
    def _parseConst(self,  module, xml):
        for child in xml.findall('constant'):
            name = ''
            desc = ''
            vtype = 'uint8'
            public = False
            if 'name' in child.attrib:
                name = child.attrib['name']
                if name in self.constDict:
                    return False
            else:
                return False
            if 'desc' in child.attrib:
                desc = child.attrib['desc']
            if 'type' in child.attrib:
                vtype = child.attrib['type']
            if 'public' in child.attrib:
                public = (child.attrib['public'] == 'true')
            Ct = Const(module,name,desc,vtype,public)
            for fl in child.findall('field'):
                field = self._parseField(fl)
                if Ct.addField(field) == False:
                    return False
            self.consts.append(Ct)
            self.constDict[name] = Ct
            if name == 'TIPS':
                self.commonConsts = Ct

    def _parseImport(self,  module, xml):
        for child in xml.findall('import'):
            name = ''
            if 'name' in child.attrib:
                name = child.attrib['name']
                if name in self.importDict:
                    return False
            else:
                return False

            Im = Import(name)
            self.imports.append(Im)
            self.importDict[name] = Im

    
    def _parseInterface(self, module, xml, isRequest=True):
        if isRequest:
            for child in xml.findall('request'):
                name = ''
                desc = ''
                cmd = 0
                if 'name' in child.attrib:
                    name = child.attrib['name']
                    if name in self.requestDict:
                        return False
                else:
                    return False
                
                if 'cmd' in child.attrib:
                    cmd = child.attrib['cmd']
                else:
                    return False
                
                if 'desc' in child.attrib:
                    desc = child.attrib['desc']
                Itf = Interface(module,name,desc)
                Itf.cmd = cmd
                if 'call_mod' in child.attrib:
                    Itf.call_mod = child.attrib['call_mod']
                for fl in child.findall('field'):
                    field = self._parseField(fl)
                    if Itf.addField(field) == False:
                        return False
                self.requests.append(Itf)
                self.requestDict[name] = Itf
                module.addRequest(Itf)
        else:
            for child in xml.findall('response'):
                name = ''
                desc = ''
                cmd = 0
                iszip = False
                if 'name' in child.attrib:
                    name = child.attrib['name']
                    if name in self.responsesDict:
                        return False
                else:
                    return False
                
                if 'cmd' in child.attrib:
                    cmd = child.attrib['cmd']
                else:
                    return False
                
                if 'desc' in child.attrib:
                    desc = child.attrib['desc']
                if "zip" in child.attrib:
                    if child.attrib['zip'] == "true":
                        iszip = True
                Itf = Interface(module,name,desc)
                Itf.cmd = cmd
                Itf.zip = iszip
                for fl in child.findall('field'):
                    field = self._parseField(fl)
                    if Itf.addField(field) == False:
                        return False
                self.responses.append(Itf)
                self.responsesDict[name] = Itf
                self.responsesCmdDict[cmd] = Itf
                module.addResponse(Itf)
            
    def _parseField(self,xml):
        name = ''
        vtype = ''
        isarray = False
        value = 0
        desc = ''
        imp = ''
        
        if 'name' in xml.attrib:
            name = xml.attrib['name']
        if 'type' in xml.attrib:
            vtype = xml.attrib['type']
        if 'isarray' in xml.attrib:
            ik = str(xml.attrib['isarray'])
            if ik.strip().lower() == 'true':
                isarray = True
        if 'value' in xml.attrib:
            value = int(xml.attrib['value'])
        if 'desc' in xml.attrib:
            desc = xml.attrib['desc']
        if 'import' in xml.attrib:
            imp = xml.attrib['import']
    
        return Field(name,vtype,isarray,value,desc,imp)
    
    
    
    
    
    
    
    