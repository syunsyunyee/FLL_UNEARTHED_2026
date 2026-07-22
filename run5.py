#미션 1, 2

#2~6 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#전에 작성한 import_def.py 코드에서 move/curve/clean/f_motor_run/b_motor_run/drive_base/b_m 함수 및 변수를 불러옴
from import_def import move, curve, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m

hub = PrimeHub()    #허브(프라임 허브)이름 설정
def solve_salvage_operation_and_angler_artifacts():
    drive_base.use_gyro(True)
    move(490, 900, 900)         #앞으로 670(mm)이동하여 구출작전의 모래 제거를 위해 일방통행 구조에 레버를 걸기
    a_m.dc(-100)                #최대속도로 뒤로움직이기
    e_m.dc(-100)
    wait(250)                   #0.5초 동안 뒤로가기
    drive_base.stop()           #시작하기 명령어를 사용하였으므로 멈추기
    move(140, 500, 500)         #앞으로 이동하여 구출 작전 미션해결
    b_motor_run(700, 520)       #팔을 내리며 낚시꾼 유물 미션 해결에 맞추기
    move(40)          #앞으로 조금 이동하여 기어가 완전히 맞물리게 하기
    f_m.dc(-100)                #낚시꾼 유물 미션 해결하기(100% 속도)
    wait(1500)                  #이것도 모터 키기 이므로 1.5초 기다리기
    f_m.stop()                  #그리고 모터 멈추기
    move(-30)         #뒤로 이동하여 팔 들어올릴 공간 만들기
    b_motor_run(700, -480)      #팔 들어올리
    drive_base.use_gyro(False)
    curve(700, 700, 6, -5000)   #살짝 휘며 홈으로 돌아가기
    drive_base.stop()


def run_5():                    #나중에 main(주 실행창)에서 불러오기 위해 함수로 실행 저장
    solve_salvage_operation_and_angler_artifacts()