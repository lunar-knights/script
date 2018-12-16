import os

path = os.path.split(os.path.realpath(__file__))[0]

req_path = path + "/requirements.txt"

pkg_ins_cmd = "pip install -r " + req_path

ico_path = path + "/ico/p2.ico"
main_path = path + "/main/main.py"
main_pyins_cmd = "pyinstaller -F -i " + ico_path + " " + main_path

ico_path = path + "/ico/p1.ico"
main_path = path + "/main/main_gui.py"
main_gui_pyins_cmd = "pyinstaller -F -w -i " + ico_path + " " + main_path

os.system(pkg_ins_cmd)
os.system(main_pyins_cmd)
os.system(main_gui_pyins_cmd)
