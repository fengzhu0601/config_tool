	// $desc
	message.$method(&message.MsgMeta{
		Cmd:   $cmd,
		Type: reflect.TypeOf((*$pb.$struct)(nil)).Elem(),
	})
