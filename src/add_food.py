import requests
import json
import datetime


def add_food(user_id="9302", user_name="何翔龙"):
    url_get_list = "http://old.chaojibiaoge.com/index.php/Oa/Folder/getMyFolderAndFiles"
    headers1 = {'Cookie': 'Hm_lvt_35a20a00be201fa9a257e423b6f54444=1545008576,1545009979,1545030021,1545037069; PHPSESSID=telhf4n53ardto278mdhpuh370; mcss_loginuser=3116770262@qq.com; mcss_corpName=undefined; mcss_staffCode=undefined; mcss_lastloginuser=3116770262@qq.com; mcss_haslogin=yes; Hm_lpvt_35a20a00be201fa9a257e423b6f54444=1545037486; lastFolder=MailFolder; lastFileUpdateTime=2018-12-17%2016%3A52%3A19'}
    res = requests.get(url_get_list, headers=headers1)
    file_list = res.json()["files"]
    f_id = ""
    for f in file_list:
        idx = f["name"].find("10F")
        if idx >= 0:
            f_id = f["id"]
            break

    if f_id == "":
        return "查表错误！"

    url = "http://old.chaojibiaoge.com/index.php/System/Model/saveFormData"
    headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "need_return_newid": True,
        "tablename": "oa_sheet",
        "fieldvalues": "SYS_ROWID<=>~|~sort<=>100~|~column_1<=>系统软件部~|~column_2<=>四处~|~column_3<=>"+user_name+"~|~column_4<=>"+user_id+"~|~column_5<=>开发~|~column_6<=>1~|~column_7<=>~|~SYS_string1<=>~|~SYS_string2<=>~|~SYS_string3<=>~|~SYS_EDITTIME<=>~|~SYS_EDITUSER<=>~|~SYS_ADDTIME<=>~|~SYS_ADDUSER<=>~|~SYS_ADDIP<=>~|~DIANZANCOUNT<=>~|~id<=>18121420250971621620~|~projectid<=>"+f_id+"~|~SYS_FORMATE<=>~|~activecell<=>",
        "modelid": "oa_sheet",
        "usermodel_recordid": f_id,
        "user": "3116770262@qq.com",
        "sharekey": ""
    }
    res = requests.post(url, data=data, headers=headers1)
    print(res.json())
    return res.json()
