package rpc_acc

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network"
	"game/network/router"
	"game/network/rpc"
	"game/network/message"
	"game/pb/rpc/pb_rpc_acc"
	"reflect"
)

// --------------------------------------- request ----------------------------------



func GetAcc(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqGetAcc) (*pb_rpc_acc.RepGetAcc,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_acc.RepGetAcc),err
}



func CreateAcc(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqCreateAcc) (*pb_rpc_acc.RepCreateAcc,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_acc.RepCreateAcc),err
}



// acc-server:更新玩家数据
func UpdateAcc(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqUpdateAcc) error{
	return rpc.Cast(req, rpcOpt)
}



func AccQuick(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqAccQuick) (*pb_rpc_acc.RepAccQuick,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_acc.RepAccQuick),err
}



// gateway-server:顶号通知
func KickAccNotic(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqKickAccNotic) error{
	return rpc.Cast(req, rpcOpt)
}



func GetSidAcc(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqGetSidAcc) (*pb_rpc_acc.RepGetSidAcc,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_acc.RepGetSidAcc),err
}



func GetUserAccList(rpcOpt *network.RpcOpt, req *pb_rpc_acc.ReqGetUserAccList) (*pb_rpc_acc.RepGetUserAccList,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_acc.RepGetUserAccList),err
}



// --------------------------------------- handler ----------------------------------

type IAccHandler interface {
	// acc-server:查询sdk账号对应sid
	OnRpcGetAcc(ctx *network.Ctx, req *pb_rpc_acc.ReqGetAcc, rep *pb_rpc_acc.RepGetAcc) error
	// game-server:创建玩家
	OnRpcCreateAcc(ctx *network.Ctx, req *pb_rpc_acc.ReqCreateAcc, rep *pb_rpc_acc.RepCreateAcc) error
	// acc-server:更新玩家数据
	OnRpcUpdateAcc(ctx *network.Ctx, req *pb_rpc_acc.ReqUpdateAcc) error
	// game-server:玩家断开连接
	OnRpcAccQuick(ctx *network.Ctx, req *pb_rpc_acc.ReqAccQuick, rep *pb_rpc_acc.RepAccQuick) error
	// gateway-server:顶号通知
	OnRpcKickAccNotic(ctx *network.Ctx, req *pb_rpc_acc.ReqKickAccNotic) error
	// acc-server:根据Sid获取角色数据
	OnRpcGetSidAcc(ctx *network.Ctx, req *pb_rpc_acc.ReqGetSidAcc, rep *pb_rpc_acc.RepGetSidAcc) error
	// acc-server:根据user获取角色列表
	OnRpcGetUserAccList(ctx *network.Ctx, req *pb_rpc_acc.ReqGetUserAccList, rep *pb_rpc_acc.RepGetUserAccList) error
}

var handler IAccHandler

func RegistHandler(h IAccHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	RpcCSGetAcc         uint32 = 201 // acc-server:查询sdk账号对应sid
	RpcCSCreateAcc      uint32 = 202 // game-server:创建玩家
	RpcCSUpdateAcc      uint32 = 203 // acc-server:更新玩家数据
	RpcCSAccQuick       uint32 = 204 // game-server:玩家断开连接
	RpcCSKickAccNotic   uint32 = 205 // gateway-server:顶号通知
	RpcCSGetSidAcc      uint32 = 206 // acc-server:根据Sid获取角色数据
	RpcCSGetUserAccList uint32 = 207 // acc-server:根据user获取角色列表
)

const(
	RpcSCGetAcc         uint32 = 201 // acc-server:查询sdk账号对应sid
	RpcSCCreateAcc      uint32 = 202 // game-server:创建玩家
	RpcSCAccQuick       uint32 = 204 // game-server:玩家断开连接
	RpcSCGetSidAcc      uint32 = 206 // acc-server:根据Sid获取角色数据
	RpcSCGetUserAccList uint32 = 207 // acc-server:根据user获取角色列表
)

// ------------------------------------- 客户端消息处理 -------------------------------



// acc-server:查询sdk账号对应sid
func onRpcGetAcc(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqGetAcc)
	rep := &pb_rpc_acc.RepGetAcc{}
	errCode := handler.OnRpcGetAcc(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// game-server:创建玩家
func onRpcCreateAcc(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqCreateAcc)
	rep := &pb_rpc_acc.RepCreateAcc{}
	errCode := handler.OnRpcCreateAcc(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// acc-server:更新玩家数据
func onRpcUpdateAcc(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqUpdateAcc)
	errCode := handler.OnRpcUpdateAcc(ctx, req)
    router.ResponeRpc(ctx,nil,errCode)
}

// game-server:玩家断开连接
func onRpcAccQuick(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqAccQuick)
	rep := &pb_rpc_acc.RepAccQuick{}
	errCode := handler.OnRpcAccQuick(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// gateway-server:顶号通知
func onRpcKickAccNotic(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqKickAccNotic)
	errCode := handler.OnRpcKickAccNotic(ctx, req)
    router.ResponeRpc(ctx,nil,errCode)
}

// acc-server:根据Sid获取角色数据
func onRpcGetSidAcc(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqGetSidAcc)
	rep := &pb_rpc_acc.RepGetSidAcc{}
	errCode := handler.OnRpcGetSidAcc(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// acc-server:根据user获取角色列表
func onRpcGetUserAccList(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_acc.ReqGetUserAccList)
	rep := &pb_rpc_acc.RepGetUserAccList{}
	errCode := handler.OnRpcGetUserAccList(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistRpc(RpcCSGetAcc, onRpcGetAcc)
	router.RegistRpc(RpcCSCreateAcc, onRpcCreateAcc)
	router.RegistRpc(RpcCSUpdateAcc, onRpcUpdateAcc)
	router.RegistRpc(RpcCSAccQuick, onRpcAccQuick)
	router.RegistRpc(RpcCSKickAccNotic, onRpcKickAccNotic)
	router.RegistRpc(RpcCSGetSidAcc, onRpcGetSidAcc)
	router.RegistRpc(RpcCSGetUserAccList, onRpcGetUserAccList)

	// 注册接收协议
	
	// acc-server:查询sdk账号对应sid
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSGetAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqGetAcc)(nil)).Elem(),
	})

	// game-server:创建玩家
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSCreateAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqCreateAcc)(nil)).Elem(),
	})

	// acc-server:更新玩家数据
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSUpdateAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqUpdateAcc)(nil)).Elem(),
	})

	// game-server:玩家断开连接
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSAccQuick,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqAccQuick)(nil)).Elem(),
	})

	// gateway-server:顶号通知
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSKickAccNotic,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqKickAccNotic)(nil)).Elem(),
	})

	// acc-server:根据Sid获取角色数据
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSGetSidAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqGetSidAcc)(nil)).Elem(),
	})

	// acc-server:根据user获取角色列表
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSGetUserAccList,
		Type: reflect.TypeOf((*pb_rpc_acc.ReqGetUserAccList)(nil)).Elem(),
	})


	// 注册发送协议
	
	// acc-server:查询sdk账号对应sid
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCGetAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.RepGetAcc)(nil)).Elem(),
	})

	// game-server:创建玩家
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCCreateAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.RepCreateAcc)(nil)).Elem(),
	})

	// game-server:玩家断开连接
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCAccQuick,
		Type: reflect.TypeOf((*pb_rpc_acc.RepAccQuick)(nil)).Elem(),
	})

	// acc-server:根据Sid获取角色数据
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCGetSidAcc,
		Type: reflect.TypeOf((*pb_rpc_acc.RepGetSidAcc)(nil)).Elem(),
	})

	// acc-server:根据user获取角色列表
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCGetUserAccList,
		Type: reflect.TypeOf((*pb_rpc_acc.RepGetUserAccList)(nil)).Elem(),
	})


}

