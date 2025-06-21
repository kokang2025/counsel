import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO
import base64

# ====== SETUP ======
st.set_page_config(page_title="AI 상담 챗봇", page_icon="🤖", layout="centered")

openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "YOUR_API_KEY_HERE"

# ====== 기본 시스템 프롬프트 ======
system_prompt = "당신은 따뜻하고 공감 잘하는 전문 상담사입니다. 친절하게 대화를 이어가 주세요."

# ====== 초기 세션 상태 설정 ======
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# ====== UI 구성 ======
st.title("🧠 AI 상담 챗봇")
st.markdown("선택한 주제나 자유롭게 궁금한 점을 입력해 주세요. 상담사는 GPT-4입니다 🤖")

topics = {
    "진로 고민 🎓": "진로가 고민돼요. 어떤 직업이 저에게 잘 맞을까요?",
    "학습 방법 🧠": "공부가 너무 어려워요. 어떻게 하면 효율적으로 할 수 있을까요?",
    "인간관계 🤝": "친구들과의 관계에서 힘든 점이 있어요.",
    "스트레스 💢": "요즘 스트레스를 많이 받아요. 어떻게 해소할 수 있을까요?",
    "자기계발 🌱": "자기 계발을 하고 싶은데 무엇부터 시작하면 좋을까요?",
}

col1, col2 = st.columns([2, 5])
with col1:
    selected_topic = st.selectbox("상담 주제", list(topics.keys()))
with col2:
    user_input = st.text_input("✍️ 상담할 내용을 입력하거나 주제를 선택하세요", key="input")

send = st.button("💬 상담하기")

# ====== GPT-4 요청 및 응답 ======
if send and (user_input or selected_topic):
    user_message = user_input if user_input else topics[selected_topic]

    # 이전 대화에 추가
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.spinner("🤔 상담사가 생각 중입니다..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # 또는 "gpt-3.5-turbo"
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=800,
            )
            assistant_reply = response.choices[0].message["content"]
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            st.error("⚠️ 에러 발생: " + str(e))

# ====== 채팅창 출력 ======
st.divider()
st.subheader("💬 상담 대화")

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue  # 시스템 메시지는 표시 안 함
    elif msg["role"] == "user":
        st.chat_message("🧑‍💬 사용자").markdown(msg["content"])
    else:
        st.chat_message("🤖 상담사").markdown(msg["content"])

        # ====== TTS 음성 출력 (GPT 응답만) ======
        tts = gTTS(text=msg["content"], lang='ko')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        b64 = base64.b64encode(audio_bytes.read()).decode()
        audio_html = f"""
        <audio controls>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# ====== 리셋 버튼 ======
if st.button("🔄 상담 초기화"):
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.experimental_rerun()
