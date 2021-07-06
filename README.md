## easy_i18n
> an easy way come true i18n for python3  
> 
> 基于 python3 实现语言本地化
> 
> HomePage: https://github.com/ALawating-Rex/easy_i18n
> 

## install - 安装
```shell script
pip install easy_i18n
```

## usage - 使用举例
```python
from easy_i18n.t import Ai18n

a_i18n = Ai18n(locales=["en", "zh"], config={})
t = a_i18n.translate

# after import or define a_i18n and t
# add translation dictionary manually.
a_i18n.add(k="hi", message="hello by added")
# print all the translation dictionary
print(a_i18n.tm)
# simple use
print(t("hi"))
# simple use, translate "hi" to zh
print(t("hi", locale="zh"))
# simple use, translate "hi" to default locale and find it in module user
print(t("hi", module="user"))
# use when string need to format
print(t("user {id} is deleted", locale="zh", module="user").format(id=1))
```

## Ai18n 说明
Ai18n 类接收两个参数：  
1.参数 locales 是list形式，指定了语言都使用哪几种。举例：["en", "zh"] 那么对应的会在config指定的目录下找 en.json 和 zh.json加载过来  
默认的 east_i18n 有目录 i18n 可供参考
2.参数 config 是dict形式，你可以指定后覆盖默认的 config值：
```
:load_path - where to find translate files（default is : i18n）
:default_locale - default locale（default is : en）
:default_module - default module（default is : g）
:default_encoding - default encoding（default is : UTF-8）
```  
3.config使用举例：
```python
config = {
    "load_path": "/locales", # 指定在 /locales 下找对应的翻译 json文件
    "default_module": "global", # 指定默认的全局模块，你可以为比如用户模块，订单模块单独设置翻译，如果不指定 module 则会去全局模块查找。
}
a_i18n = Ai18n(locales=["en", "zh"], config=config)
```
