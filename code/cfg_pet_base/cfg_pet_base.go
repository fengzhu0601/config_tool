package cfg_pet_base

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (
	"encoding/json"
	"fmt"
	"game/cfg"
)

type PetBase struct {
	PetId        int32  // 宠物ID
	Name         string // 名称
	Desc         string // 描述
	LockDesc     string // 未解锁描述
	Model        string // 模型资源
	Speed        int32  // 移动速度
	Feed         int32  // 可喂养最大体力
	Action1      string // 动作1
	Action2      string // 动作2
	Action3      string // 动作3
	FeedTime     int32  // 饲养次数
	MaxSatiation int32  // 最高体力值
	HungerTime   int32  // 每次扣减饱食度周期
	HungerLose   int32  // 扣减数量
	HeadIcon     string // 头像图标
	Mood         int    // 心情值
}

type cfgMap map[int32]*PetBase

var cfgList []*PetBase = make([]*PetBase, 0)

var cfgListByPetId map[int32][]*PetBase = make(map[int32][]*PetBase)


var cfgM cfgMap = make(cfgMap)

func Load() error {
	tmpCfgM := make(cfgMap)
	tmpCfgListByPetId := make(map[int32][]*PetBase)

	jsonFile := "PetBase.json"
	jsonData, err := cfg.GetJsonData(jsonFile)
	if err != nil {
		return err
	}
	var tmpList []*PetBase
	err = json.Unmarshal(jsonData, &tmpList)
	if err != nil {
		fmt.Println("Unmarshal json file error", jsonFile, err)
		return err
	}
	for _, cfg := range tmpList {
		tmpCfgM[cfg.PetId] = cfg

        if _, exit := tmpCfgListByPetId[cfg.PetId];!exit{
            tmpCfgListByPetId[cfg.PetId] = make([]*PetBase,0)
        }
        tmpCfgListByPetId[cfg.PetId] = append(tmpCfgListByPetId[cfg.PetId],cfg)

	}

	cfgList = tmpList
	cfgM = tmpCfgM

	cfgListByPetId = tmpCfgListByPetId

	return nil
}

// 获取唯一配置
func GetCfg(PetId int32) *PetBase {
	c, exit := cfgM[PetId]
	if !exit {
		cfg.NoticCfgNull("宠物基础表","cfg_pet_base",PetId)
		return nil
	}
	return c
}

// 获取所有配置
func GetAllCfgs() []*PetBase {
	return cfgList
}

// 根据宠物ID获取配置列表
func GetCfgsByPetId(PetId int32) []*PetBase {
	list, exit := cfgListByPetId[PetId]
	if !exit {
		return make([]*PetBase, 0)
	}
	return list
}

func init(){
	Load()
}
