#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time


class StringGui(object):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本工具集_v1.0")  # 窗口名
        self.init_window_name.geometry('685x390+10+10')
        label_color = "lightgray"
        button_color = "lightblue"
        self.init_window_name["bg"] = label_color  # 窗口背景色
        # 标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据", bg=label_color)
        self.init_data_label.grid(row=0, column=0, sticky=W)
        self.result_data_label = Label(self.init_window_name, text="输出结果", bg=label_color)
        self.result_data_label.grid(row=0, column=12, sticky=W)
        self.log_label = Label(self.init_window_name, text="日志", bg=label_color)
        self.log_label.grid(row=12, column=0, sticky=W)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=40, height=16)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=40, height=16)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=96, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=22)
        scroll_bar = Scrollbar(command=self.log_data_Text.yview, width=1)
        scroll_bar.grid(row=13, column=21, sticky=S + W + E + N)
        self.log_data_Text.config(yscrollcommand=scroll_bar.set)
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg=button_color, width=15,
                                              command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_trans_to_sha1_button = Button(self.init_window_name, text="字符串转sha1", bg=button_color, width=15,
                                               command=self.str_trans_to_sha1)
        self.str_trans_to_sha1_button.grid(row=2, column=11)
        self.str_trans_to_sha256_button = Button(self.init_window_name, text="字符串转sha256", bg=button_color, width=15,
                                                 command=self.str_trans_to_sha256)
        self.str_trans_to_sha256_button.grid(row=3, column=11)
        self.str_trans_to_sha512_button = Button(self.init_window_name, text="字符串转sha512", bg=button_color, width=15,
                                                 command=self.str_trans_to_sha512)
        self.str_trans_to_sha512_button.grid(row=4, column=11)
        self.stamp_trans_to_time_button = Button(self.init_window_name, text="时间戳(S)转时间", bg=button_color, width=15,
                                                 command=self.stamp_trans_to_time)
        self.stamp_trans_to_time_button.grid(row=5, column=11)
        self.time_trans_to_stamp_button = Button(self.init_window_name, text="时间转时间戳(S)", bg=button_color, width=15,
                                                 command=self.time_trans_to_stamp)
        self.time_trans_to_stamp_button.grid(row=6, column=11)
        self.clear_button = Button(self.init_window_name, text="clear log", bg=button_color, width=10,
                                   command=self.clear_log)
        self.clear_button.grid(row=12, column=20, sticky=E)

    # 功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                md5 = hashlib.md5()
                md5.update(src)
                md5_digest = md5.hexdigest()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, md5_digest)
                self.write_log_to_text("INFO:str_trans_to_md5 success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_text("ERROR:str_trans_to_md5 failed")

    def str_trans_to_sha1(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                sha1 = hashlib.sha1()
                sha1.update(src)
                sha1_digest = sha1.hexdigest()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, sha1_digest)
                self.write_log_to_text("INFO:str_trans_to_sha1 success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转SHA1失败")
        else:
            self.write_log_to_text("ERROR:str_trans_to_sha1 failed")

    def str_trans_to_sha256(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                sha256 = hashlib.sha256()
                sha256.update(src)
                sha256_digest = sha256.hexdigest()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, sha256_digest)
                self.write_log_to_text("INFO:str_trans_to_sha256 success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转SHA256失败")
        else:
            self.write_log_to_text("ERROR:str_trans_to_sha256 failed")

    def str_trans_to_sha512(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                sha512 = hashlib.sha512()
                sha512.update(src)
                sha512_digest = sha512.hexdigest()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, sha512_digest)
                self.write_log_to_text("INFO:str_trans_to_sha512 success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转SHA512失败")
        else:
            self.write_log_to_text("ERROR:str_trans_to_sha512 failed")

    def stamp_trans_to_time(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                time_array = time.localtime(int(src))
                other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, other_style_time)
                self.write_log_to_text("INFO:stamp_trans_to_time success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "时间戳转时间失败")
        else:
            self.write_log_to_text("ERROR:stamp_trans_to_time failed")

    def time_trans_to_stamp(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                time_array = time.strptime(str(src, encoding="utf-8"), "%Y-%m-%d %H:%M:%S")
                time_stamp = int(time.mktime(time_array))
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, time_stamp)
                self.write_log_to_text("INFO:time_trans_to_stamp success")
            except Exception as e:
                self.write_log_to_text(e)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "时间转时间戳失败，格式：2021-6-18 12:00:00")
        else:
            self.write_log_to_text("ERROR:time_trans_to_stamp failed")

    # 获取当前时间
    @staticmethod
    def get_current_time():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_text(self, log_msg):
        current_time = self.get_current_time()
        log_msg_info = str(current_time) + " " + str(log_msg) + "\n"
        self.log_data_Text.insert(END, log_msg_info)
        self.log_data_Text.see(END)

    def clear_log(self):
        self.log_data_Text.delete(1.0, END)


def gui_start():
    init_window = Tk()
    start_gui = StringGui(init_window)
    # 设置根窗口默认属性
    start_gui.set_init_window()
    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == "__main__":
    gui_start()
