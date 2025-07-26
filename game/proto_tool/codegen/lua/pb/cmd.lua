local Items=
{
	request=
	{
		[1211] = {message='pb_cs_pet.ReqPutOnClothes',pb='pb_cs_pet.pb'},
		[1212] = {message='pb_cs_pet.ReqTakeOffClothes',pb='pb_cs_pet.pb'},
		[1213] = {message='pb_cs_pet.ReqFeedPet',pb='pb_cs_pet.pb'},
		[451] = {message='pb_cs_travel.ReqGetReward',pb='pb_cs_travel.pb'},
		[100] = {message='pb_cs_login.ReqLogin',pb='pb_cs_login.pb'},
		[101] = {message='pb_cs_login.ReqPing',pb='pb_cs_login.pb'},
		[102] = {message='pb_cs_login.ReqReconnect',pb='pb_cs_login.pb'},
		[106] = {message='pb_cs_login.ReqGateInitPlayer',pb='pb_cs_login.pb'},
		[107] = {message='pb_cs_login.ReqClientUpdateAccount',pb='pb_cs_login.pb'},
		[411] = {message='pb_cs_plant.ReqPlanting',pb='pb_cs_plant.pb'},
		[412] = {message='pb_cs_plant.ReqHarvest',pb='pb_cs_plant.pb'},
		[413] = {message='pb_cs_plant.ReqUnlock',pb='pb_cs_plant.pb'},
		[502] = {message='pb_cs_item.ReqUseItem',pb='pb_cs_item.pb'},
		[611] = {message='pb_cs_role.ReqSetCurPet',pb='pb_cs_role.pb'},
		[203] = {message='pb_cs_account.ReqRandomName',pb='pb_cs_account.pb'},
		[204] = {message='pb_cs_account.ReqChangeName',pb='pb_cs_account.pb'},
		[206] = {message='pb_cs_account.ReqGiftCode',pb='pb_cs_account.pb'},
		[207] = {message='pb_cs_account.ReqFeedBack',pb='pb_cs_account.pb'},
	},
	response=
	{
		[1] = {message='pb_cs_error.RepError',pb='pb_cs_error.pb'},
		[1200] = {message='pb_cs_pet.RepPetInfo',pb='pb_cs_pet.pb'},
		[1201] = {message='pb_cs_pet.RepPetUpdate',pb='pb_cs_pet.pb'},
		[1202] = {message='pb_cs_pet.RepOnePetUpdate',pb='pb_cs_pet.pb'},
		[461] = {message='pb_cs_travel.RepTravelInfo',pb='pb_cs_travel.pb'},
		[462] = {message='pb_cs_travel.RepTravelUpdate',pb='pb_cs_travel.pb'},
		[100] = {message='pb_cs_login.RepLoginResult',pb='pb_cs_login.pb'},
		[101] = {message='pb_cs_login.RepPong',pb='pb_cs_login.pb'},
		[104] = {message='pb_cs_login.RepLoginInfoFinish',pb='pb_cs_login.pb'},
		[106] = {message='pb_cs_login.RepGateInitPlayer',pb='pb_cs_login.pb'},
		[150] = {message='pb_cs_reward.RepShowRewards',pb='pb_cs_reward.pb'},
		[401] = {message='pb_cs_plant.RepPlantInfo',pb='pb_cs_plant.pb'},
		[402] = {message='pb_cs_plant.RepPlantUpdate',pb='pb_cs_plant.pb'},
		[800] = {message='pb_cs_equip.RepAllEquips',pb='pb_cs_equip.pb'},
		[801] = {message='pb_cs_equip.RepUpdateEquips',pb='pb_cs_equip.pb'},
		[802] = {message='pb_cs_equip.RepDelEquips',pb='pb_cs_equip.pb'},
		[500] = {message='pb_cs_item.RepAllItems',pb='pb_cs_item.pb'},
		[501] = {message='pb_cs_item.RepUpdateItems',pb='pb_cs_item.pb'},
		[502] = {message='pb_cs_item.RepUseItem',pb='pb_cs_item.pb'},
		[601] = {message='pb_cs_role.RepRoleInfo',pb='pb_cs_role.pb'},
		[611] = {message='pb_cs_role.RepSetCurPet',pb='pb_cs_role.pb'},
		[201] = {message='pb_cs_account.RepPlayerInfo',pb='pb_cs_account.pb'},
		[203] = {message='pb_cs_account.RepRandomName',pb='pb_cs_account.pb'},
		[204] = {message='pb_cs_account.RepChangeName',pb='pb_cs_account.pb'},
		[205] = {message='pb_cs_account.RepLevelUp',pb='pb_cs_account.pb'},
		[206] = {message='pb_cs_account.RepGiftCode',pb='pb_cs_account.pb'},
		[207] = {message='pb_cs_account.RepFeedBack',pb='pb_cs_account.pb'},
	},
	pbList=
	{
		'pb_cs_error.pb',
		'pb_cs_pet.pb',
		'pb_cs_travel.pb',
		'pb_cs_login.pb',
		'pb_cs_reward.pb',
		'pb_cs_plant.pb',
		'pb_cs_equip.pb',
		'pb_cs_item.pb',
		'pb_cs_role.pb',
		'pb_cs_account.pb',
	},
}
pb_ReqID = 
{
	--登陆
	Login_ReqLogin = 100,
	--ping同步时间
	Login_ReqPing = 101,
	--断线重连(上次离线后n小时内可用,绕过sdk登陆)
	Login_ReqReconnect = 102,
	--网关服请求初始化player
	Login_ReqGateInitPlayer = 106,
	--客户端通知修改数据
	Login_ReqClientUpdateAccount = 107,
	--请求随机名字和改名消耗
	Account_ReqRandomName = 203,
	--玩家改名
	Account_ReqChangeName = 204,
	--输入兑换码
	Account_ReqGiftCode = 206,
	--反馈
	Account_ReqFeedBack = 207,
	--种植成功后会推送 402
	Plant_ReqPlanting = 411,
	--收获成功后会推送 402
	Plant_ReqHarvest = 412,
	--解锁后会推送 402
	Plant_ReqUnlock = 413,
	--领取旅行奖励
	Travel_ReqGetReward = 451,
	--使用物品
	Item_ReqUseItem = 502,
	--设置当前宠物 成功后会推送 611
	Role_ReqSetCurPet = 611,
	--穿戴服装请求 成功后会推送 1202
	Pet_ReqPutOnClothes = 1211,
	--脱下服装请求 成功后会推送 1202
	Pet_ReqTakeOffClothes = 1212,
	--喂养宠物 成功后会推送1202
	Pet_ReqFeedPet = 1213,
}
pb_ResID = 
{
	--错误码提示
	Error_RepError = 1,
	--登陆返回
	Login_RepLoginResult = 100,
	--pong同步时间
	Login_RepPong = 101,
	--所有登陆协议发放完成通知
	Login_RepLoginInfoFinish = 104,
	--网关服请求初始化player
	Login_RepGateInitPlayer = 106,
	--奖励弹窗
	Reward_RepShowRewards = 150,
	--账号信息登录推送(必要协议都发完才发这个，接着会发非必要的协议)
	Account_RepPlayerInfo = 201,
	--返回一个随机名字和改名消耗
	Account_RepRandomName = 203,
	--玩家改名成功返回
	Account_RepChangeName = 204,
	--玩家等级变化,或者经验变化推送
	Account_RepLevelUp = 205,
	--兑换码返回
	Account_RepGiftCode = 206,
	--反馈成功返回
	Account_RepFeedBack = 207,
	--种植系统登录推送
	Plant_RepPlantInfo = 401,
	--种植土地更新
	Plant_RepPlantUpdate = 402,
	--旅行系统登录推送
	Travel_RepTravelInfo = 461,
	--旅行更新
	Travel_RepTravelUpdate = 462,
	--物品信息登录批量推送
	Item_RepAllItems = 500,
	--物品增量更新
	Item_RepUpdateItems = 501,
	--使用物品返回
	Item_RepUseItem = 502,
	--英雄信息登录推送/变更推送
	Role_RepRoleInfo = 601,
	--设置当前宠物返回
	Role_RepSetCurPet = 611,
	--装备信息登录批量推送
	Equip_RepAllEquips = 800,
	--装备更新
	Equip_RepUpdateEquips = 801,
	--装备删除
	Equip_RepDelEquips = 802,
	--宠物信息登录推送
	Pet_RepPetInfo = 1200,
	--宠物信息变更推送
	Pet_RepPetUpdate = 1201,
	--单个宠物信息变更推送
	Pet_RepOnePetUpdate = 1202,
}
--错误码,前1000给服务器内部用
pb_Error_ECode = 
{
	ServerNotExit = 0,--服务器不存在
	ServerNotConn = 1,--服务器未连接
	RpcTimeout = 2,--rpc访问超时
	RpcServerError = 3,--目标服发生错误
	RpcLocalNotRegist = 4,--本地Rpc消息没注册
	RpcNotRegist = 5,--远程Rpc消息没注册
	RpcAccExit = 6,--角色已存在，无法创建角色
	ServerWorkerNotExit = 7,--进程不存在
	ServerCantFind = 8,--没有可用服务器
	ServerAccNotExit = 9,--角色不存在
	ServerError = 1001,--服务器内部错误:%1s
	MsgError = 1002,--未定义cmd:%1i
	NameEmptyError = 1003,--昵称为空
	NameInvalidLenError = 1004,--无效的昵称长度
	NameInvalidError = 1005,--昵称存在非法字符
	NameUsedError = 1006,--该昵称已被使用
	ItemNotEnough = 1007,--%1s不足
	ItemUseIlleganotEnoughlError = 1008,--道具非法使用
	ConfigError = 1009,--配置错误
	RewardUnmetError = 1010,--未满足领取条件
	RewardReceivedError = 1011,--该奖励已领取
	MailNotExit = 1141,--邮件不存在
	ChargeActTypeClose = 1151,--该活动类型未开放充值
	ChargeProductNull = 1152,--商品不存在
	ChargeClose = 1153,--充值入口未开放
	ChargeGenOrderErr = 1154,--生成订单号失败
	ChargeGetOrderErr = 1155,--获取订单号失败
	ChargeNotExit = 1156,--订单不存在
	ChargeHadDeliver = 1157,--订单已发货
	ChargeInfoNotMatch = 1158,--订单核对失败
	ChargeProductNotExit = 1159,--商品已过期
	ChargeGearError = 1160,--档位配置不存在
	GiftCodeError = 1171,--兑换码错误
	FirstChargeStatusErr = 1181,--没有可领取的首充奖励
	ShopNull = 1300,--商店未开启
	ShopTimeFreeLimit = 1301,--免费次数不足
	ShopTimeVideoLimit = 1302,--广告次数不足
	ShopTimeBuyLimit = 1303,--购买次数不足
	ShopTimeGoodNull = 1304,--商品不存在
	Plant = 1305,--商品不存在
}
--旅行事件类型
pb_Travel_EEventType = 
{
	EventNone = 0,--忽略
	PetFeed = 1,--宠物投喂
	ReceiveRewards = 2,--领取奖励
}
--条件表
pb_Travel_EConditionType = 
{
	ConditionNone = 0,--忽略
	Satiety = 1,--饱食度
	Charm = 2,--魅力值
}
--SDK类型
pb_Login_ESdk = 
{
	Test = 9999,--内网(无登录验证)
	PetWorld = 2,--宠物世界平台
}
--登陆返回
pb_Login_ELoginResult = 
{
	Success = 0,--登陆成功
	AuthFailed = 1,--SDK验证失败
	ReconnectFail = 2,--超过最大重连时间
	SdkError = 3,--未接入该SDK
	UserNull = 4,--账号为空
	TokenNull = 5,--Token为空
}
--账号当前状态
pb_Login_ELoginAccStatus = 
{
	Normal = 0,--普通登录
	Create = 1,--创角登录
}
--重连类型
pb_Login_EReconnectType = 
{
	Common = 0,--普通
	Quick = 1,--快速
}
--展示类型
pb_Reward_EShowType = 
{
	None = 0,--不展示
	Common = 1,--通用弹窗
}
--物品类型
pb_Item_EItemType = 
{
	Source = 0,--资源
	Equip = 1,--装备
	Box = 2,--宝箱
	Role = 3,--英雄道具
	Pet = 4,--宠物道具
	Land = 5,--地块道具
	Seed = 6,--种子道具
	Fruit = 7,--果实道具
}
--物品ID
pb_Item_EItemId = 
{
	None = 0,--未定义
	Diamond = 101,--钻石
	Gold = 102,--金币
	Exp = 103,--经验
	Stamina = 104,--体力
	SevenDayPoint = 108,--七日活跃积分
}
--宝箱类型
pb_Item_EBoxType = 
{
	No = 0,--无效果
	Choose = 1,--自选
	Auto = 2,--自动使用
}


return Items