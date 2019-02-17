from graphics import *
"""
work3.py
 A program that converts a color image to grayscale.
 The user supplies the name of a file containing a GIF or PPM image, 
 and the program loads the image and displays the file. At the click of the mouse, 
 the program converts the image to grayscale.
  The user is then prompted for a file name to store the grayscale image in.

"""
def main():
    inputfile=input("请输入原文件地址:")
    outputfile=input("请输入目标存储地址：")

    #打开图片文件获取大小
    image=Image(Point(0,0),inputfile)
    height=image.getHeight()
    width=image.getWidth()


    # 在窗口绘图
    image = Image(Point(width/2, height/2), inputfile)
    WIN=GraphWin("converts a color image to grayscale",width,height)
    image.draw(WIN)

    x = 0
    y = 0

    #等待鼠标点击转换图片
    WIN.getMouse()
    for x in range(width):
        for y in range(height):
            r,g,b=image.getPixel(x,y)
            brightness = int(round(0.299* r + 0.587*g + 0.114* b))
            image.setPixel(x,y,color_rgb(brightness,brightness,brightness))
            WIN.update()

    #保存图片，等待鼠标点击关闭窗口
    image.save(outputfile)
    WIN.getMouse()
    WIN.close()

main()