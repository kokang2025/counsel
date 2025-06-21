import streamlit as st

st.set_page_config(page_title="💬 무료 GPT 상담 챗봇", layout="centered")

st.title("💬 무료 GPT 상담 챗봇")
st.markdown("학생들을 위한 인공지능 상담 도우미입니다. 상담 주제를 선택한 뒤 아래 챗봇과 자유롭게 대화해보세요. 🤗")

topics = {
    "진로 고민": "어떤 직업이 나에게 잘 맞을지 고민된다면, 이 주제를 선택하세요.",
    "성격 분석": "내 성격에 대해 알고 싶을 때 사용할 수 있어요.",
    "학습 습관": "공부 방법이나 습관을 바꾸고 싶다면 추천해요.",
    "친구 관계": "친구와의 관계에서 어려움이 있다면 이 주제를 선택해 보세요.",
    "가족 문제": "가족과의 갈등이나 고민이 있다면 여기에 도움을 받아보세요.",
}

selected_topic = st.selectbox("🧠 상담 주제를 선택하세요:", list(topics.keys()))
st.info(f"💡 {topics[selected_topic]}")

st.markdown("---")
st.subheader("🗨️ 아래 챗봇과 대화해보세요!")

# Hugging Face의 Gradio Space URL (공용 GPT 챗봇 예시)
hf_space_url = "https://yuntian-deng-chatgpt.hf.space"

st.components.v1.html(f"""
    <script src="https://gradio.s3-us-west-2.amazonaws.com/latest/gradio.js" type="module"></script>
    <gradio-app src="{hf_space_url}"></gradio-app>
""", height=650)
