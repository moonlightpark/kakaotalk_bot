from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import time
import pyautogui
import pyperclip

app = FastAPI()

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
last_message = ""

def send_kakao_message(msg):
    # Line 활성화 (포커스 주기)
    subprocess.run(["open", "-a", "Line"])
    time.sleep(1)

    # 클립보드에 복사 (한글 지원)
    pyperclip.copy(msg)
    time.sleep(0.2)

    # 채팅창이 열려 있어야 함!
    # 붙여넣기 + Enter
    pyautogui.hotkey("command", "v")
    time.sleep(0.1)
    pyautogui.press("enter")

    # 다시 iTerm2로 복귀
    time.sleep(0.3)
    subprocess.run(["open", "-a", "iTerm"])


@app.post("/send")
async def send(msg: str = Form(...)):
    global last_message
    try:
        # 바이트로 처리
        if isinstance(msg, str):
            msg_bytes = msg.encode('latin1')
            decoded_msg = msg_bytes.decode('utf-8')
        else:
            decoded_msg = msg
            
        print(f"💬 받은 메시지: {decoded_msg}")
        send_kakao_message(decoded_msg)
        last_message = f"카카오톡으로 '{decoded_msg}' 전송 완료"
    except Exception as e:
        print(f"디코딩 에러: {e}")
        print(f"원본 메시지: {msg}")
        send_kakao_message(msg)
        last_message = f"카카오톡으로 '{msg}' 전송 완료"

    response = PlainTextResponse(
        content=f"{{\"status\": \"sent\", \"message\": \"{decoded_msg if 'decoded_msg' in locals() else msg}\"}}",
        media_type="application/json; charset=utf-8"
    )
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.get("/response", response_class=PlainTextResponse)
async def response():
    return PlainTextResponse(
        content=last_message or "응답 없음",
        media_type="text/plain; charset=utf-8"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
