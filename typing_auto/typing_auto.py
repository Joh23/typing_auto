from pynput.keyboard import Key, Controller
import time
import platform
import random

keyboard = Controller()

def press_and_release(key):
    keyboard.press(key)
    time.sleep(random.uniform(0.01, 0.05))
    keyboard.release(key)

def switch_input_mode():
    press_and_release(Key.cmd)
    press_and_release(Key.space)
    time.sleep(random.uniform(0.2, 0.4))

def simulate_typo(char):
    typo_char = random.choice('qwertasdfgzxcvb')
    keyboard.type(typo_char)
    time.sleep(random.uniform(0.1, 0.3))
    press_and_release(Key.backspace)
    time.sleep(random.uniform(0.1, 0.3))
    keyboard.type(char)

def type_text_block(block, korean_mode):
    print(f"입력 모드: {'한글' if korean_mode else '영문'}, 블록: {block}")
    if korean_mode:
        switch_input_mode()
    
    for char in block:
        if random.random() < 0.05:  # 5% 확률로 오타 발생
            simulate_typo(char)
        else:
            keyboard.type(char)
        
        if char in [' ', ',', '.']:
            time.sleep(random.uniform(0.1, 0.3))
        else:
            time.sleep(random.uniform(0.05, 0.15))
    
    if korean_mode:
        switch_input_mode()

def type_text(text):
    sentences = text.split('.')
    for sentence in sentences:
        if not sentence.strip():
            continue
        
        korean_mode = any('가' <= char <= '힣' for char in sentence)
        type_text_block(sentence.strip() + '. ', korean_mode)
        time.sleep(random.uniform(0.5, 1.0))  # 문장 사이 불규칙한 딜레이

def human_like_typing(text):
    print("타이핑을 시작합니다...")
    print(f"입력할 텍스트: {text}")
    
    print("영문 테스트 메시지 출력:")
    type_text("This is a test message.")
    time.sleep(random.uniform(1.0, 1.5))
    
    print("한글 테스트 메시지 출력:")
    type_text("이것은 테스트 메시지입니다.")
    time.sleep(random.uniform(1.0, 1.5))
    
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