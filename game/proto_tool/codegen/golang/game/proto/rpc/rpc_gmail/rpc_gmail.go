package rpc_gmail

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/network"
	"game/network/router"
	"game/network/rpc"
	"game/network/message"
	"game/pb/rpc/pb_rpc_gmail"
	"reflect"
)

// --------------------------------------- request ----------------------------------



func SendGmail(rpcOpt *network.RpcOpt, req *pb_rpc_gmail.ReqSendGmail) (*pb_rpc_gmail.RepSendGmail,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_gmail.RepSendGmail),err
}



func SendUserMail(rpcOpt *network.RpcOpt, req *pb_rpc_gmail.ReqSendUserMail) (*pb_rpc_gmail.RepSendUserMail,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*pb_rpc_gmail.RepSendUserMail),err
}



// --------------------------------------- handler ----------------------------------

type IGmailHandler interface {
	// 发送全局邮件
	OnRpcSendGmail(ctx *network.Ctx, req *pb_rpc_gmail.ReqSendGmail, rep *pb_rpc_gmail.RepSendGmail) error
	// 发送个人邮件
	OnRpcSendUserMail(ctx *network.Ctx, req *pb_rpc_gmail.ReqSendUserMail, rep *pb_rpc_gmail.RepSendUserMail) error
}

var handler IGmailHandler

func RegistHandler(h IGmailHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	RpcCSSendGmail    uint32 = 301 // 发送全局邮件
	RpcCSSendUserMail uint32 = 302 // 发送个人邮件
)

const(
	RpcSCSendGmail    uint32 = 301 // 发送全局邮件返回
	RpcSCSendUserMail uint32 = 302 // 发送个人邮件
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 发送全局邮件
func onRpcSendGmail(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_gmail.ReqSendGmail)
	rep := &pb_rpc_gmail.RepSendGmail{}
	errCode := handler.OnRpcSendGmail(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}

// 发送个人邮件
func onRpcSendUserMail(ctx *network.Ctx, info interface{}) {
	req := info.(*pb_rpc_gmail.ReqSendUserMail)
	rep := &pb_rpc_gmail.RepSendUserMail{}
	errCode := handler.OnRpcSendUserMail(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistRpc(RpcCSSendGmail, onRpcSendGmail)
	router.RegistRpc(RpcCSSendUserMail, onRpcSendUserMail)

	// 注册接收协议
	
	// 发送全局邮件
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSSendGmail,
		Type: reflect.TypeOf((*pb_rpc_gmail.ReqSendGmail)(nil)).Elem(),
	})

	// 发送个人邮件
	message.RpcReqRegist(&message.MsgMeta{
		Cmd:   RpcCSSendUserMail,
		Type: reflect.TypeOf((*pb_rpc_gmail.ReqSendUserMail)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 发送全局邮件返回
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCSendGmail,
		Type: reflect.TypeOf((*pb_rpc_gmail.RepSendGmail)(nil)).Elem(),
	})

	// 发送个人邮件
	message.RpcRepRegist(&message.MsgMeta{
		Cmd:   RpcSCSendUserMail,
		Type: reflect.TypeOf((*pb_rpc_gmail.RepSendUserMail)(nil)).Elem(),
	})


}

