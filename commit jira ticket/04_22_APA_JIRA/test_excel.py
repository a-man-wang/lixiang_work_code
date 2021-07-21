import xlrd

components_id_dict = {
    'ACC': '19701',
    'AEB': '19706',
    'ALC': '19709',
    'AP': '19704',
    'APA': '19710',
    'APO': '19711',
    'ASL': '19717',
    'BSD': '19707',
    'DOW': '19712',
    'FCTA': '19713',
    'FCW': '19705',
    'IHC': '19708',
    'LCA': '19700',
    'LDW': '19703',
    'LIOS': '19718',
    'LKA': '19702',
    'NOA控制器-J3软件': '19554',
    'NOA控制器-MCU软件': '19553',
    'NOA控制器-硬件': '19555',
    'RCTA': '19715',
    'TJA': '19716',
    'TLSI': '19714',
    '其他': '19719'
}


def Extract_Info(file_name):
    File_Info = xlrd.open_workbook(file_name)
    basic_table = File_Info.sheet_by_index(0)
    issue_table = File_Info.sheet_by_index(1)
    # 车辆vin码
    vin_src = basic_table.cell_value(0, 1)
    # 测试的软件版本
    sw_version_src = basic_table.cell_value(1, 1)
    # 预计修复时间
    fix_date_src = basic_table.cell_value(2, 1)
    # 问题等级
    issue_level = {
        'S': '10401',
        'A': '10402',
        'B': '10403',
        'C': '10404',
        'D': '10405'
    }

    items_num = issue_table.nrows
    for i in range(1, items_num):
        # type = issue_table.cell_value(i,4)
        issue_info = issue_table.row_values(i)
        # bug发生时间
        bug_time_src = issue_info[0].replace('年', '-').replace('月', '-').replace('日', '').replace(' ',
                                                                                                  'T') + '.000+0800'
        # 问题概要
        summary_content_src = '[APA]' + issue_info[1]
        # 地点
        test_place = issue_info[2]
        # 停车位类型
        parking_type = issue_info[3]
        # 测试步骤
        test_step = issue_info[4]
        # 实际结果
        current_result = issue_info[5]
        # 期待的结果
        expect_result = issue_info[6]
        # 问题等级
        custom_field_level = issue_level[issue_info[8]]

        # 所属模块
        components_id_src = components_id_dict[issue_info[9]]
        issue_description = '1.地点: ' + test_place + '\n2.停车位类型: ' + parking_type + '\n3.测试时间： ' + issue_info[0] + '\n4.测试步骤: ' + test_step + '\n5.实际结果： ' + current_result + '\n6.期待结果： ' + expect_result
        print(vin_src, sw_version_src, fix_date_src, bug_time_src, summary_content_src, issue_description,
              custom_field_level, components_id_src)
Extract_Info('APA_template.xls')