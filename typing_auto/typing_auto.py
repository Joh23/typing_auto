from pynput.keyboard import Key, Controller
import time
import platform

keyboard = Controller()

def press_and_release(key):
    keyboard.press(key)
    keyboard.release(key)

def switch_to_korean():
    press_and_release(Key.cmd)
    press_and_release(Key.space)
    time.sleep(0.5)  # 충분한 딜레이 제공

def switch_to_english():
    press_and_release(Key.cmd)
    press_and_release(Key.space)
    time.sleep(0.5)  # 충분한 딜레이 제공

def type_text_block(block, korean_mode):
    if korean_mode:
        switch_to_korean()
    else:
        switch_to_english()
    
    for char in block:
        keyboard.type(char)
        time.sleep(0.1)

def type_text(text):
    korean_mode = None
    block = ''
    
    for char in text:
        if '가' <= char <= '힣':
            if korean_mode is False:
                type_text_block(block, korean_mode)
                block = ''
            korean_mode = True
        else:
            if korean_mode is True:
                type_text_block(block, korean_mode)
                block = ''
            korean_mode = False
        
        block += char
    
    if block:
        type_text_block(block, korean_mode)

def human_like_typing(text, speed=0.1):
    print("타이핑을 시작합니다...")
    print(f"입력할 텍스트: {text}")
    
    print("영문 테스트 메시지 출력:")
    type_text("This is a test message. ")
    time.sleep(1)
    
    print("한글 테스트 메시지 출력:")
    type_text("이것은 테스트 메시지입니다. ")
    time.sleep(1)
    
    print("사용자 입력 텍스트 출력:")
    type_text(text)
    
    print("타이핑이 완료되었습니다.")

def get_system_info():
    return f"OS: {platform.system()} {platform.release()}, Python: {platform.python_version()}"

def main():
    print("자동 타이핑 프로그램을 시작합니다.")
    print(f"시스템 정보: {get_system_info()}")
    
    text = input("타이핑할 텍스트를 입력하세요: ")
    
    print("5초 후에 타이핑을 시작합니다. 원하는 입력 창을 선택하세요.")
    for i in range(5, 0, -1):
        print(f"{i}초 남았습니다...")
        time.sleep(1)
    
    human_like_typing(text)
    
    print("프로그램이 종료됩니다. 엔터 키를 눌러주세요.")
    input()

if __name__ == "__main__":
    main()
