#!/bin/bash

rm -rf codegen/
rm -rf pbgen/
python script/gen.py template/ xml/ codegen/ pbgen/

# cp -rf codegen/golang/game/* ../src/
