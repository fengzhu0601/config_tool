package pt_pet

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_pet"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IPetHandler interface {
	// 穿戴服装请求 成功后会推送 1202
	OnClientPutOnClothes(p *player.Player, req *pb_cs_pet.ReqPutOnClothes) error
	// 脱下服装请求 成功后会推送 1202
	OnClientTakeOffClothes(p *player.Player, req *pb_cs_pet.ReqTakeOffClothes) error
	// 喂养宠物 成功后会推送1202
	OnClientFeedPet(p *player.Player, req *pb_cs_pet.ReqFeedPet) error
}

var handler IPetHandler

func RegistHandler(h IPetHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSPutOnClothes   uint32 = 1211 // 穿戴服装请求 成功后会推送 1202
	CSTakeOffClothes uint32 = 1212 // 脱下服装请求 成功后会推送 1202
	CSFeedPet        uint32 = 1213 // 喂养宠物 成功后会推送1202
)

const(
	SCPetInfo      uint32 = 1200 // 宠物信息登录推送
	SCPetUpdate    uint32 = 1201 // 宠物信息变更推送
	SCOnePetUpdate uint32 = 1202 // 单个宠物信息变更推送
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 穿戴服装请求 成功后会推送 1202
func onClientPutOnClothes(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_pet.ReqPutOnClothes)
	errCode := handler.OnClientPutOnClothes(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}

// 脱下服装请求 成功后会推送 1202
func onClientTakeOffClothes(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_pet.ReqTakeOffClothes)
	errCode := handler.OnClientTakeOffClothes(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}

// 喂养宠物 成功后会推送1202
func onClientFeedPet(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_pet.ReqFeedPet)
	errCode := handler.OnClientFeedPet(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSPutOnClothes, onClientPutOnClothes)
	router.RegistCS(CSTakeOffClothes, onClientTakeOffClothes)
	router.RegistCS(CSFeedPet, onClientFeedPet)

	// 注册接收协议
	
	// 穿戴服装请求 成功后会推送 1202
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSPutOnClothes,
		Type: reflect.TypeOf((*pb_cs_pet.ReqPutOnClothes)(nil)).Elem(),
	})

	// 脱下服装请求 成功后会推送 1202
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSTakeOffClothes,
		Type: reflect.TypeOf((*pb_cs_pet.ReqTakeOffClothes)(nil)).Elem(),
	})

	// 喂养宠物 成功后会推送1202
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSFeedPet,
		Type: reflect.TypeOf((*pb_cs_pet.ReqFeedPet)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 宠物信息登录推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPetInfo,
		Type: reflect.TypeOf((*pb_cs_pet.RepPetInfo)(nil)).Elem(),
	})

	// 宠物信息变更推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPetUpdate,
		Type: reflect.TypeOf((*pb_cs_pet.RepPetUpdate)(nil)).Elem(),
	})

	// 单个宠物信息变更推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCOnePetUpdate,
		Type: reflect.TypeOf((*pb_cs_pet.RepOnePetUpdate)(nil)).Elem(),
	})


}

