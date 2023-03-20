import re

def company_entity_extraction(title):
    raw_title = str(title)
    r_str = re.search('(^[2023, 2022].*)|(.*[2023, 2022])', raw_title)
    if r_str:
        tmp = r_str.group()
    else:
        print(raw_title)
        tmp = raw_title
    tmp.strip()
    tmp = tmp.replace(' ', '').replace('招聘', '').replace('公告', '').replace('2023', '').replace('2022', '').replace('秋季', '').replace('春季', '').replace('-', '').replace('23', '').replace('22', '').replace('【', '').replace('】', '').replace('校园', '').replace('届', '').replace('年', '').replace('宣讲会', '')
    if '信息汇总' in raw_title:
        tmp = None
    if not r_str:
        print(tmp)
    return tmp
