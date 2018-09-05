import pymysql


def areas():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='cnweather', charset='utf8')
    cursor = conn.cursor()
    sql='create table weather ( id int unsigned auto_increment primary key not null,city varchar(10),weath varchar(10),temp varchar(10),wind varchar(10),ziwaixian varchar(10),clothes varchar(50),washcar varchar(20),air varchar(10),watch_time datetime);'
    cursor.execute(sql)
    conn.commit()
    print('天气表创建成功')
areas()