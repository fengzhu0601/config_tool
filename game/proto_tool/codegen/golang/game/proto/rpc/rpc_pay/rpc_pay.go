package rpc_pay

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network"
	"game/network/router"
	"game/network/rpc"
	"game/network/message"
	"game/pb/rpc/pb_rpc_pay"
	"reflect"
)

// --------------------------------------- request ----------------------------------



func PayBack(rpcOpt *network.RpcOpt, req *pb_rpc_pay.ReqPayBack) (*pb_rpc_pay.RepPayBack,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_pay.RepPayBack),err
}



// --------------------------------------- handler ----------------------------------

type IPayHandler interface {
	// 发货请求
	OnRpcPayBack(ctx *network.Ctx, req *pb_rpc_pay.ReqPayBack, rep *pb_rpc_pay.RepPayBack) error
}

var handler IPayHandler

func RegistHandler(h IPayHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	RpcCSPayBack uint32 = 501 // 发货请求
)

const(
	RpcSCPayBack uint32 = 501 // 发货成功返回
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 发货请求
func onRpcPayBack(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_pay.ReqPayBack)
	rep := &pb_rpc_pay.RepPayBack{}
	errCode := handler.OnRpcPayBack(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistRpc(RpcCSPayBack, onRpcPayBack)

	// 注册接收协议
	
	// 发货请求
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSPayBack,
		Type: reflect.TypeOf((*pb_rpc_pay.ReqPayBack)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 发货成功返回
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCPayBack,
		Type: reflect.TypeOf((*pb_rpc_pay.RepPayBack)(nil)).Elem(),
	})


}

