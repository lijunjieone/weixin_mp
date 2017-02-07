
CSRF_ENABLED = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

BASE_INFO_FILE = os.path.join(basedir,"baseinfo.db")
REDIRECT_FILE = os.path.join(basedir,"redirect.db")

BASE_DIR=basedir

CURRENT_INFO = ""

print "init config"

# country_list2={u'\u5173\u5c9b': 'GU', u'\u5723\u5362\u897f\u4e9a': 'LC', u'\u5df4\u5df4\u591a\u65af': 'BB', u'\u9a6c\u62c9\u7ef4': 'MW', u'\u5229\u6bd4\u4e9a': 'LY', u'\u5357\u975e': 'ZA', u'\u963f\u585e\u62dc\u7586': 'AZ', u'\u5723\u6587\u68ee\u7279\u5c9b': 'VC', u'\u5b89\u9053\u5c14\u5171\u548c\u56fd': 'AD', u'\u5308\u7259\u5229': 'HU', u'\u6cf0\u56fd': 'TH', u'\u9ece\u5df4\u5ae9': 'LB', u'\u58a8\u897f\u54e5': 'MX', u'\u5df4\u57fa\u65af\u5766': 'PK', u'\u52a0\u62ff\u5927': 'CA', u'\u4fdd\u52a0\u5229\u4e9a': 'BG', u'\u9a6c\u6765\u897f\u4e9a': 'MY', u'\u53d9\u5229\u4e9a': 'SY', u'\u767d\u4fc4\u7f57\u65af': 'BY', u'\u8499\u7279\u585e\u62c9\u7279\u5c9b': 'MS', u'\u6469\u6d1b\u54e5': 'MA', u'\u83b1\u7d22\u6258': 'LS', u'\u7231\u6c99\u5c3c\u4e9a': 'EE', u'\u624e\u4f0a\u5c14': 'ZR', u'\u521a\u679c': 'CG', u'\u5df4\u62c9\u572d': 'PY', u'\u59d4\u5185\u745e\u62c9': 'VE', u'\u585e\u820c\u5c14': 'SC', u'\u4e2d\u56fd': 'CN', u'\u4e5f\u95e8': 'YE', u'\u7eb3\u7c73\u6bd4\u4e9a': 'NA', u'\u82f1\u56fd': 'GB', u'\u73bb\u5229\u7ef4\u4e9a': 'BO', u'\u6469\u5c14\u591a\u74e6': 'MD', u'\u79d1\u5a01\u7279': 'KW', u'\u8499\u53e4': 'MN', u'\u5370\u5ea6\u5c3c\u897f\u4e9a': 'ID', u'\u65b0\u52a0\u5761': 'SG', u'\u610f\u5927\u5229': 'IT', u'\u82ac\u5170': 'FI', u'\u5965\u5730\u5229': 'AT', u'\u65af\u6d1b\u4f10\u514b': 'SK', u'\u6bdb\u91cc\u6c42\u65af': 'MU', u'\u9a6c\u91cc\u4e9a\u90a3\u7fa4\u5c9b': '\xe3\x80\x80', u'\u5188\u6bd4\u4e9a': 'GM', u'\u65b0\u897f\u5170': 'NZ', u'\u4ee5\u8272\u5217': 'IL', u'\u963f\u68ee\u677e': '\xe3\x80\x80', u'\u65af\u6d1b\u6587\u5c3c\u4e9a': 'SI', u'\u963f\u5bcc\u6c57': 'AF', u'\u5e0c\u814a': 'GR', u'\u5357\u65af\u62c9\u592b': 'YU', u'\u6c64\u52a0': 'TO', u'\u8d1d\u5b81': 'BJ', u'\u82cf\u4e39': 'SD', u'\u6d77\u5730': 'HT', u'\u65af\u5a01\u58eb\u5170': 'SZ', u'\u683c\u9c81\u5409\u4e9a': 'GE', u'\u5b89\u63d0\u74dc\u548c\u5df4\u5e03\u8fbe': 'AG', u'\u571f\u5e93\u66fc\u65af\u5766': 'TM', u'\u9999\u6e2f': 'HK', u'\u6fb3\u5927\u5229\u4e9a': 'AU', u'\u897f\u73ed\u7259': 'ES', u'\u54e5\u4f26\u6bd4\u4e9a': 'CO', u'\u591a\u7c73\u5c3c\u52a0\u5171\u548c\u56fd': 'DO', u'\u963f\u6839\u5ef7': 'AR', u'\u54e5\u65af\u8fbe\u9ece\u52a0': 'CR', u'\u585e\u6d66\u8def\u65af': 'CY', u'\u6c99\u7279\u963f\u62c9\u4f2f': 'SA', u'\u4e4c\u514b\u5170': 'UA', u'\u5723\u9a6c\u529b\u8bfa': 'SM', u'\u667a\u5229': 'CL', u'\u5c3c\u52a0\u62c9\u74dc': 'NI', u'\u7f57\u9a6c\u5c3c\u4e9a': 'RO', u'\u767e\u6155\u5927\u7fa4\u5c9b': 'BM', u'\u82cf\u91cc\u5357': 'SR', u'\u4f2f\u5229\u5179': 'BZ', u'\u8377\u5170': 'NL', u'\u54c8\u8428\u514b\u65af\u5766': 'KZ', u'\u5854\u5409\u514b\u65af\u5766': 'TJ', u'\u4e39\u9ea6': 'DK', u'\u897f\u8428\u6469\u4e9a': '', u'\u7acb\u9676\u5b9b': 'LT', u'\u5b89\u572d\u62c9\u5c9b': 'AI', u'\u745e\u5178': 'SE', u'\u7231\u5c14\u5170': 'IE', u'\u7d22\u9a6c\u91cc': 'SO', u'\u4e9a\u7f8e\u5c3c\u4e9a': 'AM', u'\u6377\u514b': 'CZ', u'\u7279\u7acb\u5c3c\u8fbe\u548c\u591a\u5df4\u54e5': 'TT', u'\u5370\u5ea6': 'IN', u'\u591a\u54e5': 'TG', u'\u632a\u5a01': 'NO', u'\u79d1\u7279\u8fea\u74e6': '\xe3\x80\x80', u'\u571f\u8033\u5176': 'TR', u'\u62c9\u8131\u7ef4\u4e9a': 'LV', u'\u963f\u66fc': 'OM', u'\u4e4c\u5179\u522b\u514b\u65af\u5766': 'UZ', u'\u4e1c\u8428\u6469\u4e9a(\u7f8e)': '\xe3\x80\x80', u'\u80af\u5c3c\u4e9a': 'KE', u'\u535a\u8328\u74e6\u7eb3': 'BW', u'\u52a0\u84ec': 'GA', u'\u76f4\u5e03\u7f57\u9640': 'GI', u'\u67ec\u57d4\u5be8': 'KH', u'\u5c3c\u65e5\u5c14': 'NE', u'\u5e03\u57fa\u7eb3\u6cd5\u7d22': 'BF', u'\u5723\u591a\u7f8e\u548c\u666e\u6797\u897f\u6bd4': 'ST', u'\u963f\u5c14\u5df4\u5c3c\u4e9a': 'AL', u'\u5384\u74dc\u591a\u5c14': 'EC', u'\u8461\u8404\u7259': 'PT', u'\u4e4d\u5f97': 'TD', u'\u4e2d\u975e\u5171\u548c\u56fd': 'CF', u'\u51e0\u5185\u4e9a': 'GN', u'\u5e93\u514b\u7fa4\u5c9b': 'CK', u'\u6cd5\u5c5e\u73bb\u5229\u5c3c\u897f\u4e9a': 'PF', u'\u6469\u7eb3\u54e5': 'MC', u'\u65e5\u672c': 'JP', u'\u5df4\u62ff\u9a6c': 'PA', u'\u7459\u9c81': 'NR', u'\u5df4\u6797': 'BH', u'\u572d\u4e9a\u90a3': 'GY', u'\u5c3c\u65e5\u5229\u4e9a': 'NG', u'\u52a0\u7eb3': 'GH', u'\u7259\u4e70\u52a0': 'JM', u'\u5df4\u54c8\u9a6c': 'BS', u'\u6ce2\u5170': 'PL', u'\u53e4\u5df4': 'CU', u'\u5409\u5e03\u63d0': 'DJ', u'\u7559\u5c3c\u65fa': '\xe3\x80\x80', u'\u5df4\u5e03\u4e9a\u65b0\u51e0\u5185\u4e9a': 'PG', u'\u6587\u83b1': 'BN', u'\u585e\u5185\u52a0\u5c14': 'SN', u'\u79d8\u9c81': 'PE', u'\u5f00\u66fc\u7fa4\u5c9b': '\xe3\x80\x80', u'\u5b89\u54e5\u62c9': 'AO', u'\u745e\u58eb': 'CH', u'\u6cd5\u5c5e\u572d\u4e9a\u90a3': 'GF', u'\u5580\u9ea6\u9686': 'CM', u'\u8428\u5c14\u74e6\u591a': 'SV', u'\u5b5f\u52a0\u62c9\u56fd': 'BD', u'\u97e9\u56fd': 'KR', u'\u57c3\u53ca': 'EG', u'\u53f0\u6e7e\u7701': 'TW', u'\u51b0\u5c9b': 'IS', u'\u9a6c\u91cc': 'ML', u'\u4f0a\u6717': 'IR', u'\u4f0a\u62c9\u514b': 'IQ', u'\u7a81\u5c3c\u65af': 'TN', u'\u6d25\u5df4\u5e03\u97e6': 'ZW', u'\u83f2\u5f8b\u5bbe': 'PH', u'\u7ea6\u65e6': 'JO', u'\u57c3\u585e\u4fc4\u6bd4\u4e9a': 'ET', u'\u5fb7\u56fd': 'DE', u'\u5766\u6851\u5c3c\u4e9a': 'TZ', u'\u9a6c\u8033\u4ed6': 'MT', u'\u6d2a\u90fd\u62c9\u65af': 'HN', u'\u5229\u6bd4\u91cc\u4e9a': 'LR', u'\u963f\u62c9\u4f2f\u8054\u5408\u914b\u957f\u56fd': 'AE', u'\u6fb3\u95e8': 'MO', u'\u585e\u62c9\u5229\u6602': 'SL', u'\u6240\u7f57\u95e8\u7fa4\u5c9b': 'SB', u'\u683c\u6797\u7eb3\u8fbe': 'GD', u'\u65af\u91cc\u5170\u5361': 'LK', u'\u4fc4\u7f57\u65af': 'RU', u'\u6cd5\u56fd': 'FR', u'\u5371\u5730\u9a6c\u62c9': 'GT', u'\u8d8a\u5357': 'VN', u'\u5e03\u9686\u8fea': 'BI', u'\u5df4\u897f': 'BR', u'\u6bd4\u5229\u65f6': 'BE', u'\u9a6c\u63d0\u5c3c\u514b': '\xe3\x80\x80', u'\u8377\u5c5e\u5b89\u7684\u5217\u65af': '\xe3\x80\x80', u'\u5723\u6587\u68ee\u7279': 'VC', u'\u7f8e\u56fd': 'US', u'\u9a6c\u5c14\u4ee3\u592b': 'MV', u'\u5217\u652f\u6566\u58eb\u767b': 'LI', u'\u8001\u631d': 'LA', u'\u83ab\u6851\u6bd4\u514b': 'MZ', u'\u5409\u5c14\u5409\u65af\u5766': 'KG', u'\u4e4c\u62c9\u572d': 'UY', u'\u5c3c\u6cca\u5c14': 'NP', u'\u6ce2\u591a\u9ece\u5404': 'PR', u'\u671d\u9c9c': 'KP', u'\u963f\u5c14\u53ca\u5229\u4e9a': 'DZ', u'\u5361\u5854\u5c14': 'QA', u'\u8d5e\u6bd4\u4e9a': 'ZM', u'\u7f05\u7538': 'MM', u'\u5362\u68ee\u5821': 'LU', u'\u6590\u6d4e': 'FJ', u'\u9a6c\u8fbe\u52a0\u65af\u52a0': 'MG', u'\u4e4c\u5e72\u8fbe': 'UG'}

UPLOAD_FOLDER = '%s/static/uploads/'%(basedir)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','apk'])


class Country:
    cn_name=""
    code="CN"
    en_name="China"


import json
COUNTRY_CODE_LIST=[]
def obtainAllCountry():
    print "init country data"
    country_json="%s/countrys.json"%(BASE_DIR)
    content=open(country_json).read()
    content_json=json.loads(content)
    countrys={}
    for country in content_json:
        c=Country()
        c.cn_name=country["cn"]
        c.code=country["code"]
        c.en_name=country["en"]
        COUNTRY_CODE_LIST.append(c)
        countrys[c.cn_name]=c

    return countrys


COUNTRY_LIST=obtainAllCountry()



