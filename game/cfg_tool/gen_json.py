import xlrd #需要1.2.0版本的，2.0以上的版本只能读取.xls类型的文件
import common
import os
import sys
import json

fileMap = {}

# 读取文件(.xlsx .xls) 然后返回字典数据
def readFile(filePath):
    global fileMap
    try:
        # 通过扩展名判断是否为支持的Excel格式
        fileType = filePath.split(".")[-1].lower()
        if fileType == 'xlsx' or fileType=='xls':
            wb = xlrd.open_workbook(filePath) #使用xlrd库打开工作簿
            for sh in wb.sheets():# 遍历所有工作表
                sheet_name = sh.name

                if sheet_name not in fileMap:
                    fileMap[sheet_name] = []

                #跳过名称包含"Sheet/sheet"的默认工作表
                if sheet_name.find("Sheet") != -1 or sheet_name.find("sheet") != -1:
                    break

                print("导出配置:",filePath," ---> ",sh.name+".json")
                title = [] # 字段列表
                types = [] # 类型列表
                readidx = [] # 有效列
                keyidxMap = {} # key列映射
                idx = 0 # 列数计数器
                # 遍历第一行的数据
                for item in sh.row_values(0):
                    if item != "":
                        readidx.append(idx)
                    title.append(common.CamelCase(item))
                    # 第5行如果不为空，这表示这一列是key
                    if sh.row_values(4)[idx] != "":
                        keyidxMap[idx] = True
                    else:
                        keyidxMap[idx] = False
                    idx += 1

                # 遍历第3行的类型
                for item in sh.row_values(2):
                    types.append(item)
                # data = []
                # 从第6行开始读数据
                for it in range(5,sh.nrows):
                    rowMap = {}  # 初始化单行数据字典
                    # 遍历所有有效列索引
                    for index in readidx:
                        # 如果单元格值不为空
                        if sh.row_values(it)[index] != "":
                            # 转换数据类型并添加到rowMap
                            tem =     transfer(sh.row_values(it)[index],types[index])
                            rowMap[title[index]] = tem
                            # rowMap[title[index]] = transfer(sh.row_values(it)[index],types[index])
                        # 如果单元格为空且是关键字列
                        elif keyidxMap[index] == True:
                            print("xxxx\nxxxx 导出配置错误:",filePath,"第",it+1,"行key不完整\nxxxx")
                            exit(1)
                    # 将单行数据添加到全局存储
                    fileMap[sheet_name].append(rowMap)
                
            #return data,sh.name
        else:
            return -1,""
    except(EOFError):
        print("转化过程出错！")
        print(EOFError)
        return -1,""

def makeJsonFile():
    global fileMap
    for sheetName in fileMap:
        data = fileMap[sheetName]
        jsonFileName = os.path.join(jsonPath,sheetName)+".json"
        f = open(jsonFileName,'w',encoding='utf-8')
        json.dump(data,f,ensure_ascii=False,indent=1)


# 字符串输入，转成相应的类型    
def transfer(value,typeStr):
  isNum = common.is_number(value)
  if typeStr == "string":
      if isNum:
          return ""+str(value)+""
      else:
          return value
  if common.is_int_slice(typeStr):
    if isNum:
      return [int(value)]
    else:
        num_list = []
        # 新增空字符串处理
        if str(value).strip() == '':
            return num_list
        for i in str(value).split(","):
            if float(i) == float(int(float(i))):
                num_list.append(int(i))
            else:
                num_list.append(float(i))
        return num_list
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
    makeJsonFile()
            #if "second_key_type" in data:
            #  codeGen = CodeGen2()
            #else:
            #  codeGen = CodeGen1()
            #codeGen.gen(data,"./template/","./code/")


