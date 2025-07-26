package rpc_gm

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network"
	"game/network/router"
	"game/network/rpc"
	"game/network/message"
	"game/pb/rpc/pb_rpc_gm"
	"reflect"
)

// --------------------------------------- request ----------------------------------



func GmUpdate(rpcOpt *network.RpcOpt, req *pb_rpc_gm.ReqGmUpdate) (*pb_rpc_gm.RepGmUpdate,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_gm.RepGmUpdate),err
}



func AccReport(rpcOpt *network.RpcOpt, req *pb_rpc_gm.ReqAccReport) (*pb_rpc_gm.RepAccReport,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_gm.RepAccReport),err
}



// --------------------------------------- handler ----------------------------------

type IGmHandler interface {
	// gm信息更新:acc
	OnRpcGmUpdate(ctx *network.Ctx, req *pb_rpc_gm.ReqGmUpdate, rep *pb_rpc_gm.RepGmUpdate) error
	// 账号信息更新:acc
	OnRpcAccReport(ctx *network.Ctx, req *pb_rpc_gm.ReqAccReport, rep *pb_rpc_gm.RepAccReport) error
}

var handler IGmHandler

func RegistHandler(h IGmHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	RpcCSGmUpdate  uint32 = 401 // gm信息更新:acc
	RpcCSAccReport uint32 = 402 // 账号信息更新:acc
)

const(
	RpcSCGmUpdate  uint32 = 401 // gm信息更新返回
	RpcSCAccReport uint32 = 402 // 账号信息更新:acc
)

// ------------------------------------- 客户端消息处理 -------------------------------



// gm信息更新:acc
func onRpcGmUpdate(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_gm.ReqGmUpdate)
	rep := &pb_rpc_gm.RepGmUpdate{}
	errCode := handler.OnRpcGmUpdate(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// 账号信息更新:acc
func onRpcAccReport(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_gm.ReqAccReport)
	rep := &pb_rpc_gm.RepAccReport{}
	errCode := handler.OnRpcAccReport(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistRpc(RpcCSGmUpdate, onRpcGmUpdate)
	router.RegistRpc(RpcCSAccReport, onRpcAccReport)

	// 注册接收协议
	
	// gm信息更新:acc
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSGmUpdate,
		Type: reflect.TypeOf((*pb_rpc_gm.ReqGmUpdate)(nil)).Elem(),
	})

	// 账号信息更新:acc
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSAccReport,
		Type: reflect.TypeOf((*pb_rpc_gm.ReqAccReport)(nil)).Elem(),
	})


	// 注册发送协议
	
	// gm信息更新返回
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCGmUpdate,
		Type: reflect.TypeOf((*pb_rpc_gm.RepGmUpdate)(nil)).Elem(),
	})

	// 账号信息更新:acc
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCAccReport,
		Type: reflect.TypeOf((*pb_rpc_gm.RepAccReport)(nil)).Elem(),
	})


}

