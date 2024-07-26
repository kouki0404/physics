import streamlit as st
import random
import sympy as sy
import numpy as np
import pandas as pd

st.title("物理演習アプリ")

number = [10,20,30,40,50,60,70,80,90,100,-10,-20,-30,-40,-50] #等加速度の時のみxの範囲を0から14にする
x = random.randint(0,10)
y = random.randint(0,10)
z = random.randint(0,10)
n = random.randint(0,10)
s = random.randint(1,3)
f = random.randint(4,8)
xx = number[x]
yy = number[y]
zz = number[z]
nn = number[n]

st.session_state.solution = 0

#出題範囲
st.sidebar.title("章を選択してください")
chapter = st.sidebar.radio("",("1章","2章","3章","4章","5章"),horizontal=True)

st.sidebar.title("問題内容を選択してください")
first = ["合成速度","相対速度","等加速度直線運動","自由落下","鉛直投げ上げ、投げ下ろし","水平投射","斜方投射","合力、力のつり合い"]
second = ["制作中"]
third = ["制作中"]
fourth = ["制作中"]
fifth = ["制作中"]

if chapter == "1章":
    serrect = st.sidebar.selectbox("出題範囲",first)
    if serrect == "合成速度":
        st.write("速さ" + int[s] + ".0m/sで流れる川の中を、船(静水時での速さ" + ".0m/s)が川の流れと平行に進む")
        st.write("(1) 船が川下に向かって進む場合、川岸で静止している人から見た船の速度は何m/sか。(川下を正とする)")
        solution_one = st.text_area("(1)回答 ※数字のみ")
        st.write("(2) 船が川上に向かって進む場合、川岸で静止している人から見た船の速度は何m/sか。(川下を正とする)")
        solution_two = st.text_area("(2)回答 ※数字のみ")
        st.write("(3) ①船が川を" + int[xx] + "m下るのと、②" + int[yy] + "m上るのにかかる時間はそれぞれ何秒か。")
        solution_three = st.text_area("(3)①回答 ※数字のみ")
        solution_four = st.text_area("(3)②回答 ※数字のみ")

        if st.button("解答確認"):
            st.session_state.solution += 1
            if solution_one == s + f:
                st.write("(1)正解")
            else:
                st.write("(1)不正解")
            if solution_two == s - f:
                st.write("(2)正解")
            else:
                st.write("(2)不正解")
            if solution_three == xx / (s + f):
                st.write("(3)①正解")
            else:
                st.write("(3)①不正解")
            if solution_four == yy / (f - s):
                st.write("(3)②正解")
            else:
                st.write("(3)②不正解")
    if serrect == "相対速度":
        st.write("a")