#미션 3, 4, 13

#4~8 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/clean/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, clean, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m
from lqr_test import turn_point

hub = PrimeHub()    #허브(프라임 허브)이름 설정
drive_base.use_gyro(True)
print(drive_base.heading_control.pid())
drive_base.heading_control.pid(5000, 500, 6000, 2, 8)
print(drive_base.heading_control.pid())

from lqr_test import turn_point 

def move(s, sa, mm):    #앞, 뒤 움직이기

    #매개변수(move 옆에있는 s(speed), sa(speed acceleration))를 속도 및 가속에 반영(33줄)
    drive_base.settings(straight_speed=s, straight_acceleration=sa) 
    drive_base.straight(mm) #앞으로 움직이기(mm) (straight 명령어)

def curve(s, sa, d, r): #회전 움직이기
    #매개변수(move 옆에있는 s(speed), sa(speed acceleration))를 속도 및 가속에 반영(39줄)
    drive_base.settings(turn_rate=s, turn_acceleration=sa)
#--------------------------------------------------------------------------------------
    #(r(radius) = (비)) - 회전을 할때 얼마나 크게 돌지에 대한 비를 정함 (44줄)
    #(d(dgrees) = (각도)) - 몇도를 돌건지 정함 (44줄)
    #위 두가지를 조합하여 curve 명령어로 움직임
    drive_base.curve(radius=r, angle=d)
    


move(800, 800, 800)
wait(50)
turn_point(90, False)
wait(50)
turn_point(-90, False)
wait(50)
turn_point(0, False)
wait(50)
move(800, 800, -780)
