package pt_role

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_role"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IRoleHandler interface {
	// 设置当前宠物 成功后会推送 611
	OnClientSetCurPet(p *player.Player, req *pb_cs_role.ReqSetCurPet, rep *pb_cs_role.RepSetCurPet) error
}

var handler IRoleHandler

func RegistHandler(h IRoleHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSSetCurPet uint32 = 611 // 设置当前宠物 成功后会推送 611
)

const(
	SCRoleInfo  uint32 = 601 // 英雄信息登录推送/变更推送
	SCSetCurPet uint32 = 611 // 设置当前宠物返回
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 设置当前宠物 成功后会推送 611
func onClientSetCurPet(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_role.ReqSetCurPet)
	rep := &pb_cs_role.RepSetCurPet{}
	errCode := handler.OnClientSetCurPet(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSSetCurPet, onClientSetCurPet)

	// 注册接收协议
	
	// 设置当前宠物 成功后会推送 611
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSSetCurPet,
		Type: reflect.TypeOf((*pb_cs_role.ReqSetCurPet)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 英雄信息登录推送/变更推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCRoleInfo,
		Type: reflect.TypeOf((*pb_cs_role.RepRoleInfo)(nil)).Elem(),
	})

	// 设置当前宠物返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCSetCurPet,
		Type: reflect.TypeOf((*pb_cs_role.RepSetCurPet)(nil)).Elem(),
	})


}

