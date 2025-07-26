# -*- coding: utf-8 -*-

from ProtoParser import ProtoParser
from CodeGenGolang import CodeGenGolang
from CodeGenGolangDS import CodeGenGolangDS
from CodeGenGolangRpc import CodeGenGolangRpc
from CodeGenPB import CodeGenPB
from CodeGenLua import CodeGenLua
import sys
import os
import common as common
import functools

'''
扫描目录找xml文件
'''
codeReqDesList = []
codeReqCmdList = []
codeResDesList = []
codeResCmdList = []
codePbList = []
codeEnumList = []
csRequestMap = {}
cdRepsoneMap = {}


def scan_path(Path, Ends):
    fileList = []
    for _root, _dirs, files in os.walk(Path):
        for fileObj in files:
            if fileObj.endswith(Ends):
                fileList.append(fileObj)
    return fileList


def clean_lua_cache():
    global codeReqDesList
    global codeReqCmdList
    global codeResDesList
    global codeResCmdList
    global codePbList
    global codeEnumList
    codeReqDesList = []
    codeReqCmdList = []
    codeResDesList = []
    codeResCmdList = []
    codePbList = []
    codeEnumList = []


def numeric_compare(x, y):
    return x["cmd"] - y["cmd"]


def checkRepeat(ps):
    global csRequestMap
    global cdRepsoneMap
    for req in ps.requests:
        if req.cmd in csRequestMap:
            print("xxxx\nxxxx 生成错误: request",req.cmd,"重复\nxxxx")
        csRequestMap[req.cmd] = True
    for rep in ps.responses:
        if rep.cmd in cdRepsoneMap:
            print("xxxx\nxxxx 生成错误: respone",rep.cmd,"重复\nxxxx")
        cdRepsoneMap[rep.cmd] = True

def write_json_cmd(jsonpbpath):
    global codeReqDesList
    global codeReqCmdList
    global codeResDesList
    global codeResCmdList
    global codePbList
    global codeEnumList
    codeReqCmdList.sort(key=functools.cmp_to_key(numeric_compare))
    codeResCmdList.sort(key=functools.cmp_to_key(numeric_compare))
    luacode = "[\n\t{\n"
    count= 0
    for reqCmd in codeReqCmdList:
        count+=1
        luacode += "\t\t{0}".format(common.GetJsonName("\t{0}".format(reqCmd["des"]) , ":{0}".format(reqCmd["cmd"])))
        if count==len(codeReqCmdList):
            luacode += "\n"
        else:
            luacode += ",\n"
    luacode += "\t},\n"

    luacode += "\t{\n"
    count= 0
    for resCmd in codeResCmdList:
        count+=1
        luacode += "\t\t{0}".format(common.GetJsonName("\t{0}".format(resCmd["des"]) , ":{0}".format(resCmd["cmd"])))
        if count==len(codeResCmdList):
            luacode += "\n"
        else:
            luacode += ",\n"
    luacode += "\t}\n]\n"
    common.write_file(os.path.join(luapbpath, "cmd.json"), luacode)


def write_lua_cmd(luapbpath):
    global codeReqDesList
    global codeReqCmdList
    global codeResDesList
    global codeResCmdList
    global codePbList
    global codeEnumList
    codeReqCmdList.sort(key=functools.cmp_to_key(numeric_compare))
    codeResCmdList.sort(key=functools.cmp_to_key(numeric_compare))
    luacode = "local Items=\n{\n"
    luacode += "\trequest=\n\t{\n"
    for reqDes in codeReqDesList:
        luacode += "\t\t{0}\n".format(reqDes)
    luacode += "\t},\n"
    luacode += "\tresponse=\n\t{\n"
    for resDes in codeResDesList:
        luacode += "\t\t{0}\n".format(resDes)
    luacode += "\t},\n"
    luacode += "\tpbList=\n\t{\n"
    for pb in codePbList:
        luacode += "\t\t{0}\n".format(pb)
    luacode += "\t},"
    luacode += "\n}\n"
    luacode += "pb_ReqID = \n{\n"
    for reqCmd in codeReqCmdList:
        luacode += "\t{0}\n".format(reqCmd["des"])
    luacode += "}\n"
    luacode += "pb_ResID = \n{\n"
    for resCmd in codeResCmdList:
        luacode += "\t{0}\n".format(resCmd["des"])
    luacode += "}\n"
    for codeEnum in codeEnumList:
        luacode += "{0}".format(codeEnum)
    luacode += "\n\nreturn Items"
    common.write_file(os.path.join(luapbpath, "cmd.lua"), luacode)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("genproto [template path] [protocol xml path] [output path]")
        exit()
    TemplatePath = sys.argv[1]
    ProtocolPath = sys.argv[2]
    CodeGenPath = sys.argv[3]
    PBGenPath = sys.argv[4]

    path = "codegen/golang"
    if not os.path.exists(path + "/game"):
        os.makedirs(path)

    clean_lua_cache()
    luapbpath = os.path.abspath("./codegen/lua/pb/")
    luapbprefix = "pb_cs_"
    if not os.path.exists(luapbpath):
        os.makedirs(luapbpath)
    # 生成cs pb+代码
    CSProtoPath = ProtocolPath + "cs/"
    CSPBGenPath = PBGenPath + "cs/"


    for xf in scan_path(CSProtoPath, '.xml'):
        ps = ProtoParser()
        ps.parserModule(CSProtoPath + xf, xf)
        checkRepeat(ps)
        golang = CodeGenGolang()
        golang.genServerGolang(ps, TemplatePath + "golang", CodeGenPath + "/golang/game")
        pb = CodeGenPB()
        pb.genPB(ps, TemplatePath + "pb", CSPBGenPath, "cs")
        # -----lua
        lua = CodeGenLua()
        codeReqDes, codeReqCmd, codeResDes, codeResCmd, pbName, codeEnum = lua.genLua(ps, luapbprefix)
        codeReqDesList.extend(codeReqDes)
        codeReqCmdList.extend(codeReqCmd)
        codeResDesList.extend(codeResDes)
        codeResCmdList.extend(codeResCmd)
        codePbList.append("'{0}',".format(pbName))
        codeEnumList.extend(codeEnum)
        #--

    write_lua_cmd(luapbpath)
    write_json_cmd(luapbpath)

    for xf in scan_path(CSPBGenPath, '.proto'):
        cmd = "tool/protoc --go_out=" + path + " " + os.path.join(os.path.abspath(CSPBGenPath),
                                                             xf) + " --proto_path=" + os.path.abspath(CSPBGenPath)
        # print(cmd)
        os.system(cmd)
        # lua
        filename, _ = os.path.splitext(xf)
        outputpath = "{0}/{1}.bytes".format(luapbpath, filename)
        cmdlua = "tool/protoc -o " + outputpath + " " + os.path.join(os.path.abspath(CSPBGenPath),
                                                                xf) + " --proto_path=" + os.path.abspath(CSPBGenPath)
        os.system(cmdlua)

    # 生成rpc pb+代码
    RPCProtoPath = ProtocolPath + "rpc/"
    RpcPBGenPath = PBGenPath + "rpc/"
    for xf in scan_path(RPCProtoPath, '.xml'):
        ps = ProtoParser()
        ps.parserModule(RPCProtoPath + xf, xf)
        golang = CodeGenGolangRpc()
        golang.genServerGolangRpc(ps, TemplatePath + "golang_rpc", CodeGenPath + "/golang/game", "rpc")
        pb = CodeGenPB()
        pb.genPB(ps, TemplatePath + "pb", RpcPBGenPath, "rpc")

    # 生成ds pb+rpc+代码
    clean_lua_cache()
    luapbdspath = os.path.abspath("./codegen/lua/pb_ds/")
    luapbprefix = "pb_ds_"
    if not os.path.exists(luapbdspath):
        os.makedirs(luapbdspath)
    DSProtoPath = ProtocolPath + "ds/"
    DSPBGenPath = PBGenPath + "ds/"
    for xf in scan_path(DSProtoPath, '.xml'):
        ps = ProtoParser()
        ps.parserModule(DSProtoPath + xf, xf)
        golang = CodeGenGolangDS()
        golang.genServerGolangDS(ps, TemplatePath + "golang_ds", CodeGenPath + "/golang/game")
        # golang = CodeGenGolangRpc()
        # golang.genServerGolangRpc(ps, TemplatePath + "golang_rpc", CodeGenPath + "/golang/game","ds")
        pb = CodeGenPB()
        pb.genPB(ps, TemplatePath + "pb", DSPBGenPath, "ds")
        #-----lua
        lua = CodeGenLua()
        codeReqDes, codeReqCmd, codeResDes, codeResCmd, pbName, codeEnum = lua.genLua(ps, luapbprefix)
        codeReqDesList.extend(codeReqDes)
        codeReqCmdList.extend(codeReqCmd)
        codeResDesList.extend(codeResDes)
        codeResCmdList.extend(codeResCmd)
        codePbList.append("'{0}',".format(pbName))
        codeEnumList.extend(codeEnum)
        #--

    write_lua_cmd(luapbdspath)

    for xf in scan_path(RpcPBGenPath, '.proto'):
        cmd = "tool/protoc --go_out=" + path + " " + os.path.join(os.path.abspath(RpcPBGenPath),
                                                             xf) + " --proto_path=" + os.path.abspath(RpcPBGenPath)
        # print(cmd)
        os.system(cmd)

    for xf in scan_path(DSPBGenPath, '.proto'):
        cmd = "tool/protoc --go_out=" + path + " " + os.path.join(os.path.abspath(DSPBGenPath),
                                                             xf) + " --proto_path=" + os.path.abspath(DSPBGenPath)
        # print(cmd)
        os.system(cmd)
        # lua
        filename, _ = os.path.splitext(xf)
        outputpath = "{0}/{1}.pb".format(luapbdspath, filename)
        cmdlua = "tool/protoc -o " + outputpath + " " + os.path.join(os.path.abspath(DSPBGenPath),
                                                                xf) + " --proto_path=" + os.path.abspath(DSPBGenPath)
        os.system(cmdlua)

    print('finished')
