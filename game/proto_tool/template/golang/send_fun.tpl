// $desc
func Send$name(conn *websocket.Conn, rep *$pb.Rep$name) {
	logger.Debug("Send$name = ", rep)
	message.SendClientMessage(conn, rep)
}