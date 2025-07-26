package pt_account

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_account"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IAccountHandler interface {
	// 请求随机名字和改名消耗
	OnClientRandomName(p *player.Player, req *pb_cs_account.ReqRandomName, rep *pb_cs_account.RepRandomName) error
	// 玩家改名
	OnClientChangeName(p *player.Player, req *pb_cs_account.ReqChangeName, rep *pb_cs_account.RepChangeName) error
	// 输入兑换码
	OnClientGiftCode(p *player.Player, req *pb_cs_account.ReqGiftCode, rep *pb_cs_account.RepGiftCode) error
	// 反馈
	OnClientFeedBack(p *player.Player, req *pb_cs_account.ReqFeedBack, rep *pb_cs_account.RepFeedBack) error
}

var handler IAccountHandler

func RegistHandler(h IAccountHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSRandomName uint32 = 203 // 请求随机名字和改名消耗
	CSChangeName uint32 = 204 // 玩家改名
	CSGiftCode   uint32 = 206 // 输入兑换码
	CSFeedBack   uint32 = 207 // 反馈
)

const(
	SCPlayerInfo uint32 = 201 // 账号信息登录推送(必要协议都发完才发这个，接着会发非必要的协议)
	SCRandomName uint32 = 203 // 返回一个随机名字和改名消耗
	SCChangeName uint32 = 204 // 玩家改名成功返回
	SCLevelUp    uint32 = 205 // 玩家等级变化,或者经验变化推送
	SCGiftCode   uint32 = 206 // 兑换码返回
	SCFeedBack   uint32 = 207 // 反馈成功返回
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 请求随机名字和改名消耗
func onClientRandomName(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_account.ReqRandomName)
	rep := &pb_cs_account.RepRandomName{}
	errCode := handler.OnClientRandomName(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// 玩家改名
func onClientChangeName(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_account.ReqChangeName)
	rep := &pb_cs_account.RepChangeName{}
	errCode := handler.OnClientChangeName(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// 输入兑换码
func onClientGiftCode(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_account.ReqGiftCode)
	rep := &pb_cs_account.RepGiftCode{}
	errCode := handler.OnClientGiftCode(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// 反馈
func onClientFeedBack(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_account.ReqFeedBack)
	rep := &pb_cs_account.RepFeedBack{}
	errCode := handler.OnClientFeedBack(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSRandomName, onClientRandomName)
	router.RegistCS(CSChangeName, onClientChangeName)
	router.RegistCS(CSGiftCode, onClientGiftCode)
	router.RegistCS(CSFeedBack, onClientFeedBack)

	// 注册接收协议
	
	// 请求随机名字和改名消耗
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSRandomName,
		Type: reflect.TypeOf((*pb_cs_account.ReqRandomName)(nil)).Elem(),
	})

	// 玩家改名
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSChangeName,
		Type: reflect.TypeOf((*pb_cs_account.ReqChangeName)(nil)).Elem(),
	})

	// 输入兑换码
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSGiftCode,
		Type: reflect.TypeOf((*pb_cs_account.ReqGiftCode)(nil)).Elem(),
	})

	// 反馈
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSFeedBack,
		Type: reflect.TypeOf((*pb_cs_account.ReqFeedBack)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 账号信息登录推送(必要协议都发完才发这个，接着会发非必要的协议)
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPlayerInfo,
		Type: reflect.TypeOf((*pb_cs_account.RepPlayerInfo)(nil)).Elem(),
	})

	// 返回一个随机名字和改名消耗
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCRandomName,
		Type: reflect.TypeOf((*pb_cs_account.RepRandomName)(nil)).Elem(),
	})

	// 玩家改名成功返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCChangeName,
		Type: reflect.TypeOf((*pb_cs_account.RepChangeName)(nil)).Elem(),
	})

	// 玩家等级变化,或者经验变化推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCLevelUp,
		Type: reflect.TypeOf((*pb_cs_account.RepLevelUp)(nil)).Elem(),
	})

	// 兑换码返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCGiftCode,
		Type: reflect.TypeOf((*pb_cs_account.RepGiftCode)(nil)).Elem(),
	})

	// 反馈成功返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCFeedBack,
		Type: reflect.TypeOf((*pb_cs_account.RepFeedBack)(nil)).Elem(),
	})


}

