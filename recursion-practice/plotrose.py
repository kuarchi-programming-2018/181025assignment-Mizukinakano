from turtle import*# 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-100, -150], [100, -150], [200, 200], [-200,200]], 0.20, 80)
done()  # turtleの終了処理