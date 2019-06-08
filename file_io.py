import re

log_lines=None
with open(r"C:\Users\remote_pc\Desktop\python_log2.txt",'r',encoding='utf-8') as log_txt:
    log_lines=log_txt.readlines()

machine_policty_logs={}
for line in log_lines:
    if 'Machine policy' in line:
        re_result_time=re.findall(r'\[\d+:\d+:\d+:\d+\]',line)[0].replace('[','').replace(']','')
        machine_policty_logs[re_result_time]=line

for item in machine_policty_logs.items():
    print(item)
# ---------------------------------------------------------------------------------------------------------
r_cbs=[]
package=[]
with open(r"C:\Users\remote_pc\Desktop\CBS.log",'r',encoding='utf8') as file:
    r_cbs.extend(file.readlines())
print(r_cbs)

for line in r_cbs:
    if ', Package: ' in line:
        sp_split=line.split(', Package: ')[1].split(', ')[0]
        package.append(sp_split)

[print(pkg) for pkg in set(package)]
