import add_food
import add_times
import time

if __name__ == "__main__":
    while 1:
        flag = 0
        print("* 1:填工时\n* 2:填餐票\n* 0:退出")
        flag = int(input("输入参数："))
        if flag == 0:
            print("退出中...")
            time.sleep(2)
            break
        if flag == 1:
            add_times.add_times()
        if flag == 2:
            add_food.add_food()
