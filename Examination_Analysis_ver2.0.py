#2019.11.23更新 分析强弱
#2019.11.24更新 分析挂科数目
#2019.11.30更新 GUI！
#预计优化：强弱势的机制可以更改一下；一次多人；多人互相比对；各个大题的得分率；

import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#面对ctrl编程（不）
#导入制图用的库和字体


#定义指令——Draw
def Draw():
        #设置学科
        lab=np.array(["语文","数学","英语","物理","化学","生物","政治","历史","地理","技术"])
        datalen = 10

        #当 指令 生效时  =>  抓取输入框中的数据并且处理
        name=str(name_i.get())
        chi=float(chi_i.get())/150
        mat=float(mat_i.get())/150
        eng=float(eng_i.get())/150
        phy=float(phy_i.get())/100
        che=float(che_i.get())/100
        bio=float(bio_i.get())/100
        pol=float(pol_i.get())/100
        his=float(his_i.get())/100
        geo=float(geo_i.get())/100
        tec=float(tec_i.get())/50

        #建立学科列表 并转换为待读入数据！
        grade=[chi,mat,eng,phy,che,bio,pol,his,geo,tec]
        data = np.array(grade)

        #建立字典 key为分数占比 value为科目名称，方便取最值
        g_dict={chi:"语文",
        mat:"数学",
        eng:"英语",
        phy:"物理",
        che:"化学",
        bio:"生物",
        pol:"政治",
        his:"历史",
        geo:"地理",
        tec:"技术"}

        #强弱分析
        g_max=str(g_dict[max(grade)])
        g_min=str(g_dict[min(grade)])

        #挂科分析
        fail=0
        for key in g_dict:
                if key<0.6 :
                        fail=fail+1
        fail=str(fail)

        #制图
        angles = np.linspace(0,2*np.pi,datalen,endpoint=False)#切开

        data = np.concatenate((data,[data[0]]))#闭合！
        angles = np.concatenate((angles,[angles[0]]))#闭合！角的之前弄错了！！怪不得出错！！

        plt.polar(angles,data,'ro-',linewidth=3)#建系
        plt.thetagrids(angles * 180 / np.pi,lab)#标签
        plt.fill(angles,
                data,
                facecolor='g',
                alpha=1/10 )

        #尺 规 作 图（确信
        plt.ylim(0,1)

        #标题制作 把挂科的数量公开处刑
        plt.title(name+"成绩的分析 ( · ω ·)\n宁挂了"+fail+"门课",fontsize='large')
        plt.text(0.864*3.14,0.357,"强势学科:"+g_max,fontsize='x-large')
        plt.text(1.123*3.14,0.339,"弱势学科:"+g_min,fontsize='x-large')

        #输出图！
        plt.show()      
#定义指令结束



#建立窗口 打上标题 设置大小
win = tk.Tk()
win.title("考试成绩分析装置ver2.0")
win.geometry("300x600")


#输入框设置↓
#注意 请不要设置初始数值 容易出问题 
#注意 不要pack

#语文
tk.Label(win,text="语文：").place(x=10,y=10)
chi_i = tk.Entry(win,show=None)
chi_i.place(x=100,y=10)


#数学
tk.Label(win,text="数学：").place(x=10,y=50)
mat_i = tk.Entry(win,show=None)
mat_i.place(x=100,y=50)


#英语
tk.Label(win,text="英语：").place(x=10,y=90)
eng_i = tk.Entry(win,show=None)
eng_i.place(x=100,y=90)


#物理
tk.Label(win,text="物理：").place(x=10,y=130)
phy_i = tk.Entry(win,show=None)
phy_i.place(x=100,y=130)


#化学
tk.Label(win,text="化学：").place(x=10,y=170)
che_i = tk.Entry(win,show=None)
che_i.place(x=100,y=170)


#生物
tk.Label(win,text="生物：").place(x=10,y=210)
bio_i = tk.Entry(win,show=None)
bio_i.place(x=100,y=210)


#政治
tk.Label(win,text="政治：").place(x=10,y=250)
pol_i = tk.Entry(win,show=None)
pol_i.place(x=100,y=250)


#历史
tk.Label(win,text="历史：").place(x=10,y=290)
his_i = tk.Entry(win,show=None)
his_i.place(x=100,y=290)


#地理
tk.Label(win,text="地理：").place(x=10,y=330)
geo_i = tk.Entry(win,show=None)
geo_i.place(x=100,y=330)


#技术
tk.Label(win,text="技术：").place(x=10,y=370)
tec_i = tk.Entry(win,show=None)
tec_i.place(x=100,y=370)

#设置按钮
btn=tk.Button(win,text="  制图按钮  ",command=Draw)
btn.place(x=110,y=470)

#名字
tk.Label(win,text="您的名字:").place(x=10,y=410)
name_i=tk.Entry(win,text="name",show=None)
name_i.place(x=100,y=410)


#制作人
tk.Label(win,text="制作者：迷亭").place(x=10,y=550)
tk.Label(win,text="( · ω ·)").place(x=10,y=570)
#开始循环!
win.mainloop()
