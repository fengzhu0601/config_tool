        if _, exit := tmpCfgListBy$field_name[cfg.$field_name];!exit{
            tmpCfgListBy$field_name[cfg.$field_name] = make([]*$cfg_name,0)
        }
        tmpCfgListBy$field_name[cfg.$field_name] = append(tmpCfgListBy$field_name[cfg.$field_name],cfg)