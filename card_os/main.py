#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
"""
    which python3 查看路径
    chmod +x main.py 添加权限
"""
import tools
# 无限循环
while True:
    # 显示功能菜单
    tools.show_menu(["1. 新建名片","2. 显示全部","3. 搜索名片","","0. 退出系统"])
    action_str = input("请选择希望执行的操作:")
    print("你选择的操作是[%s]" % action_str)

    # in 成员运算符
    # 1 2 3 针对名片的选择
    if action_str in ["1","2","3"]:
        """
            如果在开发程序时,不希望立刻编写分支内部的代码
            可以使用pass 关键字,表示一个占位符能够保证代码结构正确
            程序运行时pass 不会做任何操作
        """
        # 新建名片
        if action_str == "1":
            tools.new_card()
        # 显示全部
        elif action_str == "2":
            tools.show_card()
        # 查询名片
        elif action_str == "3":
            tools.search_card()
        pass
    # 为o 退出
    elif action_str == "0":
        print("欢迎再次使用[名片管理系统]")
        break
        # pass
    else:
        print("你输入的不正确,请重新选择")