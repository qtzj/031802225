import json
import os
import argparse

#命令行参数的设置
def set_command():#命令行参数的设置（-i为初始化，-u为用户，-r为项目，-e为事件）
    self_parser = argparse.ArgumentParser(description='analysis the json file')
    self_parser.add_argument('-i', '--init', help='json path')
    self_parser.add_argument('-u', '--user', help='username')
    self_parser.add_argument('-r', '--repo', help='repository name')
    self_parser.add_argument('-e', '--event', help='type of event')
#命令行参数的解析
    args = self_parser.parse_args()#命令行参数的解析

# 解析json的过程python3 GHAnalysis.py <--init|-i> <path to data>
class json_data:
    def __init__(self, dict_address: int = None, reload: int = 0):
        if reload == 1:
            self.__init(dict_address)
        x = open('F:\homework_information\2015-01-01-15.json', 'r', encoding='utf-8').read() #打开json文件
        self.__4Events4PerP = json.loads(x) # 解析json

# 数据处理，用是否存在来判断
def count(data,username,repo,event):
    answer=0
    for da in data:
        if not len(username) == 0:  # 存在用户
            if not username == da['actor']['login']: #用户不在文件中跳出循环
                    continue
            else:
                    pass
        else:
            pass
            if not len(repo) == 0:  # 存在项目
               if not repo == da['repo']['name']: #项目不在文件中跳出循环
                      continue
               else:
                   pass
            else:
               pass
        #判断项目
            if da['type']==event:
                answer=answer+1
            else:
                 pass
    return answer

