__author__ = 'Xing'
import os
import subprocess
path1 = os.environ.get('RECOGNITION_PATH') + "/validation/"
path2 = os.environ.get('DATA_PATH')
def get_linux_file_size(file_name):
    print("ls -l " + path2 + file_name + " |awk '{print $5}'")
    a=os.popen("ls -l " + path2 + file_name + " |awk '{print $5}'")
    a1=a.readlines()
    return int(a1[0][:-1])
    # return 1

def get_hive_file(path2,tablename):
    print("rm -rf " + path2 + tablename)
    os.system("rm -rf " + path2 + tablename)
    print("hadoop fs -get /user/hive/warehouse/"+tablename+' ' + path2)
    os.system("hadoop fs -get /user/hive/warehouse/"+tablename+' ' + path2)
    print("cat " + path2 + tablename + "/* > " + path2 +tablename+ ".txt")
    os.system("cat " + path2 + tablename + "/* > " + path2 + tablename+ ".txt")

def exec_sql(sql):
    f11 = codecs.open(path2+"/rule_unreasonable.sql", 'w', 'utf-8')  # 写入验证结果
    f11.writelines(sql)
    f11.close()
    print("hive -f " + path2 + "/rule_unreasonable.sql")
    os.system("hive -f " + path2 + "/rule_unreasonable.sql")


# popen可以返回值，而os.system不行
# a=os.popen("ls -l "+path2+"symptom_tongyici_v2.txt"+" |awk '{print $5}'")
# num=a.read()
# print(num[:-1])
# print(type(num))
#
# print(get_linux_file_size('symptom_tongyici_v2.txt'))

# b=os.popen('cat '+path2+'letter_in.txt')
# print(b.read())
# print(b.readlines())

# output=subprocess.call(["ls", "-l",path2+"symptom_tongyici_v2.txt"])


import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line)
retval = p.wait()
print(retval)


