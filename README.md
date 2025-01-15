# 과제명: 논문 기반 질문 답변 시스템 개발

## 목표: 제공된 논문 PDF를 기반으로, 논문 내용에 대한 질문에 정확히 답변할 수 있는 시스템 설계

=================

### 시스템 구성 요소 설계

#### Loader (로더)
논문을 불러와 수학적 기호와 수식을 정확히 인식하는 모듈  
추천 기술: LaTeX 처리 지원 PDF 파서  
- 역할: 논문에서 텍스트, 수식, 도표를 추출  

#### Splitter (분할기)
논문을 의미 단위로 분할하여 질문과 답변을 매핑  
추천 기술: 문단 단위 세분화 + 의미 기반 분할  
- 역할: 논문을 의미 단위로 분할하여 질문과 관련된 내용을 정확히 대응  

#### Search Engine (검색 엔진)
사용자의 질문과 가장 관련성이 높은 논문 부분을 탐색  
추천 기술: 벡터 검색 도구(예: Chroma DB)  
- 역할: 질문과 관련된 논문 내용을 검색  

#### Prompt Handler (프롬프트 처리기)
질문에 맞는 답변을 논문 내용에서 생성  
- 역할: 사용자의 질문에 대한 적절한 답변 생성  

=================

### Prompt 설계 원칙

1. **역할과 의도 통합**  
   - 시스템의 역할과 작업 범위를 명확히 설정  
   - **예시**: "너는 이 논문을 전공한 교수야. 논문 내용을 바탕으로 질문에 답변해."

2. **간결하고 직접적인 질문 유도**  
   - 사용자 질문이 짧고 명확하도록 설계  
   - **예시**: "논문의 주요 기여를 한 문장으로 설명해."

3. **논문 내용 중심**  
   - 답변은 반드시 논문 내용만을 기반으로 작성  
   - **예시**: "논문에 없는 내용은 답하지 마."

4. **외부 정보 추가 금지**  
   - 논문 외 정보를 포함하지 않도록 제한  
   - **예시**: "논문 내용 외의 가정이나 예측은 하지 마."

=================

이 시스템은 논문 텍스트와 수식을 포함한 내용을 기반으로 질문에 정확하고 신뢰성 있는 답변을 제공하는 데 중점을 둡니다.


# 역할

커맨더 : 지수  
아키텍처 : 윤형 , 장호  
코드 리뷰어 : 상민, 나은  
sw 엔지니어 : 연승, 진우  
발표 : 대현  
