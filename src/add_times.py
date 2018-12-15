import requests
import json
import datetime
import random


def add_times(account="LCBJ09302", password="hxl123456"):
    times_url = "http://10.7.13.26:9080/times"
    headers1 = {'Content-Type': 'application/x-www-form-urlencoded'}

    login_url = times_url + "/login/validate"
    login_data = {"userName": account, "password": password}
    login_result = requests.post(login_url, data=login_data, headers=headers1)

    cookies_dict = login_result.request._cookies.get_dict()
    cookies_str = "JSESSIONID" + "=" + cookies_dict["JSESSIONID"]
    print(cookies_str)

    headers2 = {"Cookie": cookies_str,
                'Content-Type': 'application/x-www-form-urlencoded'}

    adddetail_url = times_url + "/times/adddetail"
    workdate = datetime.datetime.now().strftime('%Y-%m-%d')
    worktime = str(random.randint(9, 11))
    params = {
        "userid": account,
        "workdate": workdate,
        "firstclass": "CDT工时",
        "projectid": "680",
        "projectleader": "褚福州",
        "worktime": worktime,
        "memo": "开发"
    }
    adddetail_result = requests.post(
        adddetail_url, params=params, headers=headers2)
    print(adddetail_result.text)

    get_times_list_url = times_url + "/times/timesdetaillist?columns[0][data]=id&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=times&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=project_name&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=projectlead&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=workd_time&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=statusInfo&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=memo&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&start=0&length=30&search[value]=&search[regex]=false&userid="+account+"&status=10&_=1544773669473"
    get_times_list_result = requests.get(get_times_list_url, headers=headers2)
    res_json = json.loads(get_times_list_result.text)

    item_id = res_json["data"][0]["id"]
    print(item_id)

    submit_url = times_url + "/times/submittimesfirst"
    data = {"ids[]": item_id}
    print(requests.post(submit_url, data=data, headers=headers2).text)
