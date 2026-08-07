#미션 9, 10

#4~8 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from math import e
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/clean/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m
hub = PrimeHub()        #허브(프라임 허브)이름 설정


def go_to_whats_on_sale():
        drive_base.use_gyro(True)
        f_m.run_target(1000, 0) # 앞쪽 모터 원위치
        b_m.run_target(1000, 0)
        move(119)         #세일 상품 미션을 해결하기위해 앞으로 이동하여 
        curve(700, 500, -45, 0)     #왼쪽으로 45도 회전하여 방향 맞추기
        move(330)         #세일 상품을 올리기 위해 앞으로 이동
def whats_on_sale():
        curve(700, 500, -50, 0)     #왼쪽으로 50도 돌며 레버를 내리고 상품을 들어올리기
        curve(300, 300, 48, 95)     #오른쪽으로 돌며 저울 기울이기 및 지붕을 올리기 위한 방향 맞추기
        b_m.dc(-70)
        f_m.dc(70)
        wait(190)
        b_m.stop()
        f_m.stop()
        wait(1000)                  
        move(-155)        #뒤로 이동하며 지붕 올리기
        wait(1000)
        b_m.dc(70)
        f_m.dc(-70)
        wait(190)                  
        b_m.stop()
        f_m.stop()
        wait(90)
def go_to_tip_the_scale():
        move(60)         #뒤로 조금 이동하여거리 맞추기
        curve(700, 700, -40, 0)     #왼쪽으로 돌며 저울 기울이기의 획득물을 얻기 위해 옆으로 돌기
        move(163)         #위치를 맞추기 위해 앞으로 이동
def tip_the_scale():
        curve(700, 700, 65, 60)     #옆으로 돌며 유물의 고리에 축 넣기
        wait(50)
        move(-80)         #뒤로 조금 빠지며 뽑을 준비
        curve(100, 100, -62, 0)     #옆으로 회전하며 완전히 뽑기
def go_home():
        wait(1000)
        curve(700, 700, -13, 5300)


def run_2():                    #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    go_to_whats_on_sale()
    whats_on_sale()
    go_to_tip_the_scale()
    tip_the_scale()
    go_home()