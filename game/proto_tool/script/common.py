import os
import codecs
from re import sub
import re

# 字符串转换为CamelCase
def CamelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string



def is_base_type(t):
    baseType = ("int8", "uint8", "int16","uint16", "int32", "uint32", "int", "uint", "int64", "uint64", "float32", "float", "float64", "string", "bool")
    return t in baseType

def base_type_map_erlang_type(t, isarray=False):
    typeMap = {"int8":"integer()","uint8":"integer()","int16":"integer()","uint16":"integer()","int32":"integer()",\
               "uint32":"integer()","int":"integer()","uint":"integer()","int64":"integer()","uint64":"integer()",\
               "float32":"float()","float":"float()","float64":"float()", "string":"list()" }
    if t in typeMap:
        if isarray == True:
          return "list("+typeMap[t]+")"
        return typeMap[t]
    if isarray == True:
      return "list(ps_"+t+")"
    return t

def to_golang_type(t, imp, isarray=False):
    typeMap = {"int8":"int8","uint8":"uint8","int16":"int16","uint16":"uint16","int32":"int32",\
               "uint32":"uint32","int":"int","uint":"uint","int64":"int64","uint64":"uint64",\
               "float32":"float32","float":"float32","float64":"float64", "string":"string", "bool":"bool" }
    if t in typeMap:
        if isarray == True:
          return "[]"+typeMap[t]
        return typeMap[t]
    t = CamelCase(t)
    if len(imp) > 0:
      t = "pt_"+imp+'.'+t
    if isarray == True:
      return "[]"+t
    return t


def to_pb_type(t, tag, imp, isarray=False):
    typeMap = {"int8":"int32","uint8":"uint32","int16":"int32","uint16":"uint32","int32":"int32",\
               "uint32":"uint32","int":"int32","uint":"uint32","int64":"int64","uint64":"uint64",\
               "float32":"float32","float":"float32","float64":"float64", "string":"string",\
               "sint32":"sint32","sint64":"sint64","bool":"bool" }
    if t in typeMap:
        if isarray == True:
          return "repeated "+typeMap[t]
        return typeMap[t]
    t = CamelCase(t)
    if len(imp) > 0:
      t = "pb_"+tag+"_"+imp+'.'+t
    if isarray == True:
      return "repeated "+t
    return t


def gen_space(Num):
    t = ''
    for _i in range(0,Num):
        t += ' '
    return t

def gen_tab(Num):
    t = ''
    for _i in range(0,Num):
        t += '\t'
    return t


def read_file(Path):
    f = codecs.open(Path, "r", "utf-8")  
    c = f.read()
    f.close()
    return c

def write_file(Path, Context):
    f = codecs.open(Path, "w", "utf-8")
    f.write(Context)
    f.close()

def GetJsonName(string1, string2):
    result = re.sub("_", ".", ''.join(re.findall(r'[A-Za-z]*\_[A-Za-z]*', string1)))
    return "\"PbCs"+ result+"\""+string2
