# inventory_management_django_system

#### 介绍
数据库大作业——前后端分离的库存管理系统——django后端部分

#### 软件架构
本项目是一个前后端分离的库存管理系统，前端采用Vue+Element-Plus+Echarts，后端采用Django+PostgreSQL,

● 本系统为一个简单的后台管理系统，可为企业提供后台管理服务，主要包括系统用户的登录注册、库存管理、订单管理、临时订单、用户管理、数据可视化六大板块的功能。

● 其中系统用户分为两类，一类是高权限的超级管理员，另一类是低权限的普通管理员，其中普通管理员不具备用户管理功能。系统用户既是系统的管理员，也是订单的负责人，每个管理员负责自己的订单与临时订单。

● 在注册页面默认注册低权限的普通管理员，超级管理员可在用户管理板块中对系统的用户权限进行修改。

● 每个订单/临时订单会通过userId这个属性与用户绑定，类似于公司中某个订单是谁负责的，增加订单/临时订单时通过验证目前所登录信息来做到绑定。

● 数据可视化模块中，主要对公司近十年具体的销售额数据进行可视化，里面的数据通过sql语句初始化在数据库表里面，前端无需提供，后端也无法更改，相当于一个独立静态的模块，无数据的改变。

前端代码链接：https://gitee.com/fish-in-jiangan-river/inventory_management_system

（看官别忘记给个star哦！）


#### 安装教程

`git clone https://gitee.com/fish-in-jiangan-river/inventory_management_system.git`


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
