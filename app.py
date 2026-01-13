import streamlit as st
import requests

st.header("📄 AI Document Assistant")
st.markdown("For more details, check the [Original PDFS]\n[NVIDIA-2025-Annual-Report.pdf](https://s201.q4cdn.com/141608511/files/doc_financials/2025/annual/NVIDIA-2025-Annual-Report.pdf)\n[attention_is_all_you_need.pdf](https://arxiv.org/abs/1706.03762)\n[Llama-3-Technical-Report.pdf](https://arxiv.org/abs/2407.21783)")
user_question = st.text_input("Ask a question:", placeholder="How does multi-head attention work?")
if st.button("Ask"):
    if user_question:
        with st.spinner("LOADING....."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask", 
                    json={"question": user_question}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    st.write("Answer")
                    st.info(answer)
                else:
                    st.error("there is a problem for calling server")
            except:
                st.error("please ensure that you are using uvicorn")