import streamlit as st
import os
from dotenv import load_dotenv
from loaders.secure_file_loader import SecureFileLoader
from services.qna_service import QnAService
from utils.helper_functions import preprocess_text

# 환경 변수 로드
load_dotenv()

# 메인 함수
def main():
    st.set_page_config(page_title="논문 Q&A 시스템", layout="wide")
    st.title("📄 논문 Q&A 시스템")

    # Session State 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Sidebar - 파일 업로드
    st.sidebar.title("📂 논문 업로드")
    uploaded_file = st.sidebar.file_uploader("PDF 파일을 업로드하세요", type=["pdf"])
    
    if uploaded_file is not None:
        # 파일 저장 및 텍스트 로드
        loader = SecureFileLoader()
        file_path = os.path.join(loader.base_dir, uploaded_file.name)
        try:
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.sidebar.success("✅ 파일 업로드 완료!")
        except Exception as e:
            st.sidebar.error(f"⚠️ 파일 업로드 중 오류 발생: {e}")
            return

        try:
            pdf_text = loader.load_pdf(uploaded_file.name)
            st.session_state.pdf_text = pdf_text
            st.sidebar.text_area("📄 논문 내용 미리보기", pdf_text[:500], height=200, disabled=True)  # 미리보기
        except Exception as e:
            st.sidebar.error(f"⚠️ PDF 로딩 오류: {e}")
            return

    # 채팅 UI 설정
    st.write("### 💬 논문과 대화하기")

    # 채팅 기록 표시
    for message in st.session_state.messages:
        if message["type"] == "user":
            st.markdown(f"""
            <div style="text-align: right; margin: 10px 0;">
                <div style="display: inline-block; padding: 10px; border-radius: 10px; background-color: #dcf8c6;">
                    {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="text-align: left; margin: 10px 0;">
                <div style="display: inline-block; padding: 10px; border-radius: 10px; background-color: #f1f0f0;">
                    {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 질문 처리 함수
    def handle_question():
        question = st.session_state.user_input
        if not question.strip():
            st.warning("⚠️ 질문을 입력해 주세요.")
            return

        if "pdf_text" not in st.session_state:
            st.warning("⚠️ 먼저 논문을 업로드해 주세요.")
            return

        # QnAService 초기화
        if "qna_service" not in st.session_state:
            try:
                st.session_state.qna_service = QnAService(st.session_state.pdf_text)
            except Exception as e:
                st.error(f"⚠️ QnA 서비스 초기화 오류: {e}")
                return

        qna_service = st.session_state.qna_service

        # 질문 처리
        try:
            answer = qna_service.get_answer(preprocess_text(question))
            st.session_state.messages.append({"type": "user", "content": question})
            st.session_state.messages.append({"type": "bot", "content": answer})
        except Exception as e:
            st.error(f"⚠️ 답변 생성 중 오류: {e}")

    # 입력창 (Enter로 자동 처리)
    st.text_input("질문을 입력하세요", placeholder="논문에 대해 궁금한 점을 입력하세요...", key="user_input", on_change=handle_question)

if __name__ == "__main__":
    main()