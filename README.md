# Cli-Translation
a command line translator script written in python3.

## Requirements:
- googletrans
- requests

## Usage:
Download the trans.py file and install requirements using pip.
then:
```bash
sudo mv trans.py /usr/local/bin/
cd /usr/local/bin/
sudo chmod +x trans.py
exit
```
open a new shell and type：
```bash
trans.py -h
trans.py -d zh-CN hello world
trans.py good morning
trans.py -s recall
trans.py 早上好
```
you can use it to translate all language.

更多使用细节参见：http://blog.niuhemoon.xyz/pages/2018/06/06/Python-CommandLine-Translator/


