import os
path = os.path.split(os.path.realpath(__file__))[0]

req_path = path+"/requirements.txt"
ico_path = path + "/ico/p2.ico"
main_path = path + "/main/main.py"

pkg_ins_cmd = "pip install -r " + req_path
main_pyins_cmd = "pyinstaller -F -i " + ico_path + " " + main_path

os.system(pkg_ins_cmd)
os.system(main_pyins_cmd)
