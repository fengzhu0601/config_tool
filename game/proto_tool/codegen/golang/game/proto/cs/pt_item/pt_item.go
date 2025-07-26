package pt_item

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (

	"game/game_server/player"
	"game/network"
	"game/network/router"
	"game/network/message"
	"game/pb/cs/pb_cs_item"
	"reflect"
)

// --------------------------------------- handler ----------------------------------

type IItemHandler interface {
	// 使用物品
	OnClientUseItem(p *player.Player, req *pb_cs_item.ReqUseItem, rep *pb_cs_item.RepUseItem) error
}

var handler IItemHandler

func RegistHandler(h IItemHandler) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

const(
	CSUseItem uint32 = 502 // 使用物品
)

const(
	SCAllItems    uint32 = 500 // 物品信息登录批量推送
	SCUpdateItems uint32 = 501 // 物品增量更新
	SCUseItem     uint32 = 502 // 使用物品返回
)

// ------------------------------------- 客户端消息处理 -------------------------------



// 使用物品
func onClientUseItem(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*pb_cs_item.ReqUseItem)
	rep := &pb_cs_item.RepUseItem{}
	errCode := handler.OnClientUseItem(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}


func init() {

	// 注册handler
	router.RegistCS(CSUseItem, onClientUseItem)

	// 注册接收协议
	
	// 使用物品
	message.CSReqRegist(&message.MsgMeta{
		Cmd:   CSUseItem,
		Type: reflect.TypeOf((*pb_cs_item.ReqUseItem)(nil)).Elem(),
	})


	// 注册发送协议
	
	// 物品信息登录批量推送
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCAllItems,
		Type: reflect.TypeOf((*pb_cs_item.RepAllItems)(nil)).Elem(),
	})

	// 物品增量更新
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCUpdateItems,
		Type: reflect.TypeOf((*pb_cs_item.RepUpdateItems)(nil)).Elem(),
	})

	// 使用物品返回
	message.CSRepRegist(&message.MsgMeta{
		Cmd:   SCUseItem,
		Type: reflect.TypeOf((*pb_cs_item.RepUseItem)(nil)).Elem(),
	})


}

