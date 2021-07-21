一· 根据地平线提供的excel表整理后批量上传jira
jira2.py
本工具是根据地平线提供的问题表格完成理想内jira上传。上传时只需修改excel name即可。
整理表格注意事项：（excel是xls结尾）
1.第一个sheet：基本信息。里面包含车辆vin码，软件版本和预计修复日期。
2.第二个sheet：默认以日期命名。  第一行时间点的格式：2021年3月25日 12:15:43。E列为是否为感知问题。
                         K列为bad case pack名称。O列为所属模块，比如：ACC,LKA。
3.第三个sheet：link_path。将地平线所给的pack按日期上传到 http://fileshare.it.chehejia.com:5000/，之后以分享的形式使得pack name和所生成的链接一一对应，之后保存。excel表中需要注意的是第一列pack name是纯pack name，
                          从网址上copy 过来的带有路径，此时需要把路径删掉。
二.APA测试批量上传jira
apa_jira.py
