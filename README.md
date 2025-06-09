# FastAPI Project

이 프로젝트는 FastAPI를 사용하여 구현된 웹 애플리케이션입니다.

## 프로젝트 구조

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 시작하기

### 필수 요구사항

- Python 3.8 이상
- pip (Python 패키지 관리자)

### 설치 방법

1. 저장소를 클론합니다:
```bash
git clone [repository-url]
cd [project-directory]
```

2. 가상환경을 생성하고 활성화합니다:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

3. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

### 환경 설정

1. `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다:
```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

### 실행 방법

개발 서버 실행:
```bash
uvicorn app.main:app --reload
```

서버가 실행되면 다음 URL에서 접근할 수 있습니다:
- API 문서: http://localhost:8000/docs
- 대체 API 문서: http://localhost:8000/redoc

## API 문서

FastAPI는 자동으로 API 문서를 생성합니다. 다음 엔드포인트에서 확인할 수 있습니다:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## 테스트

테스트를 실행하려면:
```bash
pytest
```
