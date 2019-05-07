# import src.add_food as add_food
import time
import src.add_times as add_times

if __name__ == "__main__":
    try:
        print("开始填写!")
        print(add_times.add_times())
    finally:
        print("5秒后自动退出")
        time.sleep(5)
