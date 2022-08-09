# tongda-oa-2022-poc-exp
通达oa任意用户登录批量检测脚本与利用脚本
运行环境：python3

tongda2022poc.py 运行命令：python3 tongda2022poc.py
![image](https://user-images.githubusercontent.com/51362701/183559819-a89b6b3e-cdb6-4a39-b329-bb64015d644f.png) 
只检测一个目标输入1，批量检测输入其他值: 存在漏洞的url前面会有[+]标识，且会保存至当前目录下的success.txt
![image](https://user-images.githubusercontent.com/51362701/183559874-bad54fe0-d737-4344-bb80-e777feef3af8.png)
tongda2022exp.py 使用命令：调用selenium库,需要安装谷歌浏览器驱动。 http://chromedriver.storage.googleapis.com/index.html (注意版本和自己谷歌浏览器对应，找不到完全一样的版本，就下载版本相近的)，下载至python的根路径下 python3 tongda2022exp.py url(存在漏洞的url)
![image](https://user-images.githubusercontent.com/51362701/183560587-6749dc34-7af1-436f-a2b9-ae947f218577.png)
若报No module named xxx的错误，自行使用命令python3 –m pip install xxx下载
运行后，会调谷歌浏览器，自动操作，切勿人工点击。否则会报错，待漏洞利用成功，也就是成功登录后，方可人工进行点击
![image](https://user-images.githubusercontent.com/51362701/183560609-1b638d66-ff8e-41e5-b8be-7ff72106c049.png)
