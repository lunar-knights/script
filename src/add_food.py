import requests
import json
import datetime
import time


def add_food(user_id="9302", user_name="何翔龙"):
    url_login = "http://old.chaojibiaoge.com/index.php/Home/ULogin/gotoLogin/"
    headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "registTag": "web",
        "username": "3116770262@qq.com",
        "password": "33357c32357c31357c30357c3934",
        "sceneId": "",
        "sharekey": "",
        "logintype": "undefined"
    }
    res = requests.post(url_login, data=data, headers=headers1)
    cookies_dict = res.cookies._cookies["old.chaojibiaoge.com"]["/"]["PHPSESSID"]

    cookies_str = "PHPSESSID=" + cookies_dict.value

    url_get_list = "http://old.chaojibiaoge.com/index.php/Oa/Folder/getMyFolderAndFiles"
    headers1 = {'Cookie': 'Hm_lvt_35a20a00be201fa9a257e423b6f54444=1545008576,1545009979,1545030021,1545037069; '+cookies_str +
                '; mcss_loginuser=3116770262@qq.com; mcss_corpName=undefined; mcss_staffCode=undefined; mcss_lastloginuser=3116770262@qq.com; mcss_haslogin=yes; Hm_lpvt_35a20a00be201fa9a257e423b6f54444=1545037486; lastFolder=MailFolder; lastFileUpdateTime=2018-12-17%2016%3A52%3A19'}
    res = requests.get(url_get_list, headers=headers1)
    file_list = res.json()["files"]
    f_id = ""
    for f in file_list:
        idx = f["name"].find("11F")
        if idx >= 0:
            f_id = f["id"]
            break

    if f_id == "":
        return "查表错误！"

    id = "18121420250966621720"
    st = str(int(time.time()))[0:-2]
    id = id[0:-8] + st

    url = "http://old.chaojibiaoge.com/index.php/System/Model/saveFormData"
    headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "need_return_newid": True,
        "tablename": "oa_sheet",
        "fieldvalues": "SYS_ROWID<=>~|~sort<=>100~|~column_1<=>系统软件部~|~column_2<=>四处~|~column_3<=>"+user_name+"~|~column_4<=>"+user_id+"~|~column_5<=>开发~|~column_6<=>1~|~column_7<=>~|~SYS_string1<=>~|~SYS_string2<=>~|~SYS_string3<=>~|~SYS_EDITTIME<=>~|~SYS_EDITUSER<=>~|~SYS_ADDTIME<=>~|~SYS_ADDUSER<=>~|~SYS_ADDIP<=>~|~DIANZANCOUNT<=>~|~id<=>"+id+"~|~projectid<=>"+f_id+"~|~SYS_FORMATE<=>~|~activecell<=>",
        "modelid": "oa_sheet",
        "usermodel_recordid": f_id,
        "user": "3116770262@qq.com",
        "sharekey": ""
    }
    res = requests.post(url, data=data, headers=headers1)
    print(res.json())
    return res.json()

if __name__ == "__main__":
    add_food()
