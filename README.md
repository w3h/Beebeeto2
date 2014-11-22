Beebeeto2
=========

为了使得beebeeto的框架在各位手中得到最大化的利用，同时也希望更多的人参与到beebeeto的项目中，贡献更多的高质量的POC，我在原框架基础上做了一些优化。主要增加功能如下

    1、增加POC更新功能（这个就是哪个下载器，不过修改了一点点，就是增量下载，呵呵）

    2、增加POC动态加载功能（更新下来的POC可以直接使用，当然前提是你写的POC没问题）

    3、增加指定应用程序，执行定向测试（如指定dedecms，就执行所有包含dedecms的poc）



【应用实例-POC更新】

D:\Beebeeto2>beebee.py --update "csrftoken=10UVqALJTnkV65RHmgNbTO9TJ6YfoRxL; CNZZDATA1253290531=925436804-1416563556-%7C1416563556; sessionid=9b2i7df9dj3nfzfbo8g7rt40l8p9sm7z"

[+] Get Poc -> poc-2014-0141 

[+] Get Poc -> poc-2014-0134 

[*] Get Poc -> poc-2014-0130 failed

[*] Get Poc -> poc-2014-0119 failed

[*] Get Poc -> poc-2014-0114 failed

[*] Get Poc -> poc-2014-0110 failed

[+] Get Poc -> poc-2014-0100 

[+] Get Poc -> poc-2014-0098 

[*] Get Poc -> poc-2014-0094 failed

[+] The total number of POC is 4


【应用实例-定向测试】

D:\Beebeeto2>beebee.py -t http://127.0.0.1 -n dedecms

 [+] Beebeeto.demo.poc_2014_0015                        None

 [+] Beebeeto.demo.poc_2014_0065                        None

 [+] Beebeeto.demo.poc_2014_0070                        None

 [+] Beebeeto.demo.poc_2014_0071                        None

 [+] Beebeeto.demo.poc_2014_0077                        False

 [+] Beebeeto.demo.poc_2014_0084                        False

 [+] Beebeeto.demo.poc_2014_0128                        False
