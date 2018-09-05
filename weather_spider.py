import pymysql
import requests
from datetime import datetime
from lxml import etree

def get_area(area):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='cnweather', charset='utf8')
    cursor = conn.cursor()  # 获取游标
    sql="select num from areas where area='%s';"%area
    cursor.execute(sql)
    number = cursor.fetchall()[0][0]
    return number

def spider(number,area):
    list_we=[]
    list_we.append(area)
    headers={
'Connection':'keep-alive',
'Cookie':'userNewsPort0=1; vjuids=4490f1cdc.165a51e1c70.0.fa51f6f6159a9; UM_distinctid=165a51e1cb64f0-03de4db737db8d-b373f68-144000-165a51e1cb7803; CNZZDATA1262608253=786516090-1536071805-https%253A%252F%252Fwww.baidu.com%252F%7C1536071805; f_city=%E6%9D%AD%E5%B7%9E%7C101210101%7C; defaultCty=101210101; defaultCtyName=%u676D%u5DDE; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1536073539; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1536074264; vjlast=1536073539.1536073539.30; Wa_lvt_1=1536073539; Wa_lpvt_1=1536074264',
'Host':'www.weather.com.cn',
'Referer':'http://www.weather.com.cn/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    }
    url_1='http://www.weather.com.cn/weather/'+str(number)+'.shtml#search'
    res1=requests.get(url=url_1,headers=headers).content.decode('utf8')
    html1 = etree.HTML(res1)
    print('地区：',area)
    try:
        tianqi=html1.xpath('//ul[@class="t clearfix"]/li/p[1]/text()')[0]
        print('天气：', tianqi)
        list_we.append(tianqi)
    except:
         pass
    try:
        tem=html1.xpath('//ul[@class="t clearfix"]/li/p[2]/i/text()')[0]
        print('温度：',tem)
        list_we.append(tem)
    except:
        pass
    try:
        wind=html1.xpath('//ul[@class="t clearfix"]/li/p[3]/i/text()')[0]
        print('风速：',wind)
        list_we.append(wind)
    except:
        pass

    url_2='http://www.weather.com.cn/weather1d/'+str(number)+'.shtml#search'
    res=requests.get(url=url_2,headers=headers).content.decode('utf8')
    html=etree.HTML(res)
    try:
        ziwaixian=html.xpath('//ul[@class="clearfix"]/li[1]/span/text()')[0]
        print('紫外线：',ziwaixian)
        list_we.append(ziwaixian)
    except:
        pass
    try:
        cloth=html.xpath('//li[@id="chuanyi"]/a/p/text()')[0]
        print('穿衣：',cloth)
        list_we.append(cloth)
    except:
        pass
    try:
        washcar=html.xpath('//ul[@class="clearfix"]/li[5]/span/text()')[0]
        print('洗车：',washcar)
        list_we.append(washcar)
    except:
        pass
    try:
        air=html.xpath('//ul[@class="clearfix"]/li[6]/span/text()')[0]
        print('空气质量：',air)
        list_we.append(air)
        # list_we.append(area)
    except:
        pass
    now_time = datetime.now()
    new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    list_we.append(new_time)
    # print(list_we)
    return list_we

def write_weather(list_we):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='cnweather', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("insert into weather values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (str(list_we[0]),str(list_we[1]),str(list_we[2]),str(list_we[3]),str(list_we[4]),str(list_we[5]),str(list_we[6]),str(list_we[7]),str(list_we[8])))
    conn.commit()


if __name__ == '__main__':
    area=input('请输入你要查询哪个地区的天气：')
    number=get_area(area)
    list_we=spider(number,area)
    write_weather(list_we)
