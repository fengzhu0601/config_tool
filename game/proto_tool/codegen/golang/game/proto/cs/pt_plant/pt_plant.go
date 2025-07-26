package pt_plant

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_plant"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IPlantHandler interface {
	// 种植成功后会推送 402
	OnClientPlanting(p *player.Player, req *pb_cs_plant.ReqPlanting) error
	// 收获成功后会推送 402
	OnClientHarvest(p *player.Player, req *pb_cs_plant.ReqHarvest) error
	// 解锁后会推送 402
	OnClientUnlock(p *player.Player, req *pb_cs_plant.ReqUnlock) error
}

var handler IPlantHandler

func RegistHandler(h IPlantHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSPlanting uint32 = 411 // 种植成功后会推送 402
	CSHarvest  uint32 = 412 // 收获成功后会推送 402
	CSUnlock   uint32 = 413 // 解锁后会推送 402
)

const(
	SCPlantInfo   uint32 = 401 // 种植系统登录推送
	SCPlantUpdate uint32 = 402 // 种植土地更新
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 种植成功后会推送 402
func onClientPlanting(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_plant.ReqPlanting)
	errCode := handler.OnClientPlanting(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}

// 收获成功后会推送 402
func onClientHarvest(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_plant.ReqHarvest)
	errCode := handler.OnClientHarvest(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}

// 解锁后会推送 402
func onClientUnlock(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_plant.ReqUnlock)
	errCode := handler.OnClientUnlock(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSPlanting, onClientPlanting)
	router.RegistCS(CSHarvest, onClientHarvest)
	router.RegistCS(CSUnlock, onClientUnlock)

	// 注册接收协议
	
	// 种植成功后会推送 402
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSPlanting,
		Type: reflect.TypeOf((*pb_cs_plant.ReqPlanting)(nil)).Elem(),
	})

	// 收获成功后会推送 402
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSHarvest,
		Type: reflect.TypeOf((*pb_cs_plant.ReqHarvest)(nil)).Elem(),
	})

	// 解锁后会推送 402
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSUnlock,
		Type: reflect.TypeOf((*pb_cs_plant.ReqUnlock)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 种植系统登录推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPlantInfo,
		Type: reflect.TypeOf((*pb_cs_plant.RepPlantInfo)(nil)).Elem(),
	})

	// 种植土地更新
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPlantUpdate,
		Type: reflect.TypeOf((*pb_cs_plant.RepPlantUpdate)(nil)).Elem(),
	})


}

