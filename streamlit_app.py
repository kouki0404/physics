import streamlit as st
import random
import pandas as pd

# Streamlitアプリのタイトル
st.title("物理演習アプリ")
if 'numbers' not in st.session_state:
    st.session_state.numbers = 0
if 'solution' not in st.session_state:
    st.session_state.solution = 0
if 'solution_one' not in st.session_state:
    st.session_state.solution_one = 0
if 'solution_two' not in st.session_state:
    st.session_state.solution_two = 0
if 'solution_three' not in st.session_state:
    st.session_state.solution_three = 0
if 'solution_four' not in st.session_state:
    st.session_state.solution_four = 0
if 'question' not in st.session_state:
    st.session_state.question = 0
number = [0,10,20,30,40,50,60,70,80,90,100]
if 'x' not in st.session_state:
    st.session_state.x = random.randint(0,9)
if 'y' not in st.session_state:
    st.session_state.y = random.randint(0,9)
if 'z' not in st.session_state:
    st.session_state.z = random.randint(0,9)
if 's' not in st.session_state:
    st.session_state.s = random.randint(1,3)
if 'f' not in st.session_state:
    st.session_state.f = random.randint(4,7)
xx = number[st.session_state.x]
yy = number[st.session_state.y]
zz = number[st.session_state.z]


# 出題範囲
st.sidebar.title("章を選択してください")
chapter = st.sidebar.radio("", ("1章", "2章", "3章", "4章", "5章"), horizontal=True)

st.sidebar.title("問題内容を選択してください")
first = ["合成速度", "相対速度", "等加速度直線運動", "自由落下", "鉛直投げ上げ、投げ下ろし", "水平投射", "斜方投射", "合力、力のつり合い"]
second = ["制作中"]
third = ["制作中"]
fourth = ["制作中"]
fifth = ["制作中"]

if chapter == "1章":
    choose = st.sidebar.selectbox("出題範囲", first)
    
    if choose == "合成速度":
        st.session_state.question += 1
        st.write("速さ" + str(st.session_state.s) + ".0m/sで流れる川の中を、船(静水時での速さ" + str(st.session_state.f) + ".0m/s)が川の流れと平行に進む")
        st.write("(1) 船が川下に向かって進む場合、川岸で静止している人から見た船の速度は何m/sか。(川下を正とする)")
        st.session_state.solution_one = st.number_input("(1)回答 ※数字のみ", step=0.1, format="%.1f")
        st.write("(2) 船が川上に向かって進む場合、川岸で静止している人から見た船の速度は何m/sか。(川下を正とする)")
        st.session_state.solution_two = st.number_input("(2)回答 ※数字のみ", step=0.1, format="%.1f")
        st.write("(3) ①船が川を" + str(xx) + "m下るのと、②" + str(yy) + "m上るのにかかる時間はそれぞれ何秒か。")
        st.session_state.solution_three = st.number_input("(3)①回答 ※数字のみ", step=0.1, format="%.1f")
        st.session_state.solution_four = st.number_input("(3)②回答 ※数字のみ", step=0.1, format="%.1f")

        if st.button("解答確認"):
            st.session_state.solution += 1

            try:
                # 数値の比較
                if int(st.session_state.solution_one) == st.session_state.s + st.session_state.f:
                    st.write("(1)正解")
                else:
                    st.write("(1)不正解")

                if int(st.session_state.solution_two) == st.session_state.s - st.session_state.f:
                    st.write("(2)正解")
                else:
                    st.write("(2)不正解")

                if xx / st.session_state.solution_one != "%.1f":
                    h = int(xx / st.session_state.solution_one)
                    h = round(h,1)
                    if int(st.session_state.solution_three) == int(h):
                        st.write("(3)①正解")
                    else:
                        st.write("(3)①不正解")
                else:
                    h = int(xx / st.session_state.solution_one)
                    if int(st.session_state.solution_three) == int(h):
                        st.write("(3)①正解")
                    else:
                        st.write("(3)①不正解")

                if yy / st.session_state.solution_two * -1 != "%.1f":
                    w = int(yy / st.session_state.solution_two * -1)
                    w = round(w, 1)
                    
                    if int(st.session_state.solution_four) == int(w):
                        st.write("(3)②正解")
                    else:
                        st.write("(3)②不正解")

                else:
                    w = int(yy / st.session_state.solution_two * -1)
                    if int(st.session_state.solution_four) == int(w):
                        st.write("(3)②正解")
                    else:
                        st.write("(3)②不正解")

            
            except ValueError:
                st.write("入力された値が無効です。数字のみを入力してください")
    
    if choose == "相対速度":
        st.write("a")

