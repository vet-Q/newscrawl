import pymysql
import pandas as pd
import argparse
from sqlalchemy import create_engine
import time

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mysql_host", type=str, default="127.0.0.1", help="MySQL host ip")
    parser.add_argument("--mysql_user", type=str, default="root", help="MySQL user name")
    parser.add_argument("--mysql_password", type=str, default="DJPY!", help="MySQL password")
    parser.add_argument("--mysql_database", type=str, help="database name")
    parser.add_argument("--mysql_table", type=str, help="table name")
    opt = parser.parse_args()
    return opt

def connectToSQL(opt):
    # MySQL Connector using pymysql
    host = opt.mysql_host
    name = opt.mysql_user
    password = opt.mysql_password

    engine_address = f"mysql+mysqldb://{name}:{password}@{host}:3306/djpy?charset=utf8"
    pymysql.install_as_MySQLdb()
    engine = create_engine(engine_address)
    conn = pymysql.connect(host=host,
                           user=name,
                           password=password,
                           db='djpy')
    cursor = conn.cursor()
    cursor.execute("select `title` from datas")

    ## 데이터 Fetch
    titles = []
    rows = cursor.fetchall()
    for i in rows:
        i = i[0]
        titles.append(i)

    return titles


def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res


def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r


x = connectToSQL(parse_opt())

for i,j in enumerate(x):
    if i<len(x)-1:
        r2, word2 = diff_ngram(x[i],x[i+1], 2)
        if r2>0.7:
            print(x[i],'\n', x[i+1],'point:', r2)
            time.sleep(2)
        else:
            print('point:', r2)
            time.sleep(2)
    else:
        break





