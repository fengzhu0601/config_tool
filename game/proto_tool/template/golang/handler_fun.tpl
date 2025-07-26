// $desc
func onClient$fun(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*$pb_name.$req_sturct)
	errCode := handler.OnClient$fun(p, req)
    router.ResponeCS(p,ctx,nil,errCode)
}