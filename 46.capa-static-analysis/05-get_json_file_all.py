#coding:utf-8
#By:Eastmount CSDN 2023-03-14
import os
import json
from jsonsearch import JsonSearch

def getAllFiles(targetDir):
    listFiles = os.listdir(targetDir)
    return listFiles

apt_path = r"D:\capa\result"
apt_name = ['AAAA']

apt_list = []          #组织名称
pe_md5_list = []       #恶意软件文件名称
tactic_list = []       #攻击ATT&CK框架Tactic
technique_list = []    #攻击ATT&CK框架Technique
id_list = []           #攻击ATT&CK框架类别

i = 0
while i<len(apt_name):
    file_name = apt_path + "\\" + str(apt_name[i])
    print(file_name)

    apt_list.append("AAAA")
    files = getAllFiles(file_name)
    for name in files:
        jsonName = file_name + "\\" +  str(name)
        print(jsonName)
        pe_md5_list.append(jsonName)

        #打开json文件
        with open(jsonName) as fp:
            data = json.load(fp)
            #print(data)
            print(data.keys())
            #dict_keys(['meta', 'rules'])
            #包含meta和rules两大块内容 静态行为及API在rules部分

            #提取ATT&CK特征
            behavior = data["rules"]
            print(behavior)

            #查找attack对应的所有值
            jsondata = JsonSearch(object=behavior, mode='j')
            attack = jsondata.search_all_value(key='attack')
            print(attack)
            print(len(attack))

            #提取tactic、technique和id
            tactic_str = ""
            technique_str = ""
            id_str = ""
            for n in attack:
                if len(n)>0:
                    #print(n,type(n))
                    value = n[0]
                    print(value,type(value))
                    tactic_str += str(value['tactic']) + ";"
                    technique_str += str(value['technique']) + ";"
                    id_str += str(value['id']) + ";"
            else:
                print("over!!!")
        print(tactic_str, technique_str, id_str)
        tactic_list.append(tactic_str)
        technique_list.append(technique_str)
        id_list.append(id_str)
        break
    i += 1
    break
