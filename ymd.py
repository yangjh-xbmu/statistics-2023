import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from matplotlib import font_manager

# 设置中文字体
font_path = 'SimHei.ttf'  # 根据实际路径设置字体路径
font = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font.get_name()

# 读取Excel文件
file_path = '264356010_按文本_关于卡尔美运动品牌知名度的问卷调查_47_47.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# 将年龄列进行数值化处理
age_mapping = {
    'A. 18岁及以下': 18,
    'B. 19-25岁': 22,
    'C. 26-35岁': 30,
    'D. 35岁及以上': 40
}
data['年龄数值'] = data['1、请问您的年龄是？'].map(age_mapping)

# 描述性统计分析
# 年龄分布
age_counts = data['1、请问您的年龄是？'].value_counts()
age_percentage = (age_counts / len(data)) * 100
age_mean = data['年龄数值'].mean()
age_median = data['年龄数值'].median()
age_std = data['年龄数值'].std()

# 性别分布
gender_counts = data['2、您的性别是？'].value_counts()
gender_percentage = (gender_counts / len(data)) * 100

# 职业分布
occupation_counts = data['3、您的职业是？'].value_counts()
occupation_percentage = (occupation_counts / len(data)) * 100

# 打印描述性统计结果
print('年龄分布:')
print(pd.DataFrame({'Counts': age_counts, 'Percentage': age_percentage}))
print(f'年龄均值: {age_mean:.2f}')
print(f'年龄中位数: {age_median:.2f}')
print(f'年龄标准差: {age_std:.2f}')

print('\n性别分布:')
print(pd.DataFrame({'Counts': gender_counts, 'Percentage': gender_percentage}))

print('\n职业分布:')
print(pd.DataFrame({'Counts': occupation_counts,
      'Percentage': occupation_percentage}))

# 推论性统计分析
# 示例：t检验 - 比较不同性别的总分
male_scores = data.loc[data['2、您的性别是？'] == 'A. 男', '总分']
female_scores = data.loc[data['2、您的性别是？'] == 'B. 女', '总分']
t_stat, p_val = stats.ttest_ind(male_scores.dropna(), female_scores.dropna())

print(f'\nt检验结果: t_stat = {t_stat:.4f}, p_val = {p_val:.4f}')

# 示例：卡方检验 - 比较不同年龄段的职业分布
age_groups = pd.cut(data['年龄数值'], bins=[0, 18, 25, 35, 50, 100], labels=[
                    '0-18', '19-25', '26-35', '36-50', '50+'])
crosstab = pd.crosstab(age_groups, data['3、您的职业是？'])
chi2, p, dof, expected = stats.chi2_contingency(crosstab)

print(f'\n卡方检验结果: chi2 = {chi2:.4f}, p_val = {p:.4f}')

# 可视化
# 年龄分布
plt.figure(figsize=(10, 6))
age_counts.plot(kind='bar')
plt.title('年龄分布', fontproperties=font)
plt.xlabel('年龄', fontproperties=font)
plt.ylabel('人数', fontproperties=font)
plt.show()

# 性别分布
plt.figure(figsize=(10, 6))
gender_counts.plot(kind='bar')
plt.title('性别分布', fontproperties=font)
plt.xlabel('性别', fontproperties=font)
plt.ylabel('人数', fontproperties=font)
plt.show()

# 职业分布
plt.figure(figsize=(10, 6))
occupation_counts.plot(kind='bar')
plt.title('职业分布', fontproperties=font)
plt.xlabel('职业', fontproperties=font)
plt.ylabel('人数', fontproperties=font)
plt.show()
