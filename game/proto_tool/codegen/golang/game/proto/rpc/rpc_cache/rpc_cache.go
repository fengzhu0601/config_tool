package rpc_cache

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network"
	"game/network/router"
	"game/network/rpc"
	"game/network/message"
	"game/pb/rpc/pb_rpc_cache"
	"reflect"
)

// --------------------------------------- request ----------------------------------



func CacheLookup(rpcOpt *network.RpcOpt, req *pb_rpc_cache.ReqCacheLookup) (*pb_rpc_cache.RepCacheLookup,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_cache.RepCacheLookup),err
}



// --------------------------------------- handler ----------------------------------

type ICacheHandler interface {
	// cache查找
	OnRpcCacheLookup(ctx *network.Ctx, req *pb_rpc_cache.ReqCacheLookup, rep *pb_rpc_cache.RepCacheLookup) error
}

var handler ICacheHandler

func RegistHandler(h ICacheHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	RpcCSCacheLookup uint32 = 101 // cache查找
)

const(
	RpcSCCacheLookup uint32 = 101 // cache查找返回
)

// ------------------------------------- 客户端消息处理 -------------------------------



// cache查找
func onRpcCacheLookup(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_cache.ReqCacheLookup)
	rep := &pb_rpc_cache.RepCacheLookup{}
	errCode := handler.OnRpcCacheLookup(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistRpc(RpcCSCacheLookup, onRpcCacheLookup)

	// 注册接收协议
	
	// cache查找
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSCacheLookup,
		Type: reflect.TypeOf((*pb_rpc_cache.ReqCacheLookup)(nil)).Elem(),
	})


	// 注册发送协议
	
	// cache查找返回
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCCacheLookup,
		Type: reflect.TypeOf((*pb_rpc_cache.RepCacheLookup)(nil)).Elem(),
	})


}

