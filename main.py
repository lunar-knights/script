import add_food
import add_times
import time

if __name__ == "__main__":
    while 1:
        flag = 0
        print("* 1:填工时\n* 2:填餐票\n* 0:退出")
        try:
            flag = int(input("输入参数："))
        except Exception:
            print("参数类型错误!\n")
            time.sleep(0.5)
            continue
        if flag == 0:
            print("退出中...")
            time.sleep(1)
            break
        if flag == 1:
            add_times.add_times()
        if flag == 2:
            add_food.add_food()
