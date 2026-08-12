#2~6 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, b_m, f_m

hub = PrimeHub()    #허브(프라임 허브)이름 설정

def forge_and_WHO_LIVED_HERE():
        drive_base.use_gyro(True)
        move(672)         #대장간 및 누가 여기 살았을까요 미션 해결을 위해 앞으로 이동
        curve(50, 30, -90, 65)     #왼쪽 앞 방향으로 회전하며 미션 해결
        move(25)          #앞으로 조금 이동하여 누가 여기 살았을까요 확실하게 해결
        move(-10)         #위치를 다시 맞추기 위해 뒤로 이동
        curve(200, 150, -90, -30)   #다음 미션을 해결하기 위해 뒤로 빠지며 회전
def prepare_silo():
        move(-30)         #사일로 사이로 들어가기 위해 뒤로 조금 이동
        curve(700, 700, 90, 0)      #오른쪽으로90도 회전
        wait(1000)                  #오차 보정을 위해 1초 기다리기
        move(82)          #앞으로 이동하여 완전히 위치 맞추기
def silo():
        b_motor_run(100, -120)      #무거운 짐 들기를 해결하기 위해 왼 팔 내리기
        f_m.run_target(300, -40)
        for i in range(3):          #3번 반복하기
            f_m.dc(-100)#사일로 미션을 해결하기 위해 오른 팔 내리기
            wait(110)
            f_m.stop()
            wait(100)
            f_m.run_target(10000, -40) #사일로 미션을 다시 해결하기 위해 팔 다시 올리기
            wait(300)               #0.03초 기다리기
        f_m.run_target(700, 0)
def heavy_lifting_and_go_home():
        move(110)         #앞으로 조금 가 무거운 짐을 들어올릴 수 있도록 준비
        b_m.run_target(100, 0)      #왼팔 들기(0점)
        drive_base.use_gyro(False)
        move(320)           #앞으로 가 홈으로 들어


def run_1():    #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    forge_and_WHO_LIVED_HERE()
    prepare_silo()
    silo()
    heavy_lifting_and_go_home()