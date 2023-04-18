# Torn-ne-push（Torn报信）
[![Python application](https://github.com/Mostlai/Torn-ne-push/actions/workflows/tnp.yml/badge.svg)](https://github.com/Mostlai/Torn-ne-push/actions/workflows/tnp.yml)
<img  src="https://img.shields.io/badge/-Python-green?style=flat-square&logo=Python" />
<a href="mostlai.github.io"><img src="https://img.shields.io/static/v1?label=Blog&message=link&color=red"/></a>

基于[Git action](https://github.com/Mostlai/Torn-ne-push/actions)和[Qmsg](https://qmsg.zendee.cn/)搭建的Torn报信仓库

```
cron: '20 * * * *'
//每小时的第20分钟报时一次，延迟预计10min
```

## How to use

首先在[Qmsg](https://qmsg.zendee.cn/)登录并获取你的机器人KEY，注意你的QQ记得添加机器人为好友（不然怎么发消息给你）

然后Fork此仓库到你的Github账户下

Fork之后在你的仓库下的Settings->Actions secrets and variables->Actions页面下点击New Repository secrets,在NAME处输入QMSG_KEY，在SECRET处输入你刚获取到的机器人KEY，然后点击Add secret，然后再次点击New Repository secrets,在NAME处输入TORN_KEY，在SECRET处输入你的TORN账户API KEY，Github是可靠平台，可以放Full access，点击Add secret
