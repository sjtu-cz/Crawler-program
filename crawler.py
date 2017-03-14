# coding=utf-8
#导入需要的三个库，requests网络交互，bs4获取标签，os处理系统操作

import requests
import bs4
import os

#模拟header信息，保证网络请求通过
header = {'User-Agent':
                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                        '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

         }

#请求网址，抓取从N页到M页妹子图片链接，返回list，包含所有链接地址
def req(start_page,end_page):

# 生成图片地址的空列表
    fecthed_pic_add_all = []
# 逐一访问页面
    for i in range(start_page,end_page+1):
         jiandan_url = 'http://jandan.net/ooxx/page-'+str(i)
        #防止请求错误
         try:
             response = requests.get(jiandan_url,headers=header)
         except Exception as e:
             print('请求出现错误，错误信息：%s' %e)
         else:
             #确定访问正常后，得到页面信息
             content = response.text
             #将信息传入bs4
             fecthed_info = bs4.BeautifulSoup(content,'html.parser')
             #寻找所有包含图片地址的tag
             fecthed_info_tagA = fecthed_info.find_all('a','view_img_link')
             #得到本页所有图片地址
             fecthed_pic_add = [l.get('href') for l in fecthed_info_tagA]
             #将该页面图片地址添加到总表
             for i in fecthed_pic_add:
                  fecthed_pic_add_all.append(i)
    #返回图片地址列表
    # print (fecthed_pic_add_all)
    return fecthed_pic_add_all
#下载图片
def downliad_pic(pic_addresses):
     #遍历图片地址
     for i in pic_addresses:
         try:
             i = 'http:'+i
             #请求图片网址
             pic_resp = requests.get(i,headers = header)
             #二进制方式读取网页
             pic = pic_resp.content
             pic_name = i.split('/')[-1]
             #以'wb'写入文件
             with open('pic/'+pic_name,'wb') as f:
                 f.write(pic)
                 print ('文件\t'+pic_name+'\t已下载')
         except Exception as e:
            print('下载出现错误，信息：%s' %e)

def main():
    #判断是否创建下载文件夹
    create_file = os.path.exists('pic')
    #print(create_file)
    if not create_file:
        os.mkdir('pic')
        print ('已创建了下载文件夹')
    print ('设置您要下载的开始页与最终页：')
    while True:
        try:
            start_page = int(input('起始页：'))
            end_page = int(input('最终页：'))
            if end_page < start_page:
                print ('最终页小于起始页')
                continue
        except:
            print ('输入不合法')
        else:
            break
    print ('正在下载...')
    pic_addresses = req(start_page, end_page)
    downliad_pic(pic_addresses)
    print ('全部下载完成')

main()








# #  coding=gbk

# import time
# import urllib2
# from bs4 import BeautifulSoup
# import re
# # import sys
# # reload(sys)
# # sys.setdefaultencoding('gbk')

# m = time.strftime('%m',time.localtime())
# day = time.strftime('%m/%d/',time.localtime())
# y = time.strftime('%Y',time.localtime())
# age = int(y) - 1984


# time_now = time.strftime('%Y%m%d',time.localtime())
# # print "today is %s"%time_now
# # print "movies:",


# ###get douban movie list ###

# url = "http://movie.douban.com/later/ziyang"
# html = urllib2.urlopen(url)
# content = html.read()
# html.close()

# l = []

# soup = BeautifulSoup(content,"html5lib")
# soup.prettify()

# movies = soup.find_all("div",class_="intro")#get info from web

# for items in movies:
#     movie_name = items.a.get_text() #movie name
#     movie_date = items.li.get_text()#display date

#     str_movie_date = str(movie_date)
#     str_movie_date = str_movie_date.replace('yue','/').replace('ri','/')

#     movie_info = str_movie_date + movie_name
#     n = ''.join(movie_info)
#     m_list = []
#     # if str_movie_date == day:
#     #     today_movie = ''.join(n)
#     #     print today_movie
#     # else:
#     #     str_movie_date.startswith(m)
#     #     month_movie = ''.join(n)
#     #     print month_movie

# url2 = "http://movie.douban.com/nowplaying/shanghai/"
# html2 = urllib2.urlopen(url2)
# content2 = html2.read()
# html2.close()

# soup2 = BeautifulSoup(content2,"html5lib")


# movie2 = soup2.find_all("li",class_="stitle")
# for i in movie2:
#     print i.a.get_text(),




# """邮件部分"""

# msg1 = " 亲爱的xcsbaty，今天是%s等精彩电影上映的日子，希望你能喜欢！" % (n[6:20])
# msg2 = """ which is so perfectly fitting for you!
#                              #每天都永远爱你的汤姆猫！ """
# msg3 = msg1+msg2
# print msg3



# """email doc

# import smtplib
# from email.mime.text import MIMEText
# mailto_list=["xcsbaty@21cn.com"]
# mail_host="smtp.qq.com"  #设置服务器
# mail_user="517xxxx93"    #用户名
# mail_pass="amXXXX21"   #口令
# mail_postfix="qq.com"  #发件箱的后缀

# def send_mail(to_list,sub,content):
#     me= "Dear xcsbaty"+"<"+mail_user+"@"+mail_postfix+">"
#     msg = MIMEText(content,_subtype='plain',_charset='')
#     msg['Subject'] = "亲爱的xcsbaty"
#     msg['From'] = me
#     msg['To'] = ";".join(to_list)
#     try:
#         server = smtplib.SMTP()
#         server.connect(mail_host)
#         server.login(mail_user,mail_pass)
#         server.sendmail(me, to_list, msg.as_string())
#         server.close()
#         return True
#     except Exception, e:
#         print str(e)
#         return False
# if __name__ == '__main__':
#     if send_mail(mailto_list,"hello",msg3):
#         print "发送成功"
#     else:
#         print "发送失败"

#         """
