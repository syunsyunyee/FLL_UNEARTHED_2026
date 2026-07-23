#2~6 - 기본적인 환경 설정(작업 실행을 위한 툴, 모듈)
from pybricks.hubs import PrimeHub                                                      
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub() #허브(프라임 허브)이름 설정

print(hub.battery.voltage())