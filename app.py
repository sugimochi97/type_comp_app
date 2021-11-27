import streamlit as st
import pandas as pd

df_type_comp = pd.read_csv('type_comp.csv')
df_type_single = pd.read_csv('type_comp_single.csv')
type_dict = dict(zip(df_type_comp.columns, df_type_single.columns))

def check_comp(attack_type, defence_type):
    comp = df_type_comp[defence_type][attack_type]
    print('相性', comp)

def party_type_check(party_type_list):
    types = list(df_type_comp.columns)
    for pt in party_type_list:
        targets = list(df_type_comp.loc[df_type_comp.loc[pt]=='●'].index)
        for target in targets:
            if target in types:
                types.remove(target)
    lacks =  []
    for t in types:
        lacks.extend(df_type_comp[df_type_comp.loc[:, t] == '●'].index)
    lacks = list(set(lacks))
    for pt in party_type_list:
        if pt in lacks:
            lacks = lacks.remove(pt)
    print('効果抜群にできないタイプ→', types)
    print('不足タイプ→', lacks)
    return types, lacks

st.write('# パーティーに含まれるタイプを選択してください。')
select_types = st.multiselect('選択↓', df_type_comp.index)
types, lacks = party_type_check(select_types)
st.markdown("# 効果抜群にできないタイプ")
st.write(' / '.join(types))
st.markdown("# 不足しているタイプ")
st.write(' / '.join(lacks))
types = [type_dict[key] for key in types]
lacks = [type_dict[key] for key in lacks]
st.markdown("# 参考用タイプ相性表")
st.dataframe(df_type_single[types].loc[lacks])