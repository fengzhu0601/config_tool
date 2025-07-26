package $package_name

// WARNING: THIS FILE WAS AUTO-GENERATED, PLEASE DO NOT EDIT.

import (
$player_import$router_import
)

// --------------------------------------- handler ----------------------------------

$interface

var handler $handler_name

func RegistHandler(h $handler_name) {
	handler = h
}


// -------------------------------------- 协议号常量 ---------------------------------

$const_proto_recv

$const_proto_send

// ------------------------------------- 客户端消息处理 -------------------------------

$handler_fun


func init() {

	// 注册handler
$regHandler

	// 注册接收协议
	$recvMsgRegist

	// 注册发送协议
	$sendMsgRegist

}

