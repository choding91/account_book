## 🐣 나만의 가계부 서비스

- 수입/지출 내역 기록 및 관리 서비스 제공

</br>

## 😎 Introduction

- 기간 : 2023.02.01 ~ 2023.02.04
- Solo : 조인걸([Github](https://github.com/Choding91))

</br>

## 🛠 Stacks

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/Django_rest_framework-A50E15?style=for-the-badge&logo=Django&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/MySQL-4169E1?style=for-the-badge&logo=MySQL&logoColor=white">&nbsp;

</br>

## 🤝 Project Rules


### API

- [Notion](https://www.notion.so/API-baa0a4820226466b87bdbfd2938dc451)

</br>

### ERD

![image](https://user-images.githubusercontent.com/113072964/216600371-e905c3e0-38ba-4a3c-b7a9-56e4a68d3a0a.png)

</br>

## 📂 Structure

```
┌─ACCOUNT_BOOK
├── account_book                    // project
│   ├── settings.py                 // setting
│   ├── urls.py                     // base url
│   └── ...
├── posts                           // app
│   ├── models.py                   // DB model - Post
│   ├── serializers.py              // serializers
│   ├── tests.py                    // test cases
│   ├── urls.py                     // posts url
│   ├── views.py                    // view functions
│   └── ...
├── users                           // app
│   ├── models.py                   // DB model - User
│   ├── serializers.py              // serializers
│   ├── tests.py                    // test cases
│   ├── urls.py                     // users url
│   ├── views.py                    // view functions
│   └── ...
├── .gitignore
├── requirements.txt
└── ...
```

</br>

## 💻 Development

#### 구현율 : ★(완료) / ☆(추가 작업 필요)

</br>

### 유저 기능

> [★] 회원가입 : 이메일/비밀번호 입력, 비밀번호 암호화 적용

> [★] 회원탈퇴 : 유저 인증 여부 확인 및 서비스 이용 종료

> [★] 로그인 : Simple JWT/Token(Access, Refresh) 발급

> [☆] 로그아웃 : Simple JWT/Blacklist 적용
>> 로컬스토리지에 저장되는 토큰 특성상 완벽한 로그아웃을 위한 JS 추가 작업 필요

</br>

### 가계부 기능(인증된 유저만 이용 가능)

> [★] 전체 조회 : 가계부 내역 전체 조회

> [★] 등록 : 가계부 신규 등록

> [☆] 상세 조회 : 가계부 내역 상세 조회(+단축 URL)
>> 단축 URL 라이프타임 설정에 대한 추가 작업 필요

> [★] 복제 : 가계부 내역 복제

> [★] 수정 : 가계부 내역 수정

> [★] 삭제 : 가계부 내역 삭제

</br>

## 🛠 Trouble Shooting

<details>
<summary>🐛 가계부 복제 시 동일한 가계부에 덮어쓰기 되는 문제</summary>

</br>

<div>

- 상황 : 가계부 복제 기능 구현 중 기존 가계부에 같은 내용이 덮어쓰기 되는 문제 발생(수정 시간만 변경됨)

![image](https://user-images.githubusercontent.com/113072964/216566037-5f7b4ab6-41bf-4090-ba9f-1778df1ce46a.png)

- 해결 : 기존 id값으로 가계부를 받아온 뒤 id값만 None 처리하여 새로운 가계부로 인식 및 등록 가능

![image](https://user-images.githubusercontent.com/113072964/216563082-b2f4cbb3-5520-4604-bed2-5461e0985196.png)

</div>
</details>
