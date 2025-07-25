from dataclasses import fields
from pickle import TRUE
from unicodedata import name
import xlrd #需要1.2.0版本的，2.0以上的版本只能读取.xls类型的文件
import common
import os
import sys
from CodeGen import CodeGen
from MethodGen import MethodGen

fileMap = {}

# 读取文件(.xlsx .xls .csv) 然后返回字典数据
def readFile(filePath):
    global fileMap
    try:
        fileType = filePath.split(".")[-1].lower()

        # # window下的处理
        # excelName = filePath.split(".")[0].split("\\")[-1]
        # 跨平台处理
        excelName = os.path.splitext(os.path.basename(filePath))[0]
        if fileType == 'xlsx' or fileType=='xls':
            wb = xlrd.open_workbook(filePath)
            # sh = wb.sheet_by_index(0)
            for sh in wb.sheets():
                sheet_name = sh.name
                if sheet_name in fileMap:
                  # 相同名字的sheet不再重复生成代码
                  continue
                fileMap[sheet_name] = True
                # 过滤不需要处理的sheet
                if sheet_name.find("Sheet") != -1 or sheet_name.find("sheet") != -1:
                    break
                print("导出代码:",filePath," ---> ",sh.name)

                # 解析表头信息（第0-4行）
                data = {}
                data["indexs"] = []
                fields = []
                readidx = [] # 有效列
                idx = 0
                for item in sh.row_values(0):
                    if item != "":
                        readidx.append(idx) # 收集非空列索引
                    idx += 1

                # 提取字段定义（名称/描述/类型）
                for index in readidx:
                  field = {}
                  field["name"] = common.CamelCase(sh.row_values(0)[index]) # 字段名转驼峰
                  field["desc"] = sh.row_values(1)[index]# 描述信息
                  field["type"] = common.trans_type(sh.row_values(2)[index])# 类型转换
                  field["desc_more"] = sh.row_values(3)[index]# 补充描述
                  fields.append(field)

                  # 设置索引键（第4行标记1/2/3表示一/二/三级键）
                  if sh.row_values(4)[index] != "":
                    indexInfo = {}
                    indexInfo["field_name"] = field["name"]
                    indexInfo["field_type"] = field["type"]
                    indexInfo["field_desc"] = field["desc"]
                    data["indexs"].append(indexInfo)

                  if sh.row_values(4)[index] == 1:
                    data["first_key_type"]      = field["type"]
                    data["first_key_name"]      = field["name"]

                  elif sh.row_values(4)[index] == 2:
                    data["second_key_type"]      = field["type"]
                    data["second_key_name"]      = field["name"]

                  elif sh.row_values(4)[index] == 3:
                    data["third_key_type"]      = field["type"]
                    data["third_key_name"]      = field["name"]


                # 代码生成配置
                data["fields"] = fields
                data["package_name"] = common.MakePackName(sh.name)
                data["cfg_name"] = sh.name
                data["excel"] = excelName

                if "third_key_type" in data:
                    data["tpl"] = "/key3.tpl"
                elif "second_key_type" in data:
                    data["tpl"] = "/key2.tpl"
                else:
                    data["tpl"] = "/key1.tpl"
                codeGen = CodeGen()
                methodGen = MethodGen()

                codeGen.gen(data,"./template/","./code/")
                methodGen.gen(data,"./template/","./code/")
            return 0
        else:
            return -1
    except(EOFError):
        print("转化过程出错！")
        print(EOFError)
        return -1


# 字符串输入，转成相应的类型    
def transfer(value,typeStr):
  isNum = common.is_number(value)
  if common.is_int_slice(typeStr):
    if isNum:
      return [int(value)]
    else:
      return [int(i) for i in str(value).split(",")]
  try:
      if float(value) == float(int(float(value))):
          return int(value)
      else:
          return float(value)
  except:
      pass
  return True if value.lower() == 'true' else (False if value.lower() == 'false' else value)

# # 自定义json编码器
# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#       print("obj=",obj)
#       return super(MyEncoder, self).default(obj)

list=[]
def listFile(path):
  fileNames=os.listdir(path)
  for fileName in fileNames:
      combine=os.path.join(path,fileName)
      if os.path.isfile(combine):
          list.append(combine)
      else:
          list.append(combine)
          listFile(combine)
  return list

if __name__ == '__main__':
  excelPath = sys.argv[1]
  # excelPath = "./excel/"
  jsonPath = "./json/"
  if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)

  # 仅支持Excel格式(.xlsx和.xls)
  SUPPORTED_FORMATS = ('.xlsx', '.xls')
  for file in listFile(excelPath):
    if file.lower().endswith(SUPPORTED_FORMATS) and file.find("$") == -1:
      data = readFile(r''+file)
      #if "second_key_type" in data:
      #  codeGen = CodeGen2()
      #else:
      #  codeGen = CodeGen1()
      #codeGen.gen(data,"./template/","./code/")



