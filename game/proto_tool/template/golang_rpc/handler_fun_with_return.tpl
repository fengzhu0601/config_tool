// $desc
func onRpc$fun(ctx *network.Ctx, info interface{}) {
	req := info.(*$pb_name.$req_sturct)
	rep := $rep
	errCode := handler.OnRpc$fun(ctx, req, rep)
    router.ResponeRpc(ctx,rep,errCode)
}