import requests
import json
import datetime


def add_food():
    url = "http://old.chaojibiaoge.com/index.php/System/Model/saveFormData"
    headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "need_return_newid": True,
        "tablename": "oa_sheet",
        "fieldvalues": "SYS_ROWID<=>~|~sort<=>100~|~column_1<=>系统软件部~|~column_2<=>四处~|~column_3<=>何翔龙~|~column_4<=>9302~|~column_5<=>开发~|~column_6<=>1~|~column_7<=>~|~SYS_string1<=>~|~SYS_string2<=>~|~SYS_string3<=>~|~SYS_EDITTIME<=>~|~SYS_EDITUSER<=>~|~SYS_ADDTIME<=>~|~SYS_ADDUSER<=>~|~SYS_ADDIP<=>~|~DIANZANCOUNT<=>~|~id<=>18121420250971621620~|~projectid<=>18121416514324249003~|~SYS_FORMATE<=>~|~activecell<=>",
        "modelid": "oa_sheet",
        "usermodel_recordid": "18121416514324249003",
        "user": "3116770262@qq.com",
        "sharekey": ""
    }
    res = requests.post(url, data=data, headers=headers1)
    print(res.json())
