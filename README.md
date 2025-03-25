
# Neovim KakaoTalk Plugin

## 설명

MacOS 기반으로 neovim용 KakaoTalk 플러그인을 구현한 것입니다.
nvim 작업시 카톡창이 다른 모니터에 있어 마우스를 움직이는 것이 귀찮아서
구현하게 되었습니다. 

## 구성
.
├── README.md
├── kakao-server
│   ├── main.py
│   └── requirements.txt
└── nvim-kakaobot
    └── lua
        └── kakaobot.lua



## 사용법

1. 플러그인 설치
```bash
cp -p ./nvim-kakaobot/lua/kakaobot.lua ~/.config/nvim/lua/kakaobot.lua
```

2. Neovim 설정에 플러그인 추가
```lua
# ~/.config/nvim/init.lua에 추가
require("kakaobot")
```


3. 서버 실행
```bash
cd ./kakao-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```



