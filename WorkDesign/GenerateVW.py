class GenerateVWCases(object):

    def __init__(self, data: list, title_map: list):
        self.data = data
        # 全局等待时间
        self.timeout = 60
        # 功能：菜单是否存在,生成是否出错；默认False
        self.status = {"读汽车电脑信息": [False, False], "故障码": [False, False], "读数据流": [False, False],
                       "高级ID": [False, False], "动作测试": [False, False], "匹配": [False, False],
                       "基本设置": [False, False], "安全访问": [False, False], "编码": [False, False],
                       "离线编码": [False, False], "引导功能": [False, False],
                       "在线安装列表": [False, False], "在线安全登录": [False, False]}

    # 根据输入不同切换不同方法，替代复杂的if/elif/else语法
    def switch_function(self, selection: str):
        function_map = {"读汽车电脑信息": self.info, "故障码": self.trouble_code, "读数据流": self.data_stream,
                        "高级ID": self.advanced_id, "动作测试": self.action_test, "匹配": self.adapter,
                        "基本设置": self.basic_fun, "安全访问": self.safe_access, "编码": self.coding_online,
                        "离线编码": self.code_offline, "引导功能": self.follow_fun,
                        "在线安装列表": self.install_list, "在线安全登录": self.online_safety_login}
        return function_map[selection]()

    def generate(self):
        """
        生成用例步骤
        :return:
        """
        # 启动模拟平台
        self.start_simulator()
        # 进入ECU
        self.forward_click(self.data[self.data.index('%') + 1:])
        # 获取所有功能选项列表
        all_fun = self.get_all_select()
        # 生成用例步骤
        all_steps = self.data[:self.data.index('%') + 1]
        for key, value in self.status.items():
            if key in all_fun:
                value[0] = True
                list_step = self.switch_function(key)
                if list_step:
                    value[1] = True
                    all_steps += list_step

        # 关闭模拟平台
        self.close_simulator()
        # 写入用例
        self.write_cases()
        self.check_point()

    def start_simulator(self):
        pass

    def close_simulator(self):
        pass

    def write_cases(self):
        pass

    def check_point(self):
        pass

    def info(self):
        self.forward_click('读汽车电脑信息')
        return []

    def trouble_code(self):
        self.forward_click('故障码')
        return []

    def data_stream(self):
        self.forward_click('读数据流')
        return ['读数据流', 'sleep20', 'press4']

    def advanced_id(self):
        self.forward_click('高级ID')
        return []

    def action_test(self):
        self.forward_click('动作测试')
        return []

    def adapter(self):
        self.forward_click('匹配')
        return []

    def basic_fun(self):
        self.forward_click('基本设置')
        return []

    def safe_access(self):
        self.forward_click('安全访问')
        return []

    def coding_online(self):
        self.forward_click('编码')
        return []

    def code_offline(self):
        self.forward_click('离线编码')
        return []

    def follow_fun(self):
        self.forward_click('引导功能')
        return []

    def install_list(self):
        self.forward_click('在线安装列表')
        return []

    def online_safety_login(self):
        self.forward_click('在线安全登录')
        return ['在线安全登录', '取消']

    def forward_click(self, *data):
        pass

    def get_all_select(self):
        """
        获取所有选项列表
        :return: 选项列表
        """
        self.forward_click('laal')
        return []
