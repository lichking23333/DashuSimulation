import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

def single_simulation(initial_skills, desired_skills, essential_skills, skill_prices, include_set_skills, output_text):
    current_skills = initial_skills.copy()
    total_cost = 0

    output_text.insert(tk.END, "\n开始单次模拟...\n\n")
    while True:
        # 根据是否包含套装技能调整停止条件
        if include_set_skills:
            stop_condition = (
                len(set(current_skills) & set(desired_skills)) >= len(desired_skills) - 1
                and all(skill in current_skills for skill in essential_skills)
            )
        else:
            stop_condition = (
                len(set(current_skills) & set(desired_skills)) >= len(desired_skills)
                and all(skill in current_skills for skill in essential_skills)
            )

        if stop_condition:
            break

        # 找到缺失的技能
        missing_skills = [skill for skill in desired_skills if skill not in current_skills]
        if not missing_skills:
            break  # 已经拥有所有需要的技能

        # 学习最便宜的缺失技能
        skill_to_learn = min(missing_skills, key=lambda x: skill_prices.get(x, float('inf')))
        # 随机替换当前技能中的一个
        index_to_replace = random.randint(0, len(current_skills) - 1)
        replaced_skill = current_skills[index_to_replace]
        current_skills[index_to_replace] = skill_to_learn
        # 增加总成本
        temp = skill_prices.get(skill_to_learn, float('inf'))
        total_cost += temp
        output_text.insert(tk.END, f"将技能 '{replaced_skill}' 替换为 '{skill_to_learn}' 花费 '{temp}'\n")
        output_text.insert(tk.END, f"当前技能列表: {current_skills}\n\n")

    output_text.insert(tk.END, "学习完成！\n")
    output_text.insert(tk.END, f"最终技能列表: {current_skills}\n")
    output_text.insert(tk.END, f"总共花费: {total_cost:.2f} R\n")

def multiple_simulations(initial_skills, desired_skills, essential_skills, skill_prices, include_set_skills, output_text):
    total_costs = []

    output_text.insert(tk.END, "\n开始10000次模拟...\n\n")
    for _ in range(10000):
        current_skills = initial_skills.copy()
        total_cost = 0

        while True:
            # 根据是否包含套装技能调整停止条件
            if include_set_skills:
                stop_condition = (
                    len(set(current_skills) & set(desired_skills)) >= len(desired_skills) - 1
                    and all(skill in current_skills for skill in essential_skills)
                )
            else:
                stop_condition = (
                    len(set(current_skills) & set(desired_skills)) >= len(desired_skills)
                    and all(skill in current_skills for skill in essential_skills)
                )

            if stop_condition:
                break

            # 找到缺失的技能
            missing_skills = [skill for skill in desired_skills if skill not in current_skills]
            if not missing_skills:
                break  # 已经拥有所有需要的技能

            # 学习最便宜的缺失技能
            skill_to_learn = min(missing_skills, key=lambda x: skill_prices.get(x, float('inf')))
            # 随机替换当前技能中的一个
            index_to_replace = random.randint(0, len(current_skills) - 1)
            current_skills[index_to_replace] = skill_to_learn
            # 增加总成本
            total_cost += skill_prices.get(skill_to_learn, float('inf'))

        total_costs.append(total_cost)

    average_cost = sum(total_costs) / len(total_costs)
    output_text.insert(tk.END, f"10000次模拟的平均学习成本为: {average_cost:.2f} R\n")

def run_simulation():
    initial_skills_input = initial_skills_entry.get()
    desired_skills_input = desired_skills_entry.get()
    essential_skills_input = essential_skills_entry.get()

    initial_skills = initial_skills_input.strip().split("，")
    desired_skills = desired_skills_input.strip().split("，")
    essential_skills = essential_skills_input.strip().split("，")
    if desired_skills == ['']:
        desired_skills = []
    if essential_skills == ['']:
        essential_skills = []

    # 技能价格表
    skill_prices = {
        "死亡召唤": 48888.00,
        "法力陷阱": 239.50,
        "灵能激发": 655.00,
        "夜舞倾城": 4555.00,
        "龙魂": 5000.00,
        "高级必杀": 334.00,
        "高级连击": 338.00,
        "高级偷袭": 385.00,
        "高级夜战": 200.95,
        "高级神佑复生": 118.81,
        "高级吸血": 140.00,
        "高级法术暴击": 118.98,
        "高级魔之心": 110.00,
        "高级法术波动": 113.60,
        "高级法术连击": 18.00,
        "高级感知": 17.40,
        "高级反震": 23.00,
        "高级敏捷": 139.77,
        "高级强力": 94.90,
        "高级幸运": 24.50,
        "高级防御": 94.00,
        "壁垒击破": 28.70,
        "高级驱鬼": 101.00,
        "高级隐身": 13.00,
        "高级合纵": 41.00,
        "嗜血追击": 10.00,
        "必杀": 10.00,
        "吸血": 10.00,
        "夜战": 10.00
    }

    include_set_skills = include_set_skills_var.get()

    if mode_var.get() == 1:
        single_simulation(initial_skills, desired_skills, essential_skills, skill_prices, include_set_skills, output_text)
    elif mode_var.get() == 2:
        multiple_simulations(initial_skills, desired_skills, essential_skills, skill_prices, include_set_skills, output_text)
    else:
        messagebox.showerror("错误", "请选择模拟模式！")

def clear_output():
    output_text.delete('1.0', tk.END)

# 创建主窗口
root = tk.Tk()
root.title("召唤兽打书模拟器 - 成都府")

# 设置窗口大小
root.geometry('600x750')

# 初始技能输入
initial_skills_label = tk.Label(root, text="初始技能列表（以中文逗号分隔）：")
initial_skills_label.pack()
initial_skills_entry = tk.Entry(root, width=80)
initial_skills_entry.pack()
initial_skills_entry.insert(0, "幸运，水攻，必杀，强力，进击必杀，感知，反击，盾气，法术抵抗，反震")

# 学习技能输入
desired_skills_label = tk.Label(root, text="打成技能列表（以中文逗号分隔）：")
desired_skills_label.pack()
desired_skills_entry = tk.Entry(root, width=80)
desired_skills_entry.pack()
desired_skills_entry.insert(0, "高级连击，高级必杀，高级吸血，高级夜战，高级偷袭，高级强力，高级神佑复生，高级合纵，嗜血追击")

# 必备技能输入
essential_skills_label = tk.Label(root, text="大四喜（不追这行空着，以中文逗号分隔）：")
essential_skills_label.pack()
essential_skills_entry = tk.Entry(root, width=80)
essential_skills_entry.pack()
essential_skills_entry.insert(0, "高级偷袭，高级合纵，高级夜战，高级必杀")


# 是否包含套装技能
include_set_skills_var = tk.BooleanVar()
include_set_skills_var.set(True)  # 默认勾选
include_set_skills_check = tk.Checkbutton(root, text="是否包含套装技能", variable=include_set_skills_var)
include_set_skills_check.pack()

# 模式选择
mode_label = tk.Label(root, text="请选择模拟模式：")
mode_label.pack()

mode_var = tk.IntVar()
mode_var.set(1)
mode_frame = tk.Frame(root)
mode_frame.pack()

single_mode_radio = tk.Radiobutton(mode_frame, text="1. 单次模拟", variable=mode_var, value=1)
single_mode_radio.pack(side=tk.LEFT)

multiple_mode_radio = tk.Radiobutton(mode_frame, text="2. 10000次模拟计算平均成本", variable=mode_var, value=2)
multiple_mode_radio.pack(side=tk.LEFT)

# 运行按钮
run_button = tk.Button(root, text="运行模拟", command=run_simulation)
run_button.pack()

# 清空输出按钮
clear_button = tk.Button(root, text="清空输出", command=clear_output)
clear_button.pack()

# 输出框
output_label = tk.Label(root, text="模拟输出：")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, width=70, height=25)
output_text.pack()

# 运行主循环
root.mainloop()
