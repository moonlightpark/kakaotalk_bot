
# Neovim KakaoTalk Plugin

## 설명
nvim 작업시 카톡창이 다른 모니터에 있어 마우스를 움직이는 것이 귀찮아서<br>
구현하게 되었습니다. <br>
<br>
## 구성
```
.
├── README.md
├── kakao-server
│   ├── main.py
│   └── requirements.txt
└── nvim-kakaobot
    └── lua
        └── kakaobot.lua
```


## 사용법

1. 플러그인 설치
```bash
cp -p ./nvim-kakaobot/lua/kakaobot.lua ~/.config/nvim/lua/kakaobot.lua
```

2. Neovim 설정에 플러그인 추가
```lua
# ~/.config/nvim/init.lua에 추가
require("kakaobot")

kakaobot.lua > ~/.config/nvim/lua/ 에 복사
linebot.lua > ~/.config/nvim/lua/ 에 복사
```


3. 서버 실행
```bash
use 8000 port
cd ./kakao-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py


use 8001 port
cd ./line-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

4. nvim 실행한뒤 
```
<space> -> ks # KAKAO 메시지 전송
<space> -> kr # KAKAO 응답 가져오기
<space> -> ls # LINE 메시지 전송
<space> -> lr # LINE 응답 가져오기
```

