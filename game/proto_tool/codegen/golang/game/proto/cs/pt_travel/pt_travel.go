package pt_travel

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_travel"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type ITravelHandler interface {
	// 领取旅行奖励
	OnClientGetReward(p *player.Player, req *pb_cs_travel.ReqGetReward) error
}

var handler ITravelHandler

func RegistHandler(h ITravelHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSGetReward uint32 = 451 // 领取旅行奖励
)

const(
	SCTravelInfo   uint32 = 461 // 旅行系统登录推送
	SCTravelUpdate uint32 = 462 // 旅行更新
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 领取旅行奖励
func onClientGetReward(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_travel.ReqGetReward)
	errCode := handler.OnClientGetReward(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSGetReward, onClientGetReward)

	// 注册接收协议
	
	// 领取旅行奖励
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSGetReward,
		Type: reflect.TypeOf((*pb_cs_travel.ReqGetReward)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 旅行系统登录推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCTravelInfo,
		Type: reflect.TypeOf((*pb_cs_travel.RepTravelInfo)(nil)).Elem(),
	})

	// 旅行更新
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCTravelUpdate,
		Type: reflect.TypeOf((*pb_cs_travel.RepTravelUpdate)(nil)).Elem(),
	})


}

