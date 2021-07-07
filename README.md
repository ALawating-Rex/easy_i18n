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

# 版本>=1.2 增加的逻辑：要翻译的str 指定的语言(locale)不存在则认为指定的是默认语言，在当前语言找不到则原样返回（注：不会再去默认语言查找）  
# 要翻译的str 指定的模块(module)不存在则认为指定的是默认模块，在当前模块找不到，如果当前模块是默认模块则原样返回  
# 如果当前模块不是默认模块，那么会再重新去默认模块查找翻译，再找不到则原样返回 
print(t("hi_only_en", locale="zh"))
print(t("only g has this", locale="zh", module="user"))
print(t("both g and user module has this", locale="zh", module="user"))
print(t("both g and user module has this", locale="zh", module="user1"))
print(t("only en and g has this", locale="zh"))
print(t("only en and g has this"))
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
  
## config 说明
config使用举例：   
```python
config = {
    "load_path": "/locales", # 指定在 /locales 下找对应的翻译 json文件
    "default_module": "global", # 指定默认的全局模块，你可以为比如用户模块，订单模块单独设置翻译，如果不指定 module 则会去全局模块查找。
}
a_i18n = Ai18n(locales=["en", "zh"], config=config)
```

## NOTE 注意
```
**NOTE:** 
for example your locale is en , define load_path as a absolutely path is recommended,
create an en.json in this path. the content for example is: (default_module should equal g)
    {
      "g": {
        "hi": "hello world",
        "test": "test 1"
      },
      "user": {
        "hi": "user:hello world",
        "user {id} is deleted": "user {id} is deleted"
      }
    }

比如上述例子指定 load_path 为 /locales 且 Ai18n(locales=["en", "zh"], config=config)  
那么要提前在 /locales 下 创建 en.json 和 zh.json  
json内容参考上述例子即可  
```
