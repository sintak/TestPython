# -*- coding: utf-8 -*-
# 如果还不清楚词云怎么搞，请参考这里https://mp.weixin.qq.com/s/0Bw8QUo1YfWZR_Boeaxu_Q，或者自行百度，很简单的一个包

import numpy as np
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

# 统计词频
# win的用户，把解码去掉即可，因为当时mac写入的文件有编码，所以读出来需要解码
def statistics(lst):  
    dic = {}  
    for k in lst:  
        # if not k.decode('utf-8') in dic:dic[k.decode('utf-8')] = 0  
        # dic[k.decode('utf-8')] +=1
        if not k in dic: dic[k] = 0  
        dic[k] +=1
    return dic  


path = '256539666'  # 自己路径自己搞定
list_ = []
with open(path,'r', encoding='utf-8') as f:
    for line in f:
        list_.append(line.strip().split('|')[-2].strip())

dict_ = statistics(list_)


# the font from github: https://github.com/adobe-fonts
font = r'simhei.ttf'
coloring = np.array(Image.open("pic02.jpg"))  # 遮罩层自己定义，可选自己的图片
wc = WordCloud(background_color="white",
               collocations=False, 
               font_path=font,
               width=1400, 
               height=1400,
               margin=2,
               mask=np.array(Image.open("pic02.jpg"))).generate_from_frequencies(dict_)

# 这里采用了generate_from_frequencies(dict_)的方法，里面传入的值是{‘歌手1’:5,‘歌手2’:8,},分别是歌手及出现次数，其实和jieba分词
# 之后使用generate(text)是一个效果，只是这里的text已经被jieba封装成字典了

image_colors = ImageColorGenerator(np.array(Image.open("pic02.jpg")))
plt.imshow(wc.recolor(color_func=image_colors))
plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('mymusic.png')  # 把词云保存下来 