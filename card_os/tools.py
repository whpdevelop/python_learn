
# 记录所有名片列表
card_list = []
def show_menu(list_welcome):
    """
        欢迎界面
    """
    print("*"*50)
    print("欢迎使用 [名片管理系统]")
    for item in list_welcome:
        print(item)
    print("*"*50)


def new_card():
    """
        新增名片
    """
    print("+"*50)
    print("新增名片")
    # 1. 提示用户输入名片的详细信息
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    qq = input("请输入QQ号码: ")
    email = input("请输入邮箱: ")
    # 2. 使用用户输入的信息建立一个名片字典
    card_dict={
        "name":name,
        "phone":phone,
        "qq":qq,
        "email":email
    }
    # 3. 将名片添加到列表中
    card_list.append(card_dict)
    # 4. 提示用户添加成功
    print("添加 %s 的名片成功!" % name)

def show_card():
    """
        显示全部
    """ 
    print("+"*50)
    print("显示全部")
    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有名片记录请先新建名片!!!")
        return
    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")
    print("="*50)
    # 打印分割线
    for item in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (item["name"],item["phone"],item["qq"],item["email"]))

def search_card():
    """
        搜索名片
    """
    print("+"*50)
    print("搜索名片")
    # 1. 提示用户输入的用户名
    find_name= input("请输入要搜索的姓名: ")
    # 2. 遍历名片列表,查询要搜索的姓名,如果没有找到,需要提示用户
    for dirt in card_list:
        if dirt["name"] == find_name:
            # 打印表头
            for name in ["姓名","电话","QQ","邮箱"]:
                print(name,end="\t\t")
            print("")
            print("="*50)
            # 打印分割线
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (dirt["name"],
                                                dirt["phone"],
                                                dirt["qq"],
                                                dirt["email"]))

            # 针对找到的名片 修改和删除操作
            deal_card(dirt)
            break
    else: 
        print("没有查到%s名片信息" % find_name)


def deal_card(find_card):
    print("你可以对信息的操作:删除[1]/修改[2]/返回[0]")
    deal_change = input("请输入你想输入的操作: ")
    if deal_change == "1":
        print("删除名片")
        card_list.remove(find_card)
    elif deal_change == "2":
        print("修改名片")
        find_card["name"] = input_card_info(find_card["name"],"修改姓名[回车不修改]")
        find_card["phone"] = input_card_info(find_card["phone"],"修改电话[回车不修改]")
        find_card["qq"] = input_card_info(find_card["qq"],"修改qq[回车不修改]")
        find_card["email"] = input_card_info(find_card["email"],"修改邮箱[回车不修改]")
        
def input_card_info(old_val,msg):
    """
        解决修改时输入为空的情况
    """
    # 1. 提示用户输入内容
    result = input(msg)
    # 2. 针对用户的输入进行判断 如果用户输入了直接返回结果
    if len(result)>0:
        return result
    # 3. 如果没有输入内容,返回字典中的原有的值
    else:
        return old_val