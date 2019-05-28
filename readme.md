# mircopython - Led
#### 📖 [English document](https://github.com/aJantes/MircoPython-led/blob/master/english_document.md)
![](album/bit.gif)
> 硬件介绍：

- [BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/README.md)   
- [LED灯(WS2812B)](https://github.com/aJantes/MircoPython-led/blob/master/source/WS2812B.pdf)





# LED矩阵显示
LED矩阵 硬件相关函数 [display 模块](https://github.com/aJantes/MircoPython-led/blob/master/source/display.py)。在调用相关函数前，需要先导入对应的库。
    

## **显示滚动文本**
bpi：bit 的 led 面板 采用的是可编程的 RGB灯(ws2812b)，这种 RGB灯 通过编程理论上可以显示255 *255 *255种颜色，也就是1600万种颜色
## 主要函数 

- `display.scroll(val, color=Red, delay=150)`：


例如: `display.scroll("Hello World!",color=Yellow,delay=200)` 在led矩阵滚动显示黄色的"Hello World!" 字符串，滚动的时间间隔为 200 ms。




## **面板显示图像**

图像的显示是由于led矩阵上每个led灯的亮灭、颜色、亮度等状态不同而形成的。只要控制不同led灯的状态，就能形成想要的图像。图像是由一个列表组成，在列表中按led灯排列顺序分别赋值1（亮）或者0（暗），从而显示图像。

## 主要函数
- `display.show(images, loop, delay)`:



例如: `display.show(Image.ALL_CLOCKS, loop=True, delay=100)`  在led矩阵通过led的亮灭显示出时钟。时钟循环播放，每次的变化间隔为 100 ms。


---

## **led矩阵例子**
1. [show_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_text.py)   -显示简单文本
2. [display_yellow_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_yellow_text.py)   -显示黄色文本
3. [display_color_text.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_color_text.py)  -显示多色文本
4. [display_custom_color.py](https://github.com/aJantes/MircoPython-led/blob/master/example/display_custom_color.py)  -显示自定义颜色文本
5. [show_image.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_image.py)  -显示内置图像
6. [show_my_image.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_my_image.py)  -显示自定义图像
7. [show_clock.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_clock.py)  -显示内置动画
8. [show_animation.py](https://github.com/aJantes/MircoPython-led/blob/master/example/show_animation.py)  -显示自定义动画

