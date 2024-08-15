import streamlit as st
import random
import pandas as pd

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
number = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
speed = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,-0.5,-1.0,-1.5,-2.0,-2.5,-3.0,-3.5,-4.0,-4.5,-5.0]
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
if 'u' not in st.session_state:
    st.session_state.u = random.randint(0,19)
if 'fast' not in st.session_state:
    st.session_state.fast = random.randint(10,15)
if 'q' not in st.session_state:
    st.session_state.q = random.randint(0,8)
brain = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
xx = number[st.session_state.x]
yy = number[st.session_state.y]
zz = number[st.session_state.z]
uu = speed[st.session_state.u]
faster = number[st.session_state.fast]
qq = brain[st.session_state.q]
ss = speed[st.session_state.s]

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
        st.write("速さ" + str(st.session_state.s) + ".0m/sで流れる川の中を、船(静水中での速さ" + str(st.session_state.f) + ".0m/s)が川の流れと平行に進む。")
        st.write("回答は少数第一位までとする")
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
                
                if int(st.session_state.solution_one) == st.session_state.s + st.session_state.f:
                    st.write("(1)正解")
                else:
                    st.write("(1)不正解 流れる方向に沿って船が進む場合、速度の和が合成速度になります。")

                if int(st.session_state.solution_two) == st.session_state.s - st.session_state.f:
                    st.write("(2)正解")
                else:
                    st.write("(2)不正解 速度の方向はあっていますか？")

                if xx / int(st.session_state.s + st.session_state.f) != "%.1f":
                    h = int(xx / (st.session_state.s + st.session_state.f))
                    h = round(h,1)
                    if int(st.session_state.solution_three) == int(h):
                        st.write("(3)①正解")
                    else:
                        st.write("(3)①不正解 (1)で出た答えを応用してみよう。")
                else:
                    h = int(xx / (st.session_state.s + st.session_state.f))
                    if int(st.session_state.solution_three) == int(h):
                        st.write("(3)①正解")
                    else:
                        st.write("(3)①不正解 (1)で出た答えを応用してみよう。")

                if yy /  int(st.session_state.f - st.session_state.s) != "%.1f":
                    w = int(yy / (st.session_state.f - st.session_state.s))
                    w = round(w, 1)
                    
                    if int(st.session_state.solution_four) == int(w):
                        st.write("(3)②正解")
                    else:
                        st.write("(3)②不正解 (2)で出た答えを応用してみよう。")

                else:
                    w = int(yy / (st.session_state.f - st.session_state.s))
                    if int(st.session_state.solution_four) == int(w):
                        st.write("(3)②正解")
                    else:
                        st.write("(3)②不正解 (2)で出た答えを応用してみよう。")

            
            except ValueError:
                st.write("入力された値が無効です。数字のみを入力してください")
    
    if choose == "相対速度":
        st.session_state.question += 1
        st.write("直線上を右向きに" + str(st.session_state.x) + ".0m/sで移動するAさんがいる。")
        st.write("(1)右向きに" + str(st.session_state.y) + ".0m/sで移動するBさんに対するAさんの相対速度を求めよ。(右向きを正とする)")
        st.session_state.solution_one = st.number_input("(1)回答 ※数字のみ", step=0.1, format="%.1f")
        st.write("左向きに" + str(st.session_state.z) + ".0m/sで移動するBさんに対するAさんの相対速度を求めよ。(右向きを正とする)")
        st.session_state.solution_two = st.number_input("(2)回答 ※数字のみ", step=0.1, format="%.1f")

        if st.button("解答確認"):
            st.session_state.solution += 1  
            try:
                
                if int(st.session_state.solution_one) == st.session_state.x - st.session_state.y:
                    st.write("(1)正解")
                else:
                    st.write("(1)不正解")

                if int(st.session_state.solution_two) == st.session_state.x + st.session_state.z:
                    st.write("(2)正解")
                else:
                    st.write("(2)不正解")
            except ValueError:
                st.write("入力された値が無効です。数字のみを入力してください")

    if choose == "等加速度直線運動":
        st.session_state.question += 1
        st.sidebar.title("難易度を選択してください")
        easy = st.sidebar.radio("", ("基礎", "応用"), horizontal=True)
        if easy == "基礎":
            st.write("右向きに速さ" + str(st.session_state.x) + ".0m/sで動いていた物体が一定の加速度" + str(uu) + "m/sで速さを増した。")
            if st.session_state.y > 5:
                number_y = st.session_state.y - 4
                st.write("(1)" + str(number_y) + ".0秒後の物体の速さは何m/sか。")
                st.session_state.solution_one = st.number_input("(1)回答 ※数字のみ", step=0.1, format="%.1f")
            else:
                st.write("(1)" + str(st.session_state.y) + ".0秒後の物体の速さは何m/sか。")
                st.session_state.solution_one = st.number_input("(1)回答 ※数字のみ", step=0.1, format="%.1f")
            if st.session_state.z > 5:
                number_z = st.session_state.z - 4
                st.write("(1)" + str(number_z) + ".0秒後までに物体が進んだ距離は何ｍか。")
                st.session_state.solution_two = st.number_input("(2)回答 ※数字のみ", step=0.1, format="%.1f")
            else:
                st.write("(1)" + str(st.session_state.z) + ".0秒後までに物体が進んだ距離は何ｍか。")
                st.session_state.solution_two = st.number_input("(2)回答 ※数字のみ", step=0.1, format="%.1f")

            if st.button("解答確認"):
                st.session_state.solution += 1  
                if st.session_state.y > 5:
                    try:
                        
                        if int(st.session_state.solution_one) == st.session_state.x + int(uu * number_y):
                            st.write("(1)正解")
                        else:
                            st.write("(1)不正解")
                    except ValueError:
                        st.write("入力された値が無効です。数字のみを入力してください")
                else:
                    try:
                        
                        if int(st.session_state.solution_one) == st.session_state.x + int(uu * st.session_state.y):
                            st.write("(1)正解")
                        else:
                            st.write("(1)不正解")
                    except ValueError:
                        st.write("入力された値が無効です。数字のみを入力してください")

                if st.session_state.z > 5:

                    try:
                        if int(st.session_state.solution_two) == int(st.session_state.x * number_z) + int(0.5 * uu * number_z ** 2):
                            st.write("(2)正解")
                        else:
                            st.write("(2)不正解")
                    except ValueError:
                        st.write("入力された値が無効です。数字のみを入力してください")
                else:
                    try:
                        if int(st.session_state.solution_two) == int(st.session_state.x * st.session_state.z) + int(0.5 * uu * st.session_state.z ** 2):
                            st.write("(2)正解")
                        else:
                            st.write("(2)不正解")
                    except ValueError:
                        st.write("入力された値が無効です。数字のみを入力してください")
        
        if easy == "応用":
            st.write("ゴールまで残り" + str(faster) + "mの位置で4つの物体が並んでいる")
            st.write("3つの物体はそれぞれ以下のように一直線上に運動をしている")
            st.write("(A) " + str(qq) + "m/s²の速度の大きさを保って減速している。残り" + str(faster) + "m地点での速さは" + str(st.session_state.fast) + "m/sであった。")
            st.write("(B) " + str(ss) + "m/s²で等加速度直線運動をしている。")
            st.write("(C) " + str(st.session_state.f) + "m/sで等速直線運動をしている。")
            st.write("問 制限時間10sの間にゴールに到達できる物体はどれか答えよ")
            st.session_state.solution_one = st.text_area("回答 ※大文字で答えてください、回答がない場合はなしと書いてください。")

            if st.button("解答確認"):
                st.session_state.solution += 1
                solution = [0,1,2]
                one = st.session_state.fast * 10 + qq * -1 * 100 / 2
                two = ss * 100 / 2
                three = 10 * st.session_state.f
                try:
                    if one >= faster:
                        solution[0] = 'A'
                        if two >= faster:
                            solution[1] = 'B'
                            if three >= faster:
                                solution[2] = 'C'
                            else:
                                solution = ['A','B']
                        else:
                            solution = ['A',1]
                            if three >= faster:
                                solution[1] = 'C'
                            else:
                                solution = ['A']
                    else:
                        solution = [0,1]
                        if two >= faster:
                            solution[0] = 'B'
                            if three >= faster:
                                solution[1] = 'C'
                            else:
                                solution = ['B']
                        else:
                            solution = [0]
                            if three >= faster:
                                solution[0] = 'C'
                            else:
                                solution = ['なし']
                except ValueError:
                    st.write("入力された値が無効です。数字のみを入力してください")

                if solution == ['A','B','C']:
                    answer = "A,B,C"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['A','B']:
                    answer = "A,B"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['A','C']:
                    answer = "A,C"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['B','C']:
                    answer = "B,C"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['A']:
                    answer = "A"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['B']:
                    answer = "B"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == ['C']:
                    answer = "C"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                if solution == 'なし':
                    answer = "なし"
                    if st.session_state.solution_one == answer:
                        st.write("正解")
                    else:
                        st.write("不正解")
                


if chapter == "2章":
    choose = st.sidebar.selectbox("出題範囲", second)

if chapter == "3章":
    choose = st.sidebar.selectbox("出題範囲", third)

if chapter == "4章":
    choose = st.sidebar.selectbox("出題範囲", fourth)

if chapter == "5章":
    choose = st.sidebar.selectbox("出題範囲", fifth)