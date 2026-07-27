# -----------------------------------------------------------
# 1. 도구(라이브러리) 가져오기
# 로봇을 움직이기 위해 필요한 기능들을 파이썬 상자로 가져오는 과정입니다.
# -----------------------------------------------------------
from pybricks.hubs import PrimeHub  # 스파이크 프라임 허브(로봇의 두뇌)를 다루기 위한 도구
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor # 모터와 센서 도구
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop # 버튼, 색상, 방향 등의 설정값
from pybricks.robotics import DriveBase # 바퀴 달린 로봇을 쉽게 움직이게 해주는 도구
from pybricks.tools import wait, StopWatch # 시간 기다리기(wait)와 스톱워치 도구
from pybricks.tools import run_task # 미션 코드를 실행시키기 위한 도구
# -----------------------------------------------------------
# 2. 내 로봇 설정 가져오기 (import_def.py 파일에서)
# 다른 파일에 미리 정의해둔 모터와 로봇 설정을 가져옵니다.
# 요청하신 대로 'x_m'은 'x(포트의 위치)에 대한 모터'를 뜻합니다.
# -----------------------------------------------------------
from import_def import f_m, a_m, b_m, e_m, drive_base
# f_m: F포트에 연결된 모터
# b_m: B포트에 연결된 모터
# a_m: A포트에 연결된 모터
# e_m: A포트에 연결된 모터  
# drive_base: 바퀴 두 개를 묶어서 이동을 담당하는 객체
# -----------------------------------------------------------
# 3. 미션(Run) 파일 가져오기
# 각 미션(1번~6번)을 수행할 코드가 담긴 함수들을 가져옵니다.
# -----------------------------------------------------------
from run1 import run_1
from run2 import run_2
from run3 import run_3
from run4 import run_4
from run5 import run_5
from run6 import run_6
# -----------------------------------------------------------
# 4. 초기 설정
# -----------------------------------------------------------
hub = PrimeHub()       # 로봇의 두뇌(허브)를 초기화합니다. (이제 허브를 코드로 제어할 수 있어요)
current_run_index = 0  # 현재 실행할 미션 번호를 저장하는 변수입니다. (0부터 시작)

# 로봇이 켜질 때 모터의 각도를 0도로 맞춰줍니다. (기준점 잡기)
f_m.reset_angle(angle=0) # 앞쪽 모터의 각도를 0으로 초기화
b_m.reset_angle(angle=0) # 뒤쪽 모터의 각도를 0으로 초기화

RUNS = [
    run_1,
    run_2,
    run_3,
    run_4,
    run_5,
    run_6,
]

print(hub.battery.voltage()) #베터리 확인
# -----------------------------------------------------------
# 5. 버튼 입력 대기 함수 (메뉴 선택 기능)
# 로봇의 왼쪽/오른쪽 버튼을 눌러 미션을 고르고, 블루투스 버튼으로 시작하는 함수입니다.
# -----------------------------------------------------------
def wait_for_button_press():
    global current_run_index  # 함수 바깥에 있는 미션 번호 변수를 수정하기 위해 가져옵니다.
    
    # 미션을 고르는 동안에는 모든 모터를 안전하게 멈춥니다.
    a_m.stop()  
    b_m.stop()  
    f_m.stop()  
    e_m.stop()  

    while True:  # 버튼이 눌릴 때까지 무한히 반복해서 검사합니다.
        pressed_buttons = hub.buttons.pressed()  # 현재 눌려있는 버튼들의 목록을 가져옵니다.
        
        # [왼쪽 버튼]을 눌렀을 때: 이전 미션 번호로 이동
        if Button.LEFT in pressed_buttons:
            current_run_index = current_run_index - 1
            # 화면에 숫자를 띄웁니다. 
            # (예: 1번 미션이면 11, 2번이면 22... 이렇게 보이게 해서 숫자를 꽉 차게 보여줍니다)
            hub.display.number(11 * (current_run_index + 1)) 
            wait(200) # 버튼이 한 번만 눌리도록 0.2초 기다립니다 + 최적화
        
        # [블루투스 버튼(가운데)]을 눌렀을 때: 선택 완료!
        elif Button.BLUETOOTH in pressed_buttons:
            return  # 이 함수를 끝내고 메인 코드로 돌아가서 미션을 시작합니다.

        # [오른쪽 버튼]을 눌렀을 때: 다음 미션 번호로 이동
        elif Button.RIGHT in pressed_buttons:
            current_run_index = current_run_index + 1
            hub.display.number(11 * (current_run_index + 1)) 
            wait(200) # 버튼이 한 번만 눌리도록 0.2초 기다립니다. + 최적화
            
        wait(50)  # 너무 빨리 검사하면 로봇이 힘드니까 0.05초 쉽니다. + 최적화
        
        # 현재 선택된 미션 번호를 화면에 계속 보여줍니다.
        hub.display.number(11 * (current_run_index + 1))
        wait(10)
# -----------------------------------------------------------
# 6. 메인 실행 함수
# 실제로 로봇이 작동하는 전체 흐름을 관리합니다.
# -----------------------------------------------------------
def main():
    global current_run_index
    # 미션 번호가 7보다 작을 동안 계속 반복합니다. (여러 번 미션을 수행하기 위해)
    while current_run_index < 6:
        
        # 1단계: 사용자가 버튼을 눌러 미션을 선택하고 시작할 때까지 기다립니다.
        wait_for_button_press()
        wait(200) # 시작 전 잠깐 대기
        drive_base.heading_control.pid(21242, 2, 5310, 3, 6)
        drive_base.use_gyro(True)   #자이로 사용
        run_task(RUNS[current_run_index]())
        current_run_index += 1 # 다음 미션 번호로 자동 넘김
        wait(550) # 미션 종료 후 잠시 대기
        
        # 4단계: 다음 미션을 위해 도구 모터들을 원위치(0도)로 복귀시킵니다.
        # run_target(속도, 각도): 1000의 속도로 0도 위치까지 회전
        f_m.run_target(1000, 0) # 앞쪽 모터 원위치
        b_m.run_target(1000, 0) # 뒤쪽 모터 원위치
        
# 이 프로그램이 시작되면 main() 함수를 가장 먼저 실행합니다.
main()