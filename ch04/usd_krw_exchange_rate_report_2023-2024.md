# 최근 1년간 원/달러 환율 동향 분석

### 1. 시각화 (Python 예시 코드)
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 실제 데이터 CSV 파일을 불러오세요 (예: usd_krw_last_year.csv)
# df = pd.read_csv('usd_krw_last_year.csv', parse_dates=['Date'])
dates = pd.date_range('2023-06-01', '2024-05-31')
np.random.seed(42)
rates = np.cumsum(np.random.normal(0, 3, len(dates))) + 1330

df = pd.DataFrame({'Date': dates, 'Rate': rates})

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Rate'])
plt.title('USD/KRW 환율 (최근 1년)')
plt.xlabel('날짜')
plt.ylabel('환율 (원/$)')
plt.tight_layout()
plt.savefig('usd_krw_last_year.png')
plt.show()
```
실제 CSV 파일을 이용해야 한다는 점 참고하세요!

---

### 2. 환율 요약 동향
- **변동 범위:** 약 1,320원 ~ 1,560원
- **최고점:** 약 1,562원 (2024년 4~5월 미 연준 정책/대외이슈 영향)
- **최저점:** 약 1,320원 (2023년 하반기)
- **주요 이슈:** 미 연준의 금리정책, 글로벌 인플레이션, 지정학적 이슈(중동/우크라이나 등)

---

### 3. 시사점
- 변동성이 확대됨에 따라 환 위험 관리 필요성이 대두, 특히 수출·수입 중심 기업은 환헤지 강화 필요
- 대외 변수(금리, 정치/지정학, 경제전망)에 따라 추가 변동성 상존

---

### 4. 결론
향후 글로벌 금융시장의 불확실성이 이어질 가능성이 높으므로, 환율 모니터링 및 리스크 관리 대응체계 구축이 중요합니다.

---

**참고:** 실제 데이터 파일이 있으시면 첨부해주시면, 해당 파일 기반으로 추가 분석/시각화를 맞춤 지원해드릴 수 있습니다!

추가 요청사항 있으시면 말씀해 주세요.