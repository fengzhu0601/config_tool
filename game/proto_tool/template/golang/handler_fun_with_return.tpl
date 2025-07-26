// $desc
func onClient$fun(p *player.Player, ctx *network.Ctx, info interface{}) {
	req := info.(*$pb_name.$req_sturct)
	rep := $rep
	errCode := handler.OnClient$fun(p, req, rep)
    router.ResponeCS(p,ctx,rep,errCode)
}