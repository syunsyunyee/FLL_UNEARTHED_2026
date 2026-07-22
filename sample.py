#혼자서 완성
from pybricks.hubs import EssentialHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = EssentialHub()

hub.imu.ready()

Left_wheel = Motor(Port.A)
right_wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(Left_wheel, right_wheel, 54, 111)
pi = int(3.141592)

kp = int(0)
ki = int(0)
kd = int(0)
last_accele = int(0)
wheel_circumference = 54 * pi
kp_imp = 0
ki_imp = 0
kd_imp = 0
last_imp = 0
def gyro_foward(accele_rate, move_distance, start_speed, max_speed, end_speed, gyro_reset=True):
    global last_accele
    global wheel_circumference
    if gyro_reset:  
        hub.imu.reset_heading(0)
    right_wheel.reset_angle(0)
    Left_wheel.reset_angle(0)
    error = int(0)
    kp = 5                     #0.3 의 비례
    ki = 0.01                  #0.001의 값으로 스케일링
    kd = 2.5                   #1의 비로 스케일링
    last_error = 0
    Left_deg = Left_wheel.angle()
    Right_deg = right_wheel.angle()
    for i in range(int(max_speed), int(end_speed), int(accele_rate * -1)):
        last_accele += (wheel_circumference * (i/360))*0.1
    while move_distance - last_accele > wheel_circumference * ((Left_deg + Right_deg)/2)/360:
        Left_deg = Left_wheel.angle()
        Right_deg = right_wheel.angle()
        error = hub.imu.heading()
        kp_imp = kp * error
        ki_imp = (error + last_error)*ki
        kd_imp = (error - last_error)*kd
        last_imp = kp_imp + ki_imp + kd_imp
        Left_wheel.dc(start_speed + last_imp)
        right_wheel.dc(start_speed - last_imp)
        if start_speed < max_speed:
            start_speed += accele_rate
        last_error = hub.imu.heading()
        wait(30)
    
    while last_accele > wheel_circumference * ((Left_deg + Right_deg)/2)*360:
        Left_deg = Left_wheel.angle()
        Right_deg = right_wheel.angle()        
        error = hub.imu.heading()
        kp_imp = kp * error
        ki_imp = (error + last_error)*ki
        kd_imp = (error - last_error)*kd
        last_imp = kp + ki + kd
        Left_wheel.dc(start_speed + last_imp)
        right_wheel.dc(start_speed - last_imp)
        if start_speed > end_speed:
            start_speed -= accele_rate
        last_error = hub.imu.heading()
        wait(30)

from import_def import move, curve, clean, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m
def turn_point(target_heading, reset_gyro=True, max_speed=23, min_speed=10, stop_threshold=0.05, max_time=2300):
    if reset_gyro:
        hub.imu.reset_heading(0)
    a_m.reset_angle(0)
    e_m.reset_angle(0)
    stopwatch = StopWatch() 
     
    def state():
        theta = hub.imu.heading()  
        theta_dot = hub.imu.angular_velocity()[2] 
        return theta, theta_dot
    
    def lqr_control(current_state, target_heading, K):
        theta, theta_dot = current_state 
        error = target_heading - theta  
        feedback = K[0] * error + K[1] * theta_dot
        return feedback
    K = [8, 0.1]  
    feedforward_gain = 0.3  
    
    while True:
        current_state = state()  
        feedback_input = lqr_control(current_state, target_heading, K)  
        feedforward_input = feedforward_gain * (target_heading - current_state[0]) 
        control_input = feedback_input + feedforward_input  
        if abs(control_input) < min_speed:
            control_input = min_speed if control_input > 0 else -min_speed
        control_input = max(min(control_input, max_speed), -max_speed)  
        a_m.dc(control_input)
        e_m.dc(-control_input)
        if stopwatch.time() > max_time:
            break
    e_m.brake()
    a_m.brake()


gyro_foward(5, 13340, 5, 100, 30, True)