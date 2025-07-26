package pt_reward

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network/message"
	"game/pb/cs/pb_cs_reward"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IRewardHandler interface {
}

var handler IRewardHandler

func RegistHandler(h IRewardHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------



const(
	SCShowRewards uint32 = 150 // 奖励弹窗
)

// ------------------------------------- 客户端消息处理 -------------------------------




func init() {

	// 注册handler


	// 注册接收协议
	

	// 注册发送协议
	
	// 奖励弹窗
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCShowRewards,
		Type: reflect.TypeOf((*pb_cs_reward.RepShowRewards)(nil)).Elem(),
	})


}

