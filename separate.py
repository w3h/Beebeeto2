#!/usr/bin/env python
#coding=utf8
import os
import re
import shutil
import codecs
import chardet

def get_tag(head, info):
    gr = re.findall("'"+ head +"': ({[\s\S]*?})", info)
    if len(gr) == 0 or not gr:
        return 

    ret = "".join(gr[0])
    ret = eval(ret)
    return ret
    

def write_init(fp):
    info = '''#!/usr/bin/env python
#coding=utf-8

import os,sys  
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir)   
'''
    if not os.path.isfile(fp + "./__init__.py"):
        open(fp + "./__init__.py", "w").write(info)


def format_csv(info):
    info = "".join(info).strip()
    try: 
        reinfo = str(info).decode("utf8").encode("gbk")
    except:
        reinfo = info

    info = reinfo
    if "," in info:
        return '"'+info +'"'
    else:
        return info


def write_index(fp, name, info):
    import csv
    csvfile = None
    fp = fp + "/index.csv"
    if not os.path.isfile(fp):
        csvfile = file(fp, 'wb') 
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'app_name', 'vul_version', 'type', 'desc', 'references'])
    else:
        csvfile = file(fp, 'a') 
        writer = csv.writer(csvfile)

    vul = get_tag("vul", info)
    app_name = format_csv(vul["app_name"])
    vul_version = format_csv(vul["vul_version"])
    typename =  format_csv(vul["type"])
    desc = format_csv(vul["desc"])
    references = format_csv(vul["references"])
    data = [(name, app_name, vul_version, typename, desc, references),]
    writer.writerows(data)
    csvfile.close()    


def load_exp():
    file_list = [f for f in os.listdir(os.path.join(os.getcwd(), "./poc/"))]
    _all_plugins = [os.path.splitext(f)[0] for f in file_list if os.path.splitext(f)[1] == '.py']
    _all_dir = [f for f in file_list if not os.path.isfile("./poc/" + f)]

    try: _all_plugins.remove('__init__') 
    except: pass
    try: _all_plugins.remove('baseframe') 
    except: pass

    for i in _all_plugins:
        print i
        info = open("./poc/" + i + ".py").read()
        tagtmp = get_tag("vul", info)
        if not tagtmp:
            continue

        name = get_tag("vul", info)["app_name"]
        if name.find(' ') >= 0: name = name[0:name.find(' ')]
        flag = False
        for f in _all_dir:
            if name.lower() == f.lower():
                try:
                    write_init("./poc/" + f)
                    write_index("./poc/" + f, i, info)
                    shutil.move("./poc/" + i + ".py", "./poc/" + f + "/" + i + ".py")
                except Exception,e:
                    #print e
                    #return
                    break
                flag = True
                break

        if not flag:
            print "[X] ",i,name

load_exp()
