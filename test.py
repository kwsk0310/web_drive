import subprocess, re, os

# subprocess.run(['cd', 'C:/'], shell=True, capture_output=True, text=True)
# log = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
# print("1:", log)
# print("2:", log.stdout)

# with open("rclone.conf", "r+") as f:
#     # 檢查f.read()內所有[]
#     result = re.findall(r"\[(.*)\]", f.read())

print(os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.conf"))     
