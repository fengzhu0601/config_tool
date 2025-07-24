import os
import codecs
from re import sub
import re

typeMap = {"int8":"int8","uint8":"uint8","int16":"int16","uint16":"uint16","int32":"int32",\
            "uint32":"uint32","int":"int","uint":"uint","int64":"int64","uint64":"uint64",\
            "float32":"float32","float":"float32","float64":"float64", "string":"string", "bool":"bool",\
            "int8[]":"[]int8", "uint8[]":"[]uint8", "int16[]":"[]int16","uint16[]":"[]uint16", "int32[]":"[]int32",\
            "uint32[]":"[]uint32", "int[]":"[]int", "uint[]":"[]uint", "int64[]":"[]int64", "uint64[]":"[]uint64",\
            "float[]":"[]float","float32[]":"[]float32","float64[]":"[]float64",\
            "item":"cfg.ItemList","attri":"cfg.Attri" }

def scan_path(Path, Ends):
    fileList = []
    for _root, _dirs, files in os.walk(Path):
        for fileObj in files:
            if fileObj.endswith(Ends):
                fileList.append(fileObj)
    return fileList
    
# 字符串转换为CamelCase
def CamelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string


def MakePackName(string):
  string = sub( r"([A-Z])", r" \1", string).lower().replace(" ", "_")
  if string[-4:] =="_cfg":
    string = string[0:-4]
  return "cfg"+ string


def trans_type(type):
  if type in typeMap:
    return typeMap[type]
  return type


def is_int_slice(t):
  baseType = ("int8[]", "uint8[]", "int16[]","uint16[]", "int32[]", "uint32[]", "int[]", "uint[]", "int64[]", "uint64[]","float[]","float32[]","float64[]")
  return t in baseType

def is_base_type(t):
    baseType = ("int8", "uint8", "int16","uint16", "int32", "uint32", "int", "uint", "int64", "uint64", "float32", "float", "float64", "string", "bool")
    return t in baseType



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


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
    

# 获取fields的最大长度(对齐用)
def get_field_max_length(fields):
    MaxLen = 0
    for field in fields:
        fieldLen = len(field["name"])
        if fieldLen > MaxLen:
            MaxLen = fieldLen
    return MaxLen

# 获取type的最大长度(对齐用)
def get_type_max_length(fields):
    MaxLen = 0
    for field in fields:
        typeLen = len(field["type"])
        if typeLen > MaxLen:
            MaxLen = typeLen
    return MaxLen