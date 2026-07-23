#미션 3, 4, 13

#4~8 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m
from lqr_test import turn_point
hub = PrimeHub()    #허브(프라임 허브)이름 설정

def go_to_mineshaft_explorer():
        drive_base.heading_control.pid(10000, 2, 5310, 3, 6)
        drive_base.use_gyro(True)
        hub.imu.reset_heading(0)
        wait(500)               #출발 오차를 줄이기 위해 0.5초 기다렸다가 시작
        hub.imu.reset_heading(0)#출발하기 전에 자이로의 요도 방향을 0도로 설정
        move(980, 700, 300)    #앞으로 1100(mm)이동하여 벽정렬 및 앞으로 이동
        drive_base.stop()       #정확한 90도를 돌아야 하므로 요도 방향을 0으로 설정해야해서 로봇 멈추기
        hub.imu.reset_heading(0)#정확한 90도를 돌아야 하므로 요도 방향을 0으로 설정
        move(-117)    #뒤로 이동하여 유물을 들기 위한 위치 맞추기
        drive_base.stop()
        curve(100, 50, 90, 0)
def minesaft_explorer():
        drive_base.stop()       #로봇을 멈추며 보정
        drive_base.heading_control.pid(9000, 0, 0) #pid 제어값 최적에 맞게 튜닝
        drive_base.use_gyro(True) #보정 끄기
        b_motor_run(100, -150)  #왼팔 내리기    
        f_motor_run(700, 114)   #오른팔 내리기
        drive_base.stop()       #로봇을 멈추며 보정
        drive_base.heading_control.pid(10000, 0, 20)
        move(110, 100, 50)     #앞으로 천천히 이동하여 유물 끼우기
        b_m.run_target(200, -117)#먼저 왼팔을 조금 올려 유물 들어올리기
        f_motor_run(200, -90)   #오른팔을 들어 갱도 탐험가 해결
        wait(1000)              #1초 기다리며 광차 보내기
        drive_base.heading_control.pid(9000, 3000, 6000, 5, 13) #pid 제어값 최적에 맞게 튜닝
        move(-120, 50, 25)      #뒤로 이동하며 유물 꺼내기
        drive_base.use_gyro(True) #보정 다시 사용
        f_m.run_target(200, 0)  #오른팔을 0도로 맞추며 들기
        b_m.run_target(200, 0)  #왼팔을 0도로 맞추며 들기
def go_to_statue_rebuild():
        drive_base.heading_control.pid(21242, 2, 5310, 3, 6)
        curve(700, 300, -90, 0) #90도 회전하여 뒤로 가는 방향 맞추기
        move(-100)    #뒤로 100(mm)이동하여 조각상 재건 방향으로 이동
        curve(700, 300, 90, 0)  #90도 회전하여 조각상 재건 하러 방향 맞추기
        move(170)     #앞으로 이동하여 팔을 넣을 위치 맞추기
        curve(700, 300, 46, 0)  #41도 회전하여 조각상 재건과 방향 맞추기
        f_motor_run(700, 110)   #오른팔을 내려서 팔이 들어갈 수 있도록 하기
def statue_rebuild():
        move(210)     #조각상에 팔 넣기
        f_m.run(-20)            #왼쪽 팔 드는방향으로 동작 시작하기
        wait(1200)
        curve(300, 300, -20, 0) #왼쪽으로 13도 돌아 조각상 재건 해결 안정성 높이기
        wait(100)
        f_m.run_target(700, 0)  #모터를 0점으로 맞추며 완전히 들어올리기
        f_m.stop()              #모터 멈추며 정상화
        curve(700, 700, 15, 0)  #아까 20도 돌아서 다시 상쇄
def go_home():
        move(-190)    #다시 뒤로 이동
        curve(700, 700, -41, 0) #홈으로 복귀할 수 있도록 아까 41도 돌았기에 반대 방향을 41도 호지너
        move(-160)    #뒤로 이동하여 복귀 할수 있도록 지도공개 옆으로 이동하기
        curve(700, 700, -80, 0) #90도 돌며 홈이랑 방향 맞추기
        drive_base.use_gyro(False)
        move(-700)    #뒤로 이동하여 홈으로 복귀


def run_3():                #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    go_to_mineshaft_explorer()
    minesaft_explorer()
    go_to_statue_rebuild()
    statue_rebuild()
    go_home()