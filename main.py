import requests, json
from bs4 import BeautifulSoup
import pandas as pd
import argparse
from sqlalchemy import create_engine
import pymysql


class GetDATA():
    '''
    Before making a dataframe related to a 'disease', we prepare an URL which is fitted to the disease,
    blanked disease parameter, and blank DataFrame to arrange the data step by step.
    '''
    def parse_opt(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--mysql_host", type=str, default="127.0.0.1", help="MySQL host ip")
        parser.add_argument("--mysql_user", type=str, default="root", help="MySQL user name")
        parser.add_argument("--mysql_password", type=str, default="DJPY!", help="MySQL password")
        parser.add_argument("--mysql_database", type=str, help="database name")
        parser.add_argument("--mysql_table", type=str, help="table name")
        opt = parser.parse_args()
        return opt

    def __init__(self):
        self.disease = ''
        self.url = ''
        self.result = pd.DataFrame()

    def connectToSQL(self, host, name, password):
        # MySQL Connector using pymysql
        host, name, password = host, name, password
        engine_address = f"mysql+mysqldb://{name}:{password}@{host}:3306/djpy?charset=utf8"
        pymysql.install_as_MySQLdb()
        engine = create_engine(engine_address)
        conn = pymysql.connect(host=host,
                               user=name,
                               password=password,
                               db='djpy')
        cursor = conn.cursor()
        return engine, conn

    def getHtml(self, disease, opt):
        self.disease = disease
        self.url = f'https://medisys.newsbrief.eu/rss/?type=search&mode=advanced&atLeast={self.disease}'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'lxml')
        datas = soup.findAll('item')
        for idx, event in enumerate(datas):
            title = event.contents[0].text
            try:
                link = event.contents[2].text
                if isinstance(link, NavigableString):
                    link = 'navigableString입니다'
                else:
                    link = event.contents[2].text
            except: link = str('링크에 문제가 있습니다')

            pubdate = event.contents[5].text

            rowData = pd.DataFrame({'title': [title],
                                    'link': [link],
                                    'pubdate': [pubdate]
                                    })

            self.result = self.result.append(rowData)

        # setting parameters by using argparse library
        host = opt.mysql_host
        name = opt.mysql_user
        pwd = opt.mysql_password

        # db connect
        engine, conn = GetDATA.connectToSQL(self, host, name, pwd)

        # db insert
        self.result.to_sql('datas', con=engine, if_exists='append', index=False)

        conn.close()

        print(self.result)

        return 'hello world'

if __name__== "__main__":
    Crawler = GetDATA()
    opt = Crawler.parse_opt()
    Crawler.getHtml('african swine fever',opt)