package $package_name

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (
	"encoding/json"
	"fmt"
	"game/cfg"
)

$struct

type cfgMap map[$first_key_type]*$cfg_name

var cfgList []*$cfg_name = make([]*$cfg_name, 0)
$cfgListByIndex


var cfgM cfgMap = make(cfgMap)

func Load() error {
	tmpCfgM := make(cfgMap)
$tmpCfgListByIndex
	jsonFile := "$cfg_name.json"
	jsonData, err := cfg.GetJsonData(jsonFile)
	if err != nil {
		return err
	}
	var tmpList []*$cfg_name
	err = json.Unmarshal(jsonData, &tmpList)
	if err != nil {
		fmt.Println("Unmarshal json file error", jsonFile, err)
		return err
	}
	for _, cfg := range tmpList {
		tmpCfgM[cfg.$first_key_name] = cfg
$cfgListByIndexSet
	}

	cfgList = tmpList
	cfgM = tmpCfgM
$cfgListByIndexSetValue

	return nil
}

// 获取唯一配置
func GetCfg($first_key_name $first_key_type) *$cfg_name {
	c, exit := cfgM[$first_key_name]
	if !exit {
		cfg.NoticCfgNull("$excel","$package_name",$first_key_name)
		return nil
	}
	return c
}

// 获取所有配置
func GetAllCfgs() []*$cfg_name {
	return cfgList
}
$getCfgsByIndex
func init(){
	Load()
}
