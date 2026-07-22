#2~6 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub                                                      
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub() #허브(프라임 허브)이름 설정

def setup_motors_and_basebot(): #모터,베이스봇 정의(간결화용 함수)
    global a_m, e_m, b_m, f_m, drive_base
    a_m = Motor(Port.A, Direction.COUNTERCLOCKWISE)  # 왼바퀴
    e_m = Motor(Port.E, Direction.CLOCKWISE)         # 오른바퀴
    b_m = Motor(Port.B, Direction.CLOCKWISE)         # 왼팔
    f_m = Motor(Port.F, Direction.COUNTERCLOCKWISE)  # 오른팔
    drive_base = DriveBase(a_m, e_m, wheel_diameter=54, axle_track=120) #베이스봇, 로봇설정([a_m, e_m] = (바퀴 설정)), (wheel_diameter=54 = (바퀴 지름(54mm))), (axle_track=120 = (로봇 폭(120mm))) 그리고 이를 drive_base를 변수로 저장
setup_motors_and_basebot()   # 실행해서 실제로 모터, 베이스봇 정의

def hub_preparation(): #(간결화용 함수)
    hub.imu.ready()             #자이로 사용 준비
    hub.imu.reset_heading(0)    #현재 방향(각도)를 0으로 설정
    drive_base.use_gyro(True)   #자이로 사용
hub_preparation() #허브 세팅

if True: #함수 설정(def - 이 명령어가 함수), 접어서 편하게 볼 수 있도록 항상 허용되는 if True 명령문을 사용
    def move(mm, speed=700, speed_acceleration=700):    #앞, 뒤 움직이기
        #매개변수(move 옆에있는 s(speed), sa(speed acceleration))를 속도 및 가속에 반영(33줄)
        drive_base.settings(straight_speed=speed, straight_acceleration=speed_acceleration) 
        drive_base.straight(mm) #앞으로 움직이기(mm) (straight 명령어)
    def curve(speed, speed_acceleration, degree, radius): #회전 움직이기
        #매개변수(move 옆에있는 s(speed), sa(speed acceleration))를 속도 및 가속에 반영(39줄)
        drive_base.settings(turn_rate=speed, turn_acceleration=speed_acceleration)
        #--------------------------------------------------------------------------------------
        #(r(radius) = (비)) - 회전을 할때 얼마나 크게 돌지에 대한 비를 정함 (44줄)
        #(d(dgrees) = (각도)) - 몇도를 돌건지 정함 (44줄)
        #위 두가지를 조합하여 curve 명령어로 움직임
        drive_base.curve(radius=radius, angle=degree) 
    def f_motor_run(speed, degree): #오른쪽 모터 돌리기
        #(s(speed) = 속도) - 돌리는 속도 설정, (deg(degrees) = 각도) - 몇 도를 돌릴건지 설정 이를 run angle 명령어를 사용해 구현
        f_m.run_angle(speed, degree)
    def b_motor_run(speed, degree): #왼쪽 모터 돌리기
        #(s(speed) = 속도) - 돌리는 속도 설정, (deg(degrees) = 각도) - 몇 도를 돌릴건지 설정 이를 run angle 명령어를 사용해 구현
        b_m.run_angle(speed, degree)
    