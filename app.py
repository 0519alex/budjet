import streamlit as st
from datetime import datetime

st.set_page_config(page_title="쟈쟛 예산 계산기", layout="centered")

st.title("예산 계산기 - '시발 돈 좀 아껴라'")

총예산 = st.number_input("이번 달 예산 (원)", value=600000, step=10000)
총일수 = st.number_input("이번 달 일수", value=30, step=1)
오늘 = datetime.today().day

지출기록 = []
st.subheader("하루하루 지출 입력")
for i in range(1, 오늘 + 1):
    지출 = st.number_input(f"{i}일차 지출 (원)", value=0, step=100, key=f"day_{i}")
    지출기록.append(지출)

사용일수 = len(지출기록)
총지출 = sum(지출기록)
남은예산 = 총예산 - 총지출
남은일수 = 총일수 - 사용일수

st.markdown("---")

if 남은예산 < 0:
    st.error("시발 예산 초과! 정신차려!!")
elif 남은일수 <= 0:
    st.success("이번 달 끝! 다음 달엔 아껴써보자 줴줴이~")
else:
    오늘지출 = 지출기록[-1]
    하루기준 = 총예산 / 총일수
    평균예산 = 남은예산 / 남은일수
    내일예산 = 평균예산 + (하루기준 - 오늘지출)

    st.subheader("계산 결과")
    st.write(f"남은 예산: **{남은예산:,.0f} 원**")
    st.write(f"남은 일수: **{남은일수} 일**")
    st.write(f"내일 쓸 수 있는 예산: **{내일예산:,.0f} 원** (오늘 {오늘지출:,}원 써서 {하루기준 - 오늘지출:+,.0f}원 아낌)")