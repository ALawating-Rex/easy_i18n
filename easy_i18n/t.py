# -*- coding: utf-8 -*-

"""
an easy way come true i18n for python3
Author: aex
github: https://github.com/ALawating-Rex/easy_i18n
"""

import json


class Ai18n:
    """
    an easy way come true i18n for python3

    :param locales: languages you will use, for example: ["en","zh"].
    :param config: is a dict , for setting config variables
        :load_path - where to find translate files（default is : i18n）
        :default_locale - default locale（default is : en）
        :default_module - default module（default is : g）
        :default_encoding - default encoding（default is : UTF-8）
    :param tm: is a dict, contains all strings you want to translate.

    Example::
        # after import a_i18n and t

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

    **NOTE:** for example your locale is en , define load_path as a absolutely path is recommended,
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
    """

    # tm 的格式类似： {"en":{"g":{"hi":"hi1","test":"test1"},"module1":{"hi":"hi2","test":"test2"}}, "zh":{"g":{"hi":"你好1","test":"测试1"}},"module1":{"hi":"你好2","test":"测试2"}}}
    # 先是区分 locale 然后区分模块， 不区分模块的是此语言全局的翻译

    config = None
    tm = None

    def __init__(self, locales=None, config=None, tm=None):
        if tm and isinstance(tm, dict):
            self.tm = tm
        else:
            self.tm = {}

        self.config = {
            "load_path": "i18n",
            "default_locale": "en",
            "default_module": "g",
            "default_encoding": "UTF-8",
        }
        if config and isinstance(config, dict):
            self.config.update(config)

        if not locales or not isinstance(locales, list):
            locales = [self.config.get("default_locale", "en")]

        for locale in locales:
            try:
                with open(self.config.get("load_path", "i18n") + "/" + locale + ".json", 'r',
                          encoding=self.config.get("default_encoding", "UTF-8")) as load_f:
                    if not self.tm.get(locale, {}):
                        self.tm[locale] = {}
                    load_dict = json.load(load_f)
                    self.tm[locale].update(load_dict)
            except Exception:
                raise

    def get_locale(self, locale: str = None):
        """
        get locale function.
        :param locale: local of your system.
        :return: locale.
        """
        if not locale:
            return self.config.get("default_locale", "en")
        else:
            return locale

    def get_module(self, module: str = ""):
        """
        get module function.
        :param module: module of your system.
        :return: module.
        """
        if not module:
            return self.config.get("default_module", "g")
        else:
            return module

    def add(self, locale: str = None, module: str = "", k: str = "", message: str = ""):
        """
        add translation dictionary manually.
        :param locale: locale of your system.
        :param module: module of your system.
        :param k: original string.
        :param message: string after translate.
        """
        tm = self.tm
        locale = self.get_locale(locale)
        if not tm.get(locale, {}):
            tm[locale] = {}

        module = self.get_module(module)
        if not tm.get(locale, {}).get(module, {}):
            tm[locale][module] = {}

        tm[locale][module][k] = message

    def load_file(self, locale: str):
        """
        add translation dictionary from read file.
        :param locale: locale of your system.
        :return: tuple of True/False , and if False with exception.
        """
        try:
            with open(self.config.get("load_path", "i18n") + "/" + locale + ".json", 'r') as load_f:
                if not self.tm.get(locale, {}):
                    self.tm[locale] = {}
                load_dict = json.load(load_f)
                self.tm[locale].update(load_dict)
        except Exception as e:
            return False, e
        return True, None

    def translate(self, message: str = "", locale: str = None, module: str = ""):
        """
        translate message.
        :param message: original string.
        :param locale: locale of your system.
        :param locale: module of your system.
        :return: string after translate.
        """
        tm = self.tm
        locale = self.get_locale(locale)
        module = self.get_module(module)
        return tm.get(locale, {}).get(module, {}).get(message, message)


if __name__ == '__main__':
    a_i18n = Ai18n(locales=["en", "zh"], config={})
    t = a_i18n.translate
    print(t("a"))
    print(t("b''"))
    print(t("b\""))

    print(t("hi"))
    a_i18n.add(k="hi", message="hello from add1")
    print(a_i18n.tm)
    print(t("hi"))
    print(t("hi", locale="zh"))
    print(t("hi", module="user"))

    print(t("hi''"))
    print(t("hi_only_zh", locale="zh"))
    print(t("user {id} is deleted", locale="zh", module="user").format(id=1))
