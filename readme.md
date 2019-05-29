# &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;MircoPython - Display
#### 📖 [English document](https://github.com/aJantes/MircoPython-led/blob/master/english_document.md)
> 模块介绍：

- [BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/README.md)   
- [LED灯(WS2812B)](https://github.com/aJantes/MircoPython-led/blob/master/source/WS2812B.pdf)


# LED 矩阵显示
LED 矩阵 硬件相关函数 [display 模块](https://github.com/aJantes/MircoPython-led/blob/master/source/display.py)。在调用相关函数前，需要先导入对应的库。
    
## 主要函数 

- `display.scroll("Hello World!", color=Red, delay=150)`：

在 led 矩阵滚动显示红色色的 "Hello World!"  字符串，滚动的时间间隔为 150 ms。

- `display.show(Image.ALL_CLOCKS, loop=True, delay=100)` :

在 led 矩阵通过led的亮灭显示出时钟。时钟循环播放，每次的变化间隔为 100 ms。


---

## 例程
文件|功能
:--|:--
 [show_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_text.py)  | 显示简单文本
 [display_yellow_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_yellow_text.py) |  显示黄色文本
 [display_color_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_color_text.py) | 显示多色文本
 [display_custom_color.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_custom_color.py) | 显示自定义颜色文本
 [show_image.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_image.py) | 显示内置图像
 [show_my_image.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_my_image.py) | 显示自定义图像
[show_clock.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_clock.py) | 显示内置动画
 [show_animation.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_animation.py) | 显示自定义动画

