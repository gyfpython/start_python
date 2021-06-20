# 中文转拼音第三方库：https://github.com/mozillazg/python-pinyin

from pypinyin import lazy_pinyin, pinyin, Style

print(''.join(lazy_pinyin('测试qwe啦')))  # ceshiqwela
print(pinyin('测试', style=Style.TONE2, heteronym=True))  # [['ce4'], ['shi4']]
