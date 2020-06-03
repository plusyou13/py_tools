# from dataclasses import dataclass
# from typing import Optional, List

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# from mpl_toolkits.mplot3d import Axes3D

# # 中华人民共和国个人所得税法: http://www.chinatax.gov.cn/n810341/n810755/c3967308/content.html
# # 关于个人所得税法修改后有关优惠政策衔接问题的通知:
# # http://www.chinatax.gov.cn/n810341/n810755/c3978994/content.html

# @dataclass
# class TaxRate:
#     start: Optional[float]
#     end: Optional[float]
#     rate: float
#     deduction: float


# def count_social_insurance(monthly_salary):
#     return 0


# def check_tax_rate(tax_rates):
#     pass


# def find_tax_rate(tax_rates: List[TaxRate], salary: float) -> Optional[TaxRate]:
#     for r in tax_rates:
#         if ((r.start is None or r.start < salary)
#                 and (r.end is None or r.end >= salary)):
#             return r
#     raise Exception("Cannot find tax rate")


# def count_tax(
#         start_point: float,  # 月薪起征点
#         tax_rates: List[TaxRate],  # 税率表
#         monthly_salary: float,  # 月薪
#         bonus: float,  # 年终奖
#         deduction: float,  # 专项扣除
# ) -> float:
#     monthly_need_tax = monthly_salary - count_social_insurance(monthly_salary) - start_point - deduction
#     if monthly_need_tax < 0:
#         monthly_need_tax = 0
#     monthly_tax_rate = find_tax_rate(tax_rates, monthly_need_tax)
#     monthly_tax = monthly_need_tax * monthly_tax_rate.rate - monthly_tax_rate.deduction
#     bonus_tax_rate = find_tax_rate(tax_rates, bonus / 12.0)
#     # The bonus tax result is not the accumulated tax, it is what the law says, not a bug
#     bonus_tax = bonus * bonus_tax_rate.rate - bonus_tax_rate.deduction
#     return 12 * monthly_tax + bonus_tax


# def min_tax(
#         start_point: float,  # 月薪起征点
#         tax_rates: List[TaxRate],  # 税率表
#         all_salary: float,
#         deduction: float,  # 专项扣除
# ) -> (float, float, float):
#     points = [r.start for r in tax_rates if r.start is not None]
#     points.append(0)
#     count_points = []

#     for p in points:
#         monthly_salary = start_point + deduction + p
#         bonus = all_salary - 12 * monthly_salary
#         if bonus < 0:
#             break
#         count_points.append((monthly_salary, bonus))
#     count_points.append((all_salary/12.0, 0))
#     for p in points:
#         bonus = 12 * p
#         monthly_salary = (all_salary - bonus) / 12.0
#         if monthly_salary < 0:
#             break
#         count_points.append((monthly_salary, bonus))
#     count_points.append((0, all_salary))

#     min_tax_result = all_salary + 1
#     min_monthly_salary = None
#     min_bonus = None

#     for (monthly_salary, bonus) in count_points:
#         if monthly_salary < 0 or bonus < 0:
#             continue
#         tax = count_tax(start_point, tax_rates, monthly_salary, bonus, deduction)
#         # print("M: %f\tB:%f\tT:%f\t" % (monthly_salary, bonus, tax))
#         if min_tax_result > tax:
#             min_tax_result = tax
#             min_monthly_salary = monthly_salary
#             min_bonus = bonus

#     return min_tax_result, min_monthly_salary, min_bonus


# tax_rates_2019 = [
#     TaxRate(None, 3000, 0.03, 0),
#     TaxRate(3000, 12000, 0.1, 210),
#     TaxRate(12000, 25000, 0.2, 1410),
#     TaxRate(25000, 35000, 0.25, 2660),
#     TaxRate(35000, 55000, 0.3, 4410),
#     TaxRate(55000, 80000, 0.35, 7160),
#     TaxRate(80000, None, 0.45, 15160),
# ]

# monthly_start_point_2019 = 60000 / 12.0


# def count_tax_2019(monthly_salary, bonus, deduction):
#     """
#     计算个人所得税
#     :param monthly_salary: 月薪
#     :param bonus: 年终奖
#     :param deduction: 每月专项扣除
#     :return: 全年需要缴纳的个人所得税
#     """
#     return count_tax(monthly_start_point_2019, tax_rates_2019, monthly_salary,
#                      bonus, deduction)


# def min_tax_2019(year_salary, monthly_deduction):
#     """
#     计算最优的年终奖方案
#     :param year_salary: 年薪
#     :param monthly_deduction: 每月专项扣除
#     :return: (全年需要缴纳的个人所得税, 月薪, 年终奖)
#     """
#     return min_tax(monthly_start_point_2019, tax_rates_2019, year_salary, monthly_deduction)


# def draw_tax_2019():
#     x = []
#     y = []
#     z = []
#     for monthly_salary in range(0, 200000, 2000):
#         for bonus in range(0, 2000000, 20000):
#             salary = 12 * monthly_salary + bonus
#             tax = count_tax_2019(monthly_salary, bonus, 0)
#             after_tax = salary - tax
#             x.append(monthly_salary)
#             y.append(bonus)
#             z.append(after_tax)
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_trisurf(np.array(x), np.array(y), np.array(z))
#     plt.show()


# def draw_min_tax_2019():
#     min_taxes = []
#     all_salaries = []
#     after_taxes = []
#     avoid_taxes = []
#     bonuses = []
#     for all_salary in range(0, 3000000, 12000):
#         tax, monthly_salary, bonus = min_tax_2019(all_salary, 0)
#         raw_tax = count_tax_2019(all_salary / 12.0, 0, 0)
#         print("All: %f\ttax: %f\tmonthly: %f\tbonus: %f" % (all_salary, tax, monthly_salary, bonus))
#         all_salaries.append(all_salary)
#         min_taxes.append(tax)
#         after_taxes.append(all_salary-tax)
#         avoid_taxes.append(raw_tax - tax)
#         bonuses.append(bonus)
#     plt.plot(all_salaries, all_salaries, label="Salary per year")
#     plt.plot(all_salaries, min_taxes, label="Minimal tax")
#     plt.plot(all_salaries, after_taxes, label="Salary after tax")
#     plt.plot(all_salaries, avoid_taxes, label="Avoided tax")
#     plt.plot(all_salaries, bonuses, label="Best bones divid")
#     plt.xlabel('Salary per year')
#     plt.ylabel('Money')
#     plt.title("Tax Counter")
#     plt.legend()
#     plt.show()

# draw_tax_2019()
# draw_min_tax_2019()








from matplotlib import pyplot as plt

# plt设置支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 工资划分的区间
sections = [36000, 144000, 300000, 420000, 660000, 960000]
# 每个区间对应的税率
rates = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
# 每个区间对应的速算扣除数
deductions = [0, 210, 1410, 2660, 4410, 7160, 15160]


def get_monthly_salary(default_salary, bonus: list, special, insurance):
    """
    :param default_salary: 基本工资
    :param bonus: 浮动奖金（绩效工资）一年内拿了几次工资就输入几个
    :param special: 专项扣除
    :param insurance: 五险一金比例
    :return: 返回每月工资
    """
    # 每月工资
    salary_list = []
    # 累计预扣缴额, 累计已缴税额
    total_need_tax, total_had_tax = 0, 0
    for i in bonus:
        # 当月预扣缴额(每月的应缴税 = 基本工资 + 浮动奖金(绩效工资) - 起征点 - 专项扣除 - 五险一金)
        should_tax = default_salary + i - 5000 - special - default_salary * insurance
        total_need_tax += should_tax
        # 税率区间
        index = get_index_from_sections(total_need_tax)
        # 累计应缴税额(累计应缴税额 * 税率 - 速算扣除数) 速算扣除数*12相当于一年
        total_tax = total_need_tax * rates[index] - deductions[index] * 12
        # 当月应缴税(当月累计应缴税 - 上月累计应缴税(累计已缴税))
        cur_tax = total_tax - total_had_tax
        # 当月工资(当月工资=基本工资 + 浮动奖金(绩效工资) - 当月应缴税 - 五险一金)
        cur_sal = default_salary + i - cur_tax - default_salary * insurance
        salary_list.append(cur_sal)
        total_had_tax = total_tax
    return salary_list


def get_index_from_sections(bonus):
    """
    :param bonus:税前年终奖
    :return:返回年终奖所在税率区间
    """
    index = 0
    while index < len(sections) and bonus > sections[index]:
        index = index + 1
    return index


def get_year_end_bonus(bonus):
    """
    :param bonus: 税前年终奖
    :return:返回税后年终奖
    """
    index = get_index_from_sections(bonus)
    # 年终奖纳税 = 税前年终奖 * 税率 - 速算扣除数
    tax = bonus * rates[index] - deductions[index]
    # 税后年终奖 = 税前年终奖 - 年终奖纳税
    return bonus - tax


def plot_bonus(r=range(0, 1200000), point: int = 0):
    """
    :param r: 税前年终奖区间
    :param point: 需要标出的点（税前年终奖的值）
    画出在r区间内的税前年终奖与税后年终奖曲线图，并标出point这个点
    """
    x = r
    y = [get_year_end_bonus(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('税前年终奖')
    plt.ylabel('税后年终奖')

    if point != 0:
        plt.scatter(x=point, y=get_year_end_bonus(point))
        p1 = r'(%d, %d)' % (point, get_year_end_bonus(point))
        plt.annotate(p1, xy=(point, get_year_end_bonus(point)))
    plt.show()


def get_bad_sections():
    """
    返回不好的年终奖区间，如果你的年终奖在本方法返回区间，那你要注意了，你可能少拿了不少钱
    """

    def get_right(i):
        return (sections[i] - rates[i] * sections[i] + deductions[i] - deductions[i + 1]) / (1 - rates[i + 1])

    return [(sections[i], int(get_right(i))) for i in range(len(sections))]


def examples():
    # 小王在上海每月工资2W，一年里每个月的绩效工资都是1000，速算扣除数为1500，上海的五险一金比例为17.5%（养老保险 8%，医疗保险 2%，失业保险0.5%，住房公积金7%）
    print("小王每个月的工资为%s" % get_monthly_salary(20000, [1000] * 12, 1500, 0.175))
    # 小李在杭州每月工资1.5W，前五个月的绩效工资分别是(0, 500, 1000, 1000, 500)，速算扣除数为1500，杭州的五险一金比例为22.5%（8% + 2% + 0.5% + 12% = 22.5%）
    print("小李前五个月的工资为%s" % get_monthly_salary(15000, [0, 500, 1000, 1000, 500], 1500, 0.225))
    # 小张的税前年终奖为36000，计算税后年终奖
    print("小张的税后年终奖为%d" % get_year_end_bonus(36000))
    # 小刘的税前年终奖为37000，计算税后年终奖(比小张拿的还少，心态崩了)
    print("小刘的税后年终奖为%d" % get_year_end_bonus(37000))


if __name__ == '__main__':
    # 计算工资和年终奖的几个小例子
    examples()
    # 计算“不好”的年终奖区间
    print(get_bad_sections())
    # 画出税前年终奖与税后年终奖曲线图
    plot_bonus()
    # plot_bonus(r=range(20000, 40000), point=36000)
    # plot_bonus(r=range(100000, 200000), point=144000)