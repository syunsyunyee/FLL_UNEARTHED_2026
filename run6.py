#미션 14, 15

#4~8 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/clean/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m

hub = PrimeHub()    #허브(프라임 허브)이름 설정


def forum():
        drive_base.use_gyro(True)
        curve(700, 700, 41, 400)    #옆으로 휘며 포렴의 두 돌 사이로 들어갈 방향 맞추기
        move(160, 200, 200)         #앞으로 이동하여 유물 넣기
        e_m.dc(-100)                #최대속도로 뒤로움직이기
        a_m.dc(-100)                #최대속도로 뒤로움직이기
        wait(700)
        drive_base.stop()
        drive_base.use_gyro(False)
def wait_bluetooth_button():
        while Button.BLUETOOTH not in hub.buttons.pressed():
            wait(10)      
def first_site_marking():
        drive_base.use_gyro(True)
        move(500, 700, 700)         #앞으로 이동하여 현장 표시를 두며 미션 전부 끝내
        curve(100, 50, 90, 200)
        f_motor_run(700, -400)
def second_site_marking():
        move(638, 500, 300)
        curve(300, 100, 90, -0)
        b_motor_run(700, 115)
        move(-80)
        f_motor_run(700, 800)
def get_and_carry_minecart():
        b_motor_run(700, -120)
        move(80)
        curve(300, 300, 90, 0)
        move(460)
        curve(700, 700, -40, 20)
        move(-20)
        b_m.dc(-30)
        wait(800)
        b_m.stop()
        move(-80)
        b_m.run_target(700, 0)


def run_6():                    #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    forum()
    wait_bluetooth_button()
    first_site_marking()
    second_site_marking()
    get_and_carry_minecart()