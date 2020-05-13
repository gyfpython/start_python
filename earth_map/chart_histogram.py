from pyecharts import Bar
from pyecharts import Line
from pyecharts import Pie
from pyecharts import Scatter
from pyecharts import WordCloud


bar = Bar('第一个图', '直方图')
kwargs = dict(
    name='柱形图',
    x_axis=['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'],
    y_axis=[5, 20, 36, 10, 75, 90]
    # bar_category_gap = 0 间距
)
bar.add(**kwargs)
bar.render('直方图.html')

x = ["衬衫", "羊毛衫", "雪纺衫","裤子", "高跟鞋", "袜子"]
y1 = [5, 20, 36, 10, 75, 90]
y2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
title1 = '商家A'
title2 = '商家B'
bar.add(title1, x, y1, is_stack=True)
bar.add(title2, x, y2, is_stack=True)
bar.render('柱状图数据堆叠.html')

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y1 = [5, 20, 36, 10, 75, 90]
y2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
title1 = '商家A'
title2 = '商家B'
bar.add(title1, x, y1, mark_point=['average'])
bar.add(title2, x, y2, mark_line=['min', 'max'])
bar.render('柱状图标记线和标记点.html')

x = ["衬衫", "羊毛衫", "雪纺衫","裤子", "高跟鞋", "袜子"]
y1 =[5, 20, 36, 10, 75, 90]
y2 = [10, 25, 8, 60, 20, 80]
bar = Bar("x轴与y轴交换")
title1 = '商家A'
title2 = '商家B'
bar.add(title1, x, y1)
bar.add(title2, x, y2, is_convert=True)
bar.render('条形图.html')

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.render('折线图1.html')

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y1 = [5, 20, 36, 10, 10, 100]
y2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
label1 = '商家A'
label2 = '商家B'
kwargs = dict(
    mark_point=['average', 'max', 'min'],
    mark_point_symbol='diamond',
    mark_point_textcolor='#40ff27'
)
line.add(label1, x, y1, **kwargs)
kwargs2 = dict(
    mark_point=['average', 'max', 'min'],
    mark_point_symbol='arrow',
    mark_point_symbolsize=40
)
line.add(label2, x, y2, **kwargs2)
line.render('折线图2.html')

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", x, y, is_label_show=True)
pie.render('饼图1.html')

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例",title_pos='center')
kwargs = dict(
    radius=(40, 75),
    label_text_color=None,
    is_label_show=True,
    legend_orient='vertical',
    legend_pos='left'
)
pie.add("", x, y, **kwargs)
pie.render('饼图-圆环图.html')

v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
scatter.render('散点图.html')

scatter.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size', visual_range_size=[20,80])
scatter.render('散点图1.html')

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y1 = [5, 20, 36, 10, 10, 100]
y2 = [55, 60, 16, 20, 15, 80]
line = Line("面积图示例")
label1 = '商家A'
label2 = '商家B'
kwargs = dict(
    if_fill=True,
    line_opacity=0.2,
    area_opacity=0.4,
    symbol=None
)
line.add(label1, x, y1, **kwargs)
kwargs2 = dict(
    s_fill=True,
    area_color='#000',
    area_opacity=0.3,
    is_smooth=True
)
line.add(label2, x, y2, **kwargs2)
line.render('面积.html')

name_list = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World',
            'Charter Communications', 'Chick Fil A', 'Planet Fitness',
            'Pitch Perfect', 'Express','Home', 'Johnny Depp',
            'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary EllenMark',
            'Farrah Abraham', 'Rita Ora', 'Serena Williams',
            'NCAA baseball tournament','Point Break']
value_list = [10000, 6181, 4386, 4055, 2467, 2244,
            1898, 1484, 1112,965, 847, 582, 555,
            550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=800, height=500)
wordcloud.add("", name_list, value_list, word_size_range=[20, 100])
wordcloud.render('词云.html')
# show map : https://blog.csdn.net/weixin_43746433/article/details/91346371

