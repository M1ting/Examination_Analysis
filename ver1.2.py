#2019.11.23更新 分析强弱
#2019.11.24更新 分析挂科数目

#预计优化：强弱势的机制可以更改一下



import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#面对ctrl编程（不）
#导入制图用的库和字体


print("考试成绩分析装置Ver1.2")
print("更新：可分析学科的强势与弱势。")
print("制作者：迷亭")
print("( ・ω・)")
lab=np.array(["语文","数学","英语","物理","化学","生物","政治","历史","地理","技术"])#10门学科
datalen = 10
name=input("请输入宁的名字:")

#成绩键入
chi=float(input("请输入语文成绩:"))/150
mat=float(input("请输入数学成绩:"))/150
eng=float(input("请输入英语成绩:"))/150
phy=float(input("请输入物理成绩:"))/100
che=float(input("请输入化学成绩:"))/100
bio=float(input("请输入生物成绩:"))/100
pol=float(input("请输入政治成绩:"))/100
his=float(input("请输入历史成绩:"))/100
geo=float(input("请输入地理成绩:"))/100
tec=float(input("请输入技术成绩:"))/50

grade=[chi,mat,eng,phy,che,bio,pol,his,geo,tec]
data = np.array(grade)

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
g_max = str(g_dict[max(grade)])
g_min = str(g_dict[min(grade)])

fail=0
for key in g_dict:
        if key<0.6 :
                fail=fail+1
fail=str(fail)
angles = np.linspace(0,2*np.pi,datalen,endpoint=False)#切开

data = np.concatenate((data,[data[0]]))#闭合！
angles = np.concatenate((angles,[angles[0]]))#闭合！角的之前弄错了！！怪不得出错！！

plt.polar(angles,data,'ro-',linewidth=3)#建系
plt.thetagrids(angles * 180 / np.pi,lab)#标签
plt.fill(angles,
         data,
         facecolor='g',
         alpha=1/10 )
plt.ylim(0,1)
plt.title(name+"成绩的分析 ( · ω ·)\n宁挂了"+fail+"门课",fontsize='large')
plt.text(0.864*3.14,0.357,"强势学科:"+g_max,fontsize='x-large')
plt.text(1.123*3.14,0.339,"弱势学科:"+g_min,fontsize='x-large')
plt.show()#给我出来!!