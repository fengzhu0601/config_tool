// $desc
func onRpc$fun(ctx *network.Ctx, info interface{}) {
	req := info.(*$pb_name.$req_sturct)
	errCode := handler.OnRpc$fun(ctx, req)
    router.ResponeRpc(ctx,nil,errCode)
}