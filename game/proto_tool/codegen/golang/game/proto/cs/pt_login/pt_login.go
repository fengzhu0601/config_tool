package pt_login

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_login"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type ILoginHandler interface {
	// 登陆
	OnClientLogin(p *player.Player, req *pb_cs_login.ReqLogin, rep *pb_cs_login.RepLoginResult) error
	// ping同步时间
	OnClientPing(p *player.Player, req *pb_cs_login.ReqPing, rep *pb_cs_login.RepPong) error
	// 断线重连(上次离线后n小时内可用,绕过sdk登陆)
	OnClientReconnect(p *player.Player, req *pb_cs_login.ReqReconnect) error
	// 网关服请求初始化player
	OnClientGateInitPlayer(p *player.Player, req *pb_cs_login.ReqGateInitPlayer, rep *pb_cs_login.RepGateInitPlayer) error
	// 客户端通知修改数据
	OnClientClientUpdateAccount(p *player.Player, req *pb_cs_login.ReqClientUpdateAccount) error
}

var handler ILoginHandler

func RegistHandler(h ILoginHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSLogin               uint32 = 100 // 登陆
	CSPing                uint32 = 101 // ping同步时间
	CSReconnect           uint32 = 102 // 断线重连(上次离线后n小时内可用,绕过sdk登陆)
	CSGateInitPlayer      uint32 = 106 // 网关服请求初始化player
	CSClientUpdateAccount uint32 = 107 // 客户端通知修改数据
)

const(
	SCLoginResult     uint32 = 100 // 登陆返回
	SCPong            uint32 = 101 // pong同步时间
	SCLoginInfoFinish uint32 = 104 // 所有登陆协议发放完成通知
	SCGateInitPlayer  uint32 = 106 // 网关服请求初始化player
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 登陆
func onClientLogin(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_login.ReqLogin)
	rep := &pb_cs_login.RepLoginResult{}
	errCode := handler.OnClientLogin(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// ping同步时间
func onClientPing(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_login.ReqPing)
	rep := &pb_cs_login.RepPong{}
	errCode := handler.OnClientPing(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// 断线重连(上次离线后n小时内可用,绕过sdk登陆)
func onClientReconnect(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_login.ReqReconnect)
	errCode := handler.OnClientReconnect(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}

// 网关服请求初始化player
func onClientGateInitPlayer(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_login.ReqGateInitPlayer)
	rep := &pb_cs_login.RepGateInitPlayer{}
	errCode := handler.OnClientGateInitPlayer(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}

// 客户端通知修改数据
func onClientClientUpdateAccount(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_login.ReqClientUpdateAccount)
	errCode := handler.OnClientClientUpdateAccount(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSLogin, onClientLogin)
	router.RegistCS(CSPing, onClientPing)
	router.RegistCS(CSReconnect, onClientReconnect)
	router.RegistCS(CSGateInitPlayer, onClientGateInitPlayer)
	router.RegistCS(CSClientUpdateAccount, onClientClientUpdateAccount)

	// 注册接收协议
	
	// 登陆
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSLogin,
		Type: reflect.TypeOf((*pb_cs_login.ReqLogin)(nil)).Elem(),
	})

	// ping同步时间
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSPing,
		Type: reflect.TypeOf((*pb_cs_login.ReqPing)(nil)).Elem(),
	})

	// 断线重连(上次离线后n小时内可用,绕过sdk登陆)
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSReconnect,
		Type: reflect.TypeOf((*pb_cs_login.ReqReconnect)(nil)).Elem(),
	})

	// 网关服请求初始化player
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSGateInitPlayer,
		Type: reflect.TypeOf((*pb_cs_login.ReqGateInitPlayer)(nil)).Elem(),
	})

	// 客户端通知修改数据
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSClientUpdateAccount,
		Type: reflect.TypeOf((*pb_cs_login.ReqClientUpdateAccount)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 登陆返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCLoginResult,
		Type: reflect.TypeOf((*pb_cs_login.RepLoginResult)(nil)).Elem(),
	})

	// pong同步时间
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCPong,
		Type: reflect.TypeOf((*pb_cs_login.RepPong)(nil)).Elem(),
	})

	// 所有登陆协议发放完成通知
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCLoginInfoFinish,
		Type: reflect.TypeOf((*pb_cs_login.RepLoginInfoFinish)(nil)).Elem(),
	})

	// 网关服请求初始化player
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCGateInitPlayer,
		Type: reflect.TypeOf((*pb_cs_login.RepGateInitPlayer)(nil)).Elem(),
	})


}

