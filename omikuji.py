from tkinter import *
import random

root = Tk()
var1 = StringVar()

#おみくじ用の関数
def omikuji():
    list_kuji = ['大凶', '凶', '末吉', '小吉', '中吉', '吉', '大吉']
    #ランダムにリストから抽出
    result = random.choice(list_kuji)
    var1.set("")
    #結果を格納
    var1.set('%s' % result)
    
"""
描画用関数
"""

def display():
    
    root.title('今年の運勢')
    
    #キャンバスの作成
    canvas = Canvas(width = 100, height = 20)
    canvas.pack()
    canvas.create_image(0, 0, anchor =NW)
    
    #応答エリア
    label = Label(root, textvariable=var1, fg="#000000",
                  bg="#ffffff", anchor=E, height=2)
    label.pack()
    
    #ボタン作成
    button = Button(root, text='今年の運勢を占う', command=omikuji, width=20, height=2)
    button.pack()
    
    #メインループ
    root.mainloop()
    
if __name__ == '__main__':
    display()
