#ai 및 예제 도움 받음
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from import_def import move, curve, f_motor_run, b_motor_run, f_m, b_m, a_m, e_m

hub = PrimeHub()
hub.imu.ready()
'''
pi = 3.141593
wheel_diameter=54
axle_track=111
Left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_wheel = Motor(Port.E)
DriveBase(Left_wheel, Right_wheel, wheel_diameter, axle_track)
wheel_circumference = wheel_diameter * pi

def lqr_point_turn(target_deg, reset_gyro=True, max_speed=100, min_speed=10):
    if reset_gyro:
        hub.imu.reset_heading(0)
    Right_wheel.reset_angle(0)

    def state():
        theta = hub.imu.heading()
        theta_dot = hub.imu.angular_velocity()[2] #<-요센서의 각속도
        return theta, theta_dot
    
    def lqr(current_state, target_deg, K):
        theta, theta_dot = current_state
        error = target_deg - current_state[0]
        feedback = K[0] * error + K[1] * current_state[1]
        return feedback
    K = [7.5540, 3.8210]
    
    ff_gain = 0.4
    while True:
        current_state = state()
        feedback_input = lqr(current_state, target_deg, K)
        feedback_foward_input = ff_gain * (target_deg - current_state[0]) #최소운동량
        control_input = feedback_input + feedback_foward_input
        if abs(feedback_foward_input) < min_speed :
            feedback_foward_input = min_speed
        control_input = max(min(control_input, max_speed), -max_speed)
        Left_wheel.dc(control_input)
        Right_wheel.dc(-control_input)
        # 1. 자이로 센서 오차가 1도 이내로 들어왔을 때
        if abs(target_deg - hub.imu.heading()) < 1.0:
            Left_wheel.hold()
            Right_wheel.hold()
            break
'''
def turn_point(target_heading, reset_gyro=True, max_speed=40, min_speed=5, stop_threshold=0.05, max_time=1800):
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
    K = [7.2, 0.4]  
    feedforward_gain = 0.4  
    
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