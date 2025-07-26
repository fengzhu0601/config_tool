package cfg_drop_weight

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (
	"encoding/json"
	"fmt"
	"game/cfg"
)

type DropWeight struct {
	DropId     int32   // 掉落ID
	Id         int32   // ID
	Type       int32   // 掉落类型
	Desc       string  // 说明
	DropItems  []int32 // 掉落物品
	Max        int32   // 最大抽取
	Min        int32   // 最小抽取
	WeightRate int32   // 权重或概率
	Grades     []int32 // 品质
}

type cfgMap map[int32]map[int32]*DropWeight

var cfgList []*DropWeight = make([]*DropWeight, 0)

var cfgListByDropId map[int32][]*DropWeight = make(map[int32][]*DropWeight)
var cfgListById map[int32][]*DropWeight = make(map[int32][]*DropWeight)

var cfgM cfgMap = make(cfgMap)

func Load() error {
	tmpCfgM := make(cfgMap)
	tmpCfgListByDropId := make(map[int32][]*DropWeight)
	tmpCfgListById := make(map[int32][]*DropWeight)

	jsonFile := "DropWeight.json"
	jsonData, err := cfg.GetJsonData(jsonFile)
	if err != nil {
		return err
	}
	var tmpList []*DropWeight
	err = json.Unmarshal(jsonData, &tmpList)
	if err != nil {
		fmt.Println("Unmarshal json file error", jsonFile, err)
		return err
	}
	for _, cfg := range tmpList {
		_, exit := tmpCfgM[cfg.DropId]
		if !exit {
			tmpCfgM[cfg.DropId] = make(map[int32]*DropWeight)
		}
		tmpCfgM[cfg.DropId][cfg.Id] = cfg
		

        if _, exit := tmpCfgListByDropId[cfg.DropId];!exit{
            tmpCfgListByDropId[cfg.DropId] = make([]*DropWeight,0)
        }
        tmpCfgListByDropId[cfg.DropId] = append(tmpCfgListByDropId[cfg.DropId],cfg)

        if _, exit := tmpCfgListById[cfg.Id];!exit{
            tmpCfgListById[cfg.Id] = make([]*DropWeight,0)
        }
        tmpCfgListById[cfg.Id] = append(tmpCfgListById[cfg.Id],cfg)


	}

	cfgList = tmpList
	cfgM = tmpCfgM

	cfgListByDropId = tmpCfgListByDropId
	cfgListById = tmpCfgListById
	
	return nil
}

// 获取唯一配置
func GetCfg(DropId int32, Id int32) *DropWeight {
	subMap, exit := cfgM[DropId]
	if !exit {
		cfg.NoticCfgNull("权重掉落表","cfg_drop_weight",DropId,Id)
		return nil
	}
	c, exit := subMap[Id]
	if !exit {
		cfg.NoticCfgNull("权重掉落表","cfg_drop_weight",DropId,Id)
		return nil
	}
	return c
}

// 获取所有配置
func GetAllCfgs() []*DropWeight {
	return cfgList
}

// 根据掉落ID获取配置列表
func GetCfgsByDropId(DropId int32) []*DropWeight {
	list, exit := cfgListByDropId[DropId]
	if !exit {
		return make([]*DropWeight, 0)
	}
	return list
}

// 根据ID获取配置列表
func GetCfgsById(Id int32) []*DropWeight {
	list, exit := cfgListById[Id]
	if !exit {
		return make([]*DropWeight, 0)
	}
	return list
}

func init(){
	Load()
}
