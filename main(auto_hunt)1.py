# python version = 3.9.6 64bit




import threading
import time
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode, Controller as KeyboardController
import pyautogui
import easyocr
import cv2
import numpy as np
from PIL import ImageGrab, Image
import pytesseract


# 마우스 및 키보드 컨트롤러 초기화
mouse = MouseController()
keyboardC = KeyboardController()

# 메타변수
stop = 0
full_mp = 0
HP = 0
MP=0
MON=0
wait = 0
kill=0
pos_x=0
pos_y=0


# 기본기능힘수
def send_key(k):
    keyboardC.press(k)
    keyboardC.release(k)
    return
def ctrl_n(n):
    time.sleep(0.01)
    keyboardC.press(Key.ctrl)
    time.sleep(0.04)
    keyboardC.press(n)
    keyboardC.release(n)
    time.sleep(0.04)
    keyboardC.release(Key.ctrl)
    time.sleep(0.01)
    return
def send_2key(k1,k2):
    time.sleep(0.01)
    keyboardC.press(k1)
    time.sleep(0.04)
    keyboardC.press(k2)
    keyboardC.release(k2)
    time.sleep(0.04)
    keyboardC.release(k1)
    time.sleep(0.01)
    return
def send_key_enter(k):
    send_key(k)
    time.sleep(0.05)
    send_key(Key.enter)
    time.sleep(0.05)


# 상황 체커

def check_mp_th():
    check_mp_thr=threading.Thread(target=check_mp)
    check_mp_thr.daemon=True
    check_mp_thr.start()
def check_mp():
    global MP
    print('마나통을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95)
            print('공증을 쓰시오')
            MP=1
        except:
            MP=0

def check_hp_th():
    check_hp_thr=threading.Thread(target=check_hp)
    check_hp_thr.daemon=True
    check_hp_thr.start()
def check_hp():
    global kill,HP
    print('피통을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            pyautogui.locateCenterOnScreen(image="hp_low.png",confidence=0.95)
            print('low hp')
            HP=1
        except :
            HP=0
            None

# 몬스터 체커
def check_mon_th():
    check_mon_thr=threading.Thread(target=check_mon)
    check_mon_thr.daemon=True
    check_mon_thr.start()
def check_mon():
    global MON
    print('주변 몹을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            # 갈색인형
            pyautogui.locateCenterOnScreen(image="doll_brown2.png",confidence=0.7)
            print('갈색인형 있음')
            MON=1
        except:
            try:
                # 갈색인형
                pyautogui.locateCenterOnScreen(image="doll_brown3.png",confidence=0.7)
                print('청색인형 있음')
                MON=1
            except:
                MON=0



def get_pos3():
    global pos_x, pos_y
    while 1:
        if kill==1:
            break
        im = ImageGrab.grab(bbox=(1133,905,1280,930))
        # im.show()
        screenshot_np = np.array(im)
        # results= pytesseract.image_to_string(screenshot_np)
        results= pytesseract.run_and_get_output(im)
        # results= pytesseract.run_and_get_output(screenshot_np)
        print(results)
        # print('현위치 x=',results[0], 'y=',results[1])
        # pos_x=int(results[0])
        # pos_y=int(results[1])
        # time.sleep(0.5)
        break

def get_pos2():
    global pos_x, pos_y
    reader = easyocr.Reader(['en'])
    while 1:
        if kill==1:
            break
        im = ImageGrab.grab(bbox=(1133,905,1280,930))
        # im.show()
        screenshot_np = np.array(im)
        results= reader.readtext(screenshot_np, detail=0, allowlist='0123456789')
        print('현위치 x=',results[0], 'y=',results[1])
        pos_x=int(results[0])
        pos_y=int(results[1])
        time.sleep(0.5)

def get_pos_th():
    global kill
    kill=0
    get_pos_thr=threading.Thread(target=get_pos2)
    get_pos_thr.daemon=True
    get_pos_thr.start()



# 반복 멈추기
def stop_sign():
    global stop
    stop=1


def 동에서인형까지걷기():
    while 1:
        if 고구려용성맞나():
            break
        else:
            print('용성으로가자')
            용성으로가기()
            time.sleep(1)
    print('비영동')
    비영동()
    get_pos_th()
    동시작점으로이동()
    인형사냥()

def 용성으로가기():
    send_2key(Key.shift,'z')
    time.sleep(0.1)
    send_key('o')

def 고구려용성맞나():
    try:
        pyautogui.locateCenterOnScreen(image="용성.png",confidence=0.75,grayscale=True)
        print('용성 맞음')
        return 1
    except:
        print('용성 아님')
        return 0
def 비영동():
    send_key('0')
    time.sleep(0.1)
    send_key_enter('1')
def 동시작점으로이동():
    위치이동(209,108)
    위치이동(187,108)
    위치이동(187,119)
    위치이동(185,119)
    위치이동(185,131)
    위치이동(178,131)
    위치이동(178,115)
    위치이동(174,115)
    send_key(Key.up)
def 위치이동(목표x, 목표y):
    global pos_x, pos_y, kill
    while 1:
        print(pos_x,pos_y)
        if pos_x==목표x:
            if pos_y==목표y:
                print('목적지 도착')
                break
        if pos_x>목표x:
            time.sleep(0.2)
            send_key(Key.left)
            time.sleep(0.2)
        if pos_x<목표x:
            time.sleep(0.2)
            send_key(Key.right)
            time.sleep(0.2)
        if pos_y>목표y:
            time.sleep(0.2)
            send_key(Key.up)
            time.sleep(0.2)
        if pos_y<목표y:
            time.sleep(0.2)
            send_key(Key.down)
            time.sleep(0.2)

def 인형사냥():
    print('인형사냥하자')
    인형1굴()

def 인형1굴():
    global kill
    kill=1
    print('인형1굴')
    while 1:
        kill=0
        check_mp_th()
        get_pos_th()
        try:
            pyautogui.locateCenterOnScreen(image="용성인형굴1.png",confidence=0.75,grayscale=True)
            time.sleep(1)

        except:
            일회이동(174,114)
            kill=1
            continue
        이동전투(4,18)
        이동전투(18,18)
        kill=1
        change_channel()
        # 이동전투(18,11)
        # 이동전투(23,11)

def 이동전투(x,y):
    global pos_x, pos_y
    while 1:
        send_key(Key.esc)
        time.sleep(0.1)
        send_key(Key.tab)
        time.sleep(0.1)
        send_key(Key.home)
        time.sleep(0.1)
        send_key(Key.tab)
        if x==pos_x:
            if y==pos_y:
                break

        if 일회이동(x, y):break
        전투()

def 일회이동(목표x, 목표y):
    global pos_x, pos_y, kill

    print(pos_x,pos_y)
    if pos_x==목표x:
        if pos_y==목표y:
            print('목적지 도착')
            return 1
    if pos_x>목표x:
        time.sleep(0.15)
        send_key(Key.left)
        time.sleep(0.15)
    if pos_x<목표x:
        time.sleep(0.15)
        send_key(Key.right)
        time.sleep(0.15)
    if pos_y>목표y:
        time.sleep(0.15)
        send_key(Key.up)
        time.sleep(0.15)
    if pos_y<목표y:
        time.sleep(0.15)
        send_key(Key.down)
        time.sleep(0.15)
    
def 몹탐색():
    time.sleep(0.2)
    send_2key(Key.shift,Key.left)
    time.sleep(0.05)
    send_key(';')
    time.sleep(0.05)
    send_2key(Key.shift,Key.down)
    time.sleep(0.05)
    send_key(';')
    time.sleep(0.05)
    send_2key(Key.shift,Key.right)
    time.sleep(0.05)
    send_key(';')
    time.sleep(0.05)
    send_2key(Key.shift,Key.up)
    time.sleep(0.05)
    send_key(';')
    time.sleep(0.05)
    try:
        pyautogui.locateCenterOnScreen(image="인형탐색2.png",confidence=0.70,grayscale=True)
        print('몹이 있다. 전투개시!')
        return 1
    except:
        print('몹없음')

        send_key('6')

        호박()
        return 0

def 전투():
    while 몹탐색():
        # send_key(Key.tab)
        # time.sleep(0.2)
        # send_key(Key.tab)
        # time.sleep(0.2)
        for i in range(20):
            if MP==1:
                time.sleep(0.1)
                send_key('3')
                time.sleep(0.1)
                
            send_key('2')
            time.sleep(0.1)
            send_key('4')
            time.sleep(0.1)
            send_key('4')
            time.sleep(0.1)
            send_key('4')
            time.sleep(0.1)
  
            send_key('5')
            time.sleep(0.1)
            send_key('6')
            time.sleep(0.1)
        # send_key(Key.esc)
        # time.sleep(0.1)
        # send_key(Key.esc)
        # time.sleep(0.1)

def 호박():

    try:
        pyautogui.locateCenterOnScreen(image="호박.png",confidence=0.70,grayscale=True)
        print('호박 있다. 먹자!')
        줍줍()
        for i in range(6):
            send_key('6')
            time.sleep(0.1)
        return 1
    except:
        print('호박없음')
        return 0

def 줍줍():
    send_key(Key.up)
    time.sleep(0.7)
    send_key(',')
    time.sleep(0.7)
    send_key(Key.down)
    time.sleep(0.7)
    send_key(Key.left)
    time.sleep(0.7)
    send_key(',')
    time.sleep(0.7)
    send_key(Key.right)
    time.sleep(0.7)
    send_key(Key.right)
    time.sleep(0.7)
    send_key(',')
    time.sleep(0.7)
    send_key(Key.left)
    time.sleep(0.7)
    send_key(Key.down)
    time.sleep(0.7)
    send_key(',')
    time.sleep(0.7)
    send_key(Key.up)
    time.sleep(0.7)


def check_mp_th():
    global kill
    kill=0
    check_mp_thr=threading.Thread(target=check_mp)
    check_mp_thr.daemon=True
    check_mp_thr.start()
def check_mp():
    global MP
    print('마나통을 체크 합니다.')
    while 1:
        if kill==1:break
        
        try:
            pyautogui.locateCenterOnScreen(image="mana_low2.png",confidence=0.95)
            print('공증을 쓰시오')
            MP=1
        except:
            MP=0




def change_channel():
    print('채널 체인지')
    change_img_check('change_1.png')
    # pyautogui.moveTo(100,200,duration=0.3)
    change_img_check('change_2.png')
    # pyautogui.moveTo(200,250,duration=0.3)
    change_img_check('change_3.png')
    # pyautogui.moveTo(300,300,duration=0.3)
    change_img_check('change_4.png')
    # pyautogui.moveTo(400,350,duration=0.3)
    change_img_check('change_5_1.png')
    # pyautogui.moveTo(500,400,duration=0.3)
    change_img_check('change_6.png')

    return
def change_img_check(img):
    while 1:
        try:
            x,y=pyautogui.locateCenterOnScreen(image=img,confidence=0.9)
            print('success!!')
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            pyautogui.leftClick(x/2,y/2)
            time.sleep(0.5)
            return
        except:
            print('실패')
            time.sleep(0.5)
            try:
                x,y=pyautogui.locateCenterOnScreen("timeout_1.png",confidence=0.9)
                print('타임아웃 발생')
                time.sleep(0.5)
                pyautogui.leftClick(x/2,y/2)
                time.sleep(0.5)
                pyautogui.leftClick(x/2,y/2)
                time.sleep(0.5)
                
                while 1:
                    try:
                        x,y=pyautogui.locateCenterOnScreen("timeout_2.png",confidence=0.9)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        pyautogui.leftClick(x/2,y/2)
                        time.sleep(0.5)
                        break
                    except:
                        print('타임아웃2 실패')
                    
            except:
                print('타임아웃1 실패')
    return





# 키 할당
def on_press(key):
    global kill

    
    if key==KeyCode(char='-'): # 공격!
        print(key,"를 눌렀습니다.")
        get_pos_th()

        return

    if key==KeyCode(char='='): # 중지!
        print(key,"를 눌렀습니다.")
        stop_sign()
        kill=1
        return



    if key==KeyCode(char='['): # 국내성 출
        print(key,"를 눌렀습니다.")
        동에서인형까지걷기()

        return

    if key==KeyCode(char=']'): # 사냥터 출
        print(key,"를 눌렀습니다.")
        인형1굴()

        return
    
    if key==KeyCode(char='!'): # 사냥터 출

        print(key,"를 눌렀습니다.")
        kill=1
        return
    
    if key==KeyCode(char='@'): # 공격!
        print(key,"를 눌렀습니다.")
        get_pos3()
        return





# 메인함수
if __name__ == "__main__":

    with Listener(on_press=on_press) as listener:
        listener.join()



