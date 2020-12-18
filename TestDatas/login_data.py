from TestDatas.Comm_data import base_url

#正常场
success_data = {'phone':'18684720553','password':'python','check':'{}Index/index'.format(base_url)}

#异常场景--没有手机号、没有密码、手机号位数不对
wrong_data = [
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"186847","passwd":"python","check":"请输入正确的手机号"},
    {"user":"186847055311","passwd":"python","check":"请输入正确的手机号"}
]

#异常场景--错误手机号、密码错误
fail_data = [
    {'user':'18684720559','passwd':'python','check':'此账号没有经过授权，请联系管理员!'},
    {'user':'18684720553','passwd':'python11','check':'帐号或密码错误!'}
]

