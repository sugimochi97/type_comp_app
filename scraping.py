import pandas as pd

df_type_comp = pd.read_html('https://yakkun.com/data/aisyou.htm')[0]
type_list_single = list(df_type_comp.iloc[1, 0:-2])
type_list = open('type_list.txt', 'r', encoding='utf-8').read().split('\n')
df_type_comp = df_type_comp.iloc[2:, 2:].set_axis(type_list, axis=0)
df_type_comp = df_type_comp.set_axis(type_list, axis=1)
df_type_comp = df_type_comp.fillna('-')
df_type_comp.to_csv('./type_comp.csv', index_label=False)

df_type_comp = df_type_comp.set_axis(type_list_single, axis=0)
df_type_comp = df_type_comp.set_axis(type_list_single, axis=1)
df_type_comp.to_csv('./type_comp_single.csv', index_label=False)