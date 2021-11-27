import streamlit as st
import pandas as pd

df_type_comp = pd.read_csv('type_comp.csv')
dict_type = {}
type_list = df_type_comp.index

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

st.selectbox('あいうえお', df_type_comp.index)
st.write(df_type_comp.index)