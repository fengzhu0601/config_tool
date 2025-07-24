#!/bin/bash

#svn up /mnt/d/svn/doc/配置表格

#rm -rf ./json
#python gen_json.py /mnt/d/svn/doc/配置表格
#rm -rf ./code
#python gen_code.py /mnt/d/svn/doc/配置表格

# svn up ~/work/svn/PetWorld/xlsx --username zhuzi --password zhuzi123

# rm -rf ./excel/*
# cp ~/work/svn/PetWorld/xlsx/* ./excel/

rm -rf ./json
python gen_json.py ./excel

# rm -rf ./code
# python gen_code.py ./excel
