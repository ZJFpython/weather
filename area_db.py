import pymysql

def data():
    areas=open('area','r',encoding='utf-8')
    a=areas.readlines()
    num=[]
    area=[]
    for i in a:
        j=i.split('=')
        a=j[0]
        num.append(a)
        b=j[1][:-1]
        area.append(b)
    return num,area

def areasdb():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='cnweather', charset='utf8')
    cursor = conn.cursor()
    sql='create table areas ( id int unsigned auto_increment primary key not null,num varchar(10),area varchar(10));'
    cursor.execute(sql)
    conn.commit()

def insert(num,area):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='cnweather', charset='utf8')
    cursor = conn.cursor()

    for i,j in zip(num,area):
        cursor.execute("insert into areas values(0,%s,%s);",(str(i),str(j)))
        conn.commit()

if __name__ == '__main__':
    areasdb()
    num,area=data()
    insert(num,area)