# -*- coding: utf-8 -*-

import subprocess
import threading
import os

# 定义要执行的命令列表
commands = [
    'free -h',
    'vmstat',
    'iostat',
    'dmesg',
    'uptime',
    'top -n 1',
    'tail -n 10 /var/log/syslog',  # 使用tail -n获取文件的最后10行内容
    'tail -n 10 /var/log/messages',  # 使用tail -n获取文件的最后10行内容
    'journalctl -xe',
    'last',
    'who'
]

# 定义执行命令的函数
def execute_command(command):
    output = subprocess.check_output(command, shell=True)
    with open('search-result.txt', 'a') as file:
        file.write("执行命令 {} 的输出：\n{}\n".format(command, output.decode('utf-8')))

# 创建线程来执行每个命令
threads = []
for command in commands:
    thread = threading.Thread(target=execute_command, args=(command,))
    threads.append(thread)
    thread.start()

# 等待所有线程执行完成，最长等待时间为10秒
for thread in threads:
    thread.join(timeout=10)

print("所有命令执行完成，并将结果导入到output.txt文件中。")