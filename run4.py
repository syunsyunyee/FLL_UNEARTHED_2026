#미션 1, 2

#4~8 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, f_m

hub = PrimeHub()    #허브(프라임 허브)이름 설정



def go_and_solve_map_reveal():
        drive_base.use_gyro(True)
        move(655)         #지도 공개 미션을 하기 위해 앞으로 이동
        curve(100, 100, -45, 45)    #42도 회젼하며 방향 맞추기
        move(270, 300, 300)         #앞으로 이동하여 미션 해결
        f_motor_run(100, 45)        #오른팔을 들며 포토 색션 들어올리기
        move(-129)        #뒤로 빠지기
def go_and_solve_surface_brushing():
        curve(700, 700, 42, -100)   #45도를 회전하며 표면 붓질과 방향 맞추기
        drive_base.stop()           #멈추며 보정 X
        move(210, 300, 280)         #앞으로 이동하여 정렬
        move(-15, 500, 500)         #앞으로 이동하여 정렬
        drive_base.stop()
        b_motor_run(700, 660)      #렉기어 내리기
        b_motor_run(700, -700)       #렉기어 올리며 미션 해결
        drive_base.stop()
        wait(250)
def go_home():
        move(-130)        #뒤로 150(mm)이동하여 홈으로 들어가기 위해 위치 맞추기
        curve(700, 700, 100, 0)     #100도 회전하여 홈이랑 방향 맞추기
        drive_base.use_gyro(False)
        move(-700)        #뒤로 이동하여 홈으로 돌아오기


def run_4():                    #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    go_and_solve_map_reveal()
    go_and_solve_surface_brushing()
    go_home()
    
'''
b_motor_run(700, 630)      #렉기어 내리기
b_motor_run(700, -630)
'''