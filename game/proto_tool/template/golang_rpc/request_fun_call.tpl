func $fun(rpcOpt *network.RpcOpt, req *$pb_name.Req$fun) (*$pb_name.Rep$fun,error){
	rep,err := rpc.Call(req, rpcOpt)
	if rep == nil{
		return nil,err
	}
	return rep.(*$pb_name.Rep$fun),err
}

