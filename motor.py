from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
motor = Motor(Port.B)

# 테스트를 위해 모터 작동 (예: 초당 500도 속도)
motor.dc(100) 

# 무한 루프를 돌며 실시간으로 데이터 뽑아보기
while True:
    speed = motor.speed()  # 현재 실제 속도 (스파이크 앱의 '속도')
    angle = motor.angle()  # 현재 회전 각도 (스파이크 앱의 '각도')
    load = motor.load()    # 현재 걸리는 부하량 (스파이크 앱의 '출력/파워'와 유사한 역할)

    # 하단 터미널 창에 데이터 출력
    print(f"속도: {speed} | 각도: {angle} | 부하(출력): {load}")
    
    # 너무 빠르게 출력되지 않도록 0.1초(100ms) 대기
    wait(100)