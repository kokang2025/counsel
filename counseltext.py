import streamlit as st

st.set_page_config(page_title="상담 챗봇 연결", page_icon="💬")
st.title("💬 ChatGPT 상담 도우미")

# 상담 주제와 프롬프트 매핑
topics = {
    "🎯 진로 고민": "저는 앞으로 어떤 직업이 저에게 잘 맞을지 고민하고 있습니다. 조언을 부탁드려요.",
    "🧠 성격 분석": "제 성격을 이해하고 장단점을 분석해 주세요.",
    "📚 학습 습관": "효율적인 공부 방법과 습관을 알고 싶습니다. 어떻게 하면 좋을까요?",
    "🤝 친구 관계": "친구와의 갈등이나 어려움을 어떻게 해결하면 좋을지 상담 받고 싶어요.",
    "🏠 가족 문제": "가족과의 갈등으로 고민이 많아요. 조언을 구하고 싶습니다.",
    "❤️ 연애 고민": "좋아하는 사람이 있는데 어떻게 다가가야 할지 고민입니다. 조언을 해주세요.",
    "🧘 스트레스 해소": "요즘 스트레스를 많이 받고 있어요. 마음을 편하게 하는 방법이 궁금합니다."
}

# 주제 선택
selected_topic = st.selectbox("📌 상담 주제를 선택하세요", list(topics.keys()))
prompt = topics[selected_topic]

# 프롬프트 보여주기
st.subheader("✍️ 추천 질문 프롬프트:")
st.code(prompt, language="markdown")

# 프롬프트 복사 기능 (Streamlit 웹에서는 JS로 대체 가능, 여기선 안내만)
st.info("👇 아래 텍스트를 복사하여 ChatGPT에 붙여넣어 주세요.")

# ChatGPT 이동 링크
st.markdown("👉 [ChatGPT로 이동하기](https://chat.openai.com)")

st.caption("🔐 ChatGPT는 URL로 자동 질문 전달을 지원하지 않습니다. 위 문장을 복사해 사용하세요.")
