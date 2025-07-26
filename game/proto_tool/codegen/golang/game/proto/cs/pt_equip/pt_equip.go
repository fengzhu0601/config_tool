package pt_equip

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network/message"
	"game/pb/cs/pb_cs_equip"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IEquipHandler interface {
}

var handler IEquipHandler

func RegistHandler(h IEquipHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------



const(
	SCAllEquips    uint32 = 800 // 装备信息登录批量推送
	SCUpdateEquips uint32 = 801 // 装备更新
	SCDelEquips    uint32 = 802 // 装备删除
)

// ------------------------------------- 客户端消息处理 -------------------------------




func init() {

	// 注册handler


	// 注册接收协议
	

	// 注册发送协议
	
	// 装备信息登录批量推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCAllEquips,
		Type: reflect.TypeOf((*pb_cs_equip.RepAllEquips)(nil)).Elem(),
	})

	// 装备更新
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCUpdateEquips,
		Type: reflect.TypeOf((*pb_cs_equip.RepUpdateEquips)(nil)).Elem(),
	})

	// 装备删除
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCDelEquips,
		Type: reflect.TypeOf((*pb_cs_equip.RepDelEquips)(nil)).Elem(),
	})


}

