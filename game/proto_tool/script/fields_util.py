import common as common

# 获取fields的最大长度(对齐用)
def get_golang_field_max_length(fields):
    MaxLen = 0
    for field in fields:
        fieldLen = len(common.CamelCase(field.name))
        if fieldLen > MaxLen:
            MaxLen = fieldLen
    return MaxLen

# 获取type的最大长度(对齐用)
def get_golang_type_max_length(fields):
    MaxLen = 0
    for field in fields:
        typeLen = len(common.to_golang_type(field.vtype, field.imp, field.isarray))
        if typeLen > MaxLen:
            MaxLen = typeLen
    return MaxLen

# 获取cmd的最大长度(对齐用)
def get_golang_cmd_max_length(fields):
    MaxLen = 0
    for field in fields:
        cmdLen = len(field.cmd)
        if cmdLen > MaxLen:
            MaxLen = cmdLen
    return MaxLen

# 获取value的最大长度(对齐用)
def get_golang_value_max_length(fields):
    MaxLen = 0
    for field in fields:
        valueLen = len(str(field.value))
        if valueLen > MaxLen:
            MaxLen = valueLen
    return MaxLen

# 获取fields+type的最大长度(对齐用)
def get_golang_field_and_type_max_length(fields):
	MaxLen = 0
	MaxFieldLen = get_golang_field_max_length(fields)
	for field in fields:
		typeLen = len(common.to_golang_type(field.vtype, field.imp, field.isarray))
		if MaxFieldLen+typeLen+1 > Max:
			MaxLen = field.len
	return MaxLen

