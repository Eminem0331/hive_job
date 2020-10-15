# -*- coding: utf-8 -*-
# tcp mapping created by hutaow(hutaow.com) at 2020-10-12

import pandas as pd
from datetime import datetime

class handle_data():

    def transfer_to_list(self,string):
        string = str(string)
        string = string.replace('(', '')
        string = string.replace(')', '')
        string = string.replace('"', '')
        string = string.replace("'", "")
        string = string.replace(" ", "")
        string = string.split(',')

        return string

    def transfer_to_tuple(self,df):
        re=[]
        for n in range(len(df)):
            print(n)
            a=df.iloc[n]
            print(a)
            print(tuple(a))
            re.append(tuple(a))
        return re

    def main(self,df):
        start = datetime.now()
        print(start)

        '''
        数据格式整理
        '''
        df=list(df)

        re=list(map(handle_data().transfer_to_list, df))
        print(re)
        re=pd.DataFrame(re)

        '''去除重复值'''
        try:
            re.drop_duplicates(inplace=True)
            print(re)
            print('Eminem')
        except:
            pass

        re = [tuple(xi) for xi in re.values]
        print(re)
        re=str(re)
        print('数据清洗完成')

        # handle_data().text_create('test',re)
        # print('111111')

        end = datetime.now()

        print(str(start), str(end))

        return re





import sys
'''
定义主函数
'''
if __name__ == '__main__':
    try:
        df=sys.stdin
        df=handle_data().main(df)
        print(df)
        re=0
    except:
        re=1
        pass

