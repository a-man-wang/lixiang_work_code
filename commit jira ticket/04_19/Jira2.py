import xlrd
import json
import shutil
import time,os
from jira import JIRA

jira = JIRA('http://jira.it.chehejia.com/', auth=('aichao', 'SuperMan0111'))
# print(jira.projects())
project = jira.project('NOAP')

prob_freq_dict = {'总是': '10100','有时': '10101','偶尔': '10102'}
components_id_dict = {
    'ACC':'19701',
    'AEB':'19706',
    'ALC':'19709',
    'AP':'19704',
    'APA':'19710',
    'APO':'19711',
    'ASL':'19717',
    'BSD':'19707',
    'DOW':'19712',
    'FCTA':'19713',
    'FCW':'19705',
    'IHC':'19708',
    'LCA':'19700',
    'LDW':'19703',
    'LIOS':'19718',
    'LKA':'19702',
    'NOA控制器-J3软件':'19554',
    'NOA控制器-MCU软件':'19553',
    'NOA控制器-硬件':'19555',
    'RCTA':'19715',
    'TJA':'19716',
    'TLSI':'19714',
    '其他':'19719'
}
# allfields = project.fields()
# name_map = {field['name']:field['id'] for field in allfields}
# print(name_map)
# print("001",project.id)
# print("002",project.name)
# print("003",project.components)
# print("004",project.versions)
# print("005",project.raw)

# issue = jira.issue('NOAP-456')
# meta = jira.editmeta(issue)
# print(meta['fields']['customfield_13103']['allowedValues'])
# print(issue.key, issue.fields.summary, issue.fields.status)
# print("001",issue.fields.customfield_16801)
# print("002",issue.fields.summary)
# print("003",issue.fields.priority.id)
# print("004",issue.fields.customfield_10816.id)
# print("005",issue.raw)

summary_content = ''
components_id = 0
sw_version = ''
bug_time = ''
vin = ''
prob_freq_id = ''
fix_date = ''
description_content = ''
pack_link = ''
def Create_issue(summary_content, components_id, sw_version, bug_time, vin, fix_date, pack_link):
    issue_dict= {
        'project': {'id': project.id},#项目
        'issuetype': {'id':'10703'},#问题类型
        'customfield_10816':{'id':'15729'},#项目名称
        'customfield_16801':{'id':'17705'},#报告人部门
        'assignee': {'name': 'yongqiang.cui_9233'},#经办人
        'summary': summary_content,#概要@@@@@@@@@@@@@@@@@@@@@@@@@
        'customfield_11111': {'id':'17396'},#问题优先级
        'components':[{'id': components_id}],#模块@@@@@@@@@@@@@@@@@@@@@@@@
        'customfield_11107': sw_version,#发现软件版本@@@@@@@@@@@@@@@@@@@@@@@1111
        'customfield_10401':{'id': '10402'},#问题严重程度
        'customfield_10749': {'id': '17603'},#测试环境
        'customfield_13109': bug_time,#Bug发生时车机系统时间@@@@@@@@@@@@@@@@
        'customfield_10750': vin,#车辆VIN号@@@@@@@@@@@@@@11111
        'customfield_10101': {'id': '10102'},#问题复现率@@@@@@@@@@@@@@@@@@@@@@@@@@
        'customfield_10307': fix_date,#计划关闭日期@@@@@@@@@@@@@@@@111111
        'customfield_13103':{'id': '17388'},#问题类别
        'description': pack_link#描述@@@@@@@@@@@@@@@@@@@@@@@@
    }
    new_issue = jira.create_issue(fields=issue_dict)

def Extract_Info(file_name):
    File_Info = xlrd.open_workbook(file_name)
    basic_table = File_Info.sheet_by_index(0)
    issue_table = File_Info.sheet_by_index(1)
    path_table = File_Info.sheet_by_index(2)
    # file_num = path_table.nrows()
    link_dict = {}
    keys = path_table.col_values(0)
    vals = path_table.col_values(1)
    link_dict = dict(zip(keys,vals))


    vin_src = basic_table.cell_value(0,1)
    sw_version_src = basic_table.cell_value(1,1)
    fix_date_src = basic_table.cell_value(2,1)


    items_num = issue_table.nrows
    for i in range(1,items_num):
        # type = issue_table.cell_value(i,4)
        issue_info = issue_table.row_values(i)
        if issue_info[4] == 'Y':
            # issue_info = issue_table.row_values(i)
            bug_time_src = issue_info[0].replace('年','-').replace('月','-').replace('日','').replace(' ','T') + '.000+0800'
            summary_content_src = issue_info[1]
            components_id_src = components_id_dict[issue_info[14]]
            # prob_freq_id_src = prob_freq_dict[basic_info[15]]
            pack_link_src = "pack名称： " + issue_info[10] + '\n' + "pack地址： " + link_dict[issue_info[10]]
            Create_issue(summary_content_src, components_id_src, sw_version_src, bug_time_src, vin_src, fix_date_src, pack_link_src)
        else:
            continue

# def Jira_update(bug_odr):
#     issue = jira.issue(bug_odr)
#     des = (issue.fields.description)[8::]
#     matflag = 0
#     for key in all_dict.keys():
#         if des == key:
#             new_des = "pack名称： " + all_dict[key] + '\n' "pack地址： " + key
#             matflag = 1
#
#     if matflag == 0:
#         print(bug_odr,des)
#     issue.update(fields={
#         # 'assignee': {'name': 'yongqiang.cui_9233'},
#         'description': new_des
#     })



if __name__ == '__main__':
    #创建JIRA问题
    Extract_Info('../04_19/20210413.xls')

    #更新JIRA问题
    # upf_list = []
    # all_dict = {}
    # all_list = os.listdir('./')
    # for upf in all_list:
    #     if 'xls'  in upf:
    #         link_dict = {}
    #         tab_path = upf
    #         File_Info = xlrd.open_workbook(tab_path)
    #         path_table = File_Info.sheet_by_index(2)
    #         keys = path_table.col_values(1)
    #         vals = path_table.col_values(0)
    #         link_dict = dict(zip(keys,vals))
    #         all_dict.update(link_dict)
    # Jira_update('NOAP-506')
    # for odr in range(497,506):
    #     bug_odr = 'NOAP-' + str(odr)
    #     Jira_update(bug_odr)
    # for odr in range(634,669):
    #     bug_odr = 'NOAP-' + str(odr)
    #     Jira_update(bug_odr)
    # for odr in range(670,697):
    #     bug_odr = 'NOAP-' + str(odr)
    #     Jira_update(bug_odr)