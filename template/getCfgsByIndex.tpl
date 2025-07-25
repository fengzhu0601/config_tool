// 根据$field_desc获取配置列表
func GetCfgsBy$field_name($field_name $field_type) []*$cfg_name {
	list, exit := cfgListBy$field_name[$field_name]
	if !exit {
		return make([]*$cfg_name, 0)
	}
	return list
}