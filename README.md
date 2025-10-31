# 🏋️ Fitness-Follow

헬스장에서 트레이너와 회원이 카톡, 밴드, 종이기록 등으로 분산 관리되던 소통과 일정을  
한 곳에서 통합 관리할 수 있도록 설계한 Django 기반 프로젝트입니다.

<br/>

## 🚀 핵심 기능

| 기능 | 설명 |
|------|------|
| 🔐 회원/트레이너/대표 인증 | JWT 기반 로그인, 권한별 접근 제어 |
| 🏢 헬스장 등록 및 회원 관리 | 하나의 회원이 여러 헬스장에 소속 가능 |
| 💬 트레이너-회원 채팅 | WebSocket 기반 실시간 채팅 |
| 🏋️ 운동 프로그램 관리 | 트레이너가 회원별 운동 루틴 등록/수정 |
| 🧾 알림/정산 (추후 개발 사항) | Redis Pub/Sub / 결제 데이터 확장 가능 |

<br/>


## 📚 기술 스택

- **Backend:** Django 5 + Django REST Framework
- **DB:** PostgreSQL
- **Cache:** Redis
- **Infra:** Docker Compose
- **Auth:** JWT (SimpleJWT)
- **Docs:** Swagger (drf-yasg)

---
