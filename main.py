from PyQt5 import QtWidgets, QtCore, QtGui

import subprocess
import signal
import threading
import os, re

import UI

class Main(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rclone_exe_path = os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.exe")
        self.rclone_conf_path = os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.conf")
        self.remote = ""
        self.stop_event = threading.Event()  # 用於控制停止執行緒
        self.rclone_process = None
        self.rclone_thread = None

        self.next_1.clicked.connect(lambda: self.next_1Button())
        self.next_2.clicked.connect(lambda: self.next_2Button())
        self.back_2.clicked.connect(lambda: self.backPage())
        self.back_3.clicked.connect(lambda: self.backPage())
        self.finish.clicked.connect(lambda: self.close())

        # 創建系統托盤圖示
        self.tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon('icon.png'), self)
        self.tray_icon.show()

        # 創建圖示菜單
        self.tray_menu = QtWidgets.QMenu()
        show_action = QtWidgets.QAction("開啟", self)
        show_action.triggered.connect(self.show)
        exit_action = QtWidgets.QAction("退出", self)
        exit_action.triggered.connect(self.stop_rclone)
        exit_action.triggered.connect(app.quit)
        self.tray_menu.addAction(show_action)
        self.tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(self.tray_menu)

    
    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def close(self):
        self.hide()

    def next_1Button(self):
        # 獲取 lineEdit_remote 的值
        remote_value = self.lineEdit_remote.text()

        if remote_value == "":
            QtWidgets.QMessageBox.warning(self, "警告", "遠端名稱不能為空")
            return
        self.remote = remote_value
        # 讀取檔案
        with open(self.rclone_conf_path, "r+") as f:
            # 檢查f.read()內所有[]
            remote_list = re.findall(r"\[(.*)\]", f.read())

            # 檢查檔案內是否有遠端名稱
            if self.remote not in remote_list:
                # 如果沒有，則進行下一步設定
                self.stackedWidget.setCurrentIndex(1)
            else:
                # 如果有，則進行連線
                self.stackedWidget.setCurrentIndex(2)
                self.rclone_thread = self.run_rclone()

    def next_2Button(self):
        # 獲取 lineEdit_id, lineEdit_account, lineEdit_password, lineEdit_port 的值
        host_value = self.lineEdit_host.text()
        user_value = self.lineEdit_user.text()
        pass_value = self.lineEdit_pass.text()
        port_value = self.lineEdit_port.text()

        command = [
            os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.exe"),
            "--config",
            os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.conf"),
            "config",
            "create",
            self.remote,
            "sftp",
            f"host={host_value}",
            f"user={user_value}",
            f"pass={pass_value}",
            f"port={port_value}"
        ]

        try:
            # 使用 subprocess.run 執行 PowerShell 命令
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=True
            )

            # 顯示結果
            if result.returncode == 0:
                print("成功創建 Rclone 配置")
                print(result.stdout)
            else:
                print("創建 Rclone 配置失敗")
                print(result.stderr)

            # 切換到下一頁
            self.stackedWidget.setCurrentIndex(2)
            self.rclone_thread = self.run_rclone()

        except Exception as e:
            print(f"創建 Rclone 過程中發生錯誤: {e}")


    def backPage(self):
        self.stackedWidget.setCurrentIndex(0)


    def run_rclone(self):
        _translate = QtCore.QCoreApplication.translate
        self.info.setText(_translate("MainWindow", ""))
        # print("執行 rclone mount")
        # 讀取檔案
        try:
            command = [
                os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.exe"),
                "--config",
                os.path.join(os.path.join(os.path.dirname(__file__), "rclone-v1.68.2-windows-amd64"),"rclone.conf"),
                "mount",
                self.remote+":",
                os.path.join(os.path.dirname(__file__), "sftp"),
                "--rc"
            ]
            
            def run_rclone_in_background():
                rclone_process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )

                # 不斷檢查 stop_event，當收到停止信號時停止執行
                while not self.stop_event.is_set():
                    for line in rclone_process.stdout:
                        self.info.setText(_translate("MainWindow", line))
                    for line in rclone_process.stderr:
                        self.info.setText(_translate("MainWindow", line))

                # 如果收到停止信號，則終止 rclone 進程
                # if os.name == 'nt':  # 如果是 Windows 系統
                #     self.rclone_process.terminate()  # 直接終止進程
                # else:  # 如果是 Unix 系統
                #     self.rclone_process.send_signal(signal.SIGINT)  # 发送 SIGINT 模拟 Ctrl+C

            # 啟動背景執行緒來執行 rclone
            self.rclone_thread = threading.Thread(target=run_rclone_in_background)
            self.rclone_thread.start()

            return self.rclone_thread

        except Exception as e:
            print(f"執行 rclone mount 過程中發生錯誤: {e}")
            self.info.setText(_translate("MainWindow", str(e)))

    def stop_rclone(self):
        command = [
                "rclone",
                "rc",
                "core/quit"
            ]
        try:
            # 使用 subprocess.run 執行 PowerShell 命令
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=True
            )

            # 顯示結果
            if result.returncode == 0:
                print("成功卸載 Rclone 配置")
                print(result.stdout)
            else:
                print("卸載 Rclone 配置失敗")
                print(result.stderr)


        except Exception as e:
            print(f"卸載 Rclone 過程中發生錯誤: {e}")
        
        # 發送停止信號
        finally:
            self.stop_event.set()
            self.rclone_thread.join()
            print("Rclone 線程已停止")



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

# 指令
# rclone config
# rclone ls gdrive:
# rclone mount sftp2: C:/sftp

# 臨時環境變數
# $env:PATH += ";C:\Users\lplpl\Downloads\rclone-v1.68.2-windows-amd64"
# rclone mount remote:mountpoint --config=/path/to/your/config.conf


# def get_script_directory(self):
    #     """取得目前執行的 .py 檔案的目錄"""
    #     return os.path.dirname(os.path.abspath(__file__))


    # def create_google_drive_remote(self):
    #     # 自動化新增一個 Google Drive 遠端配置
    #     command = """rclone config
    #         n
    #         drive
    #         19
    #         your_account
    #         your_password
    #         1
            
    #         y
    #         n
    #         y"""
    #     # 將命令字串中的換行符替換成適合當前系統的換行符
    #     command = command.replace('\n', os.linesep)

    #     # 執行命令
    #     result = subprocess.run(command, shell=True, capture_output=True, text=True)
    #     print(result.stdout)
    #     print(result.stderr)