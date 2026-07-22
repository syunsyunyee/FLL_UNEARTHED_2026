from pybricks.hubs import PrimeHub                                                      
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub() #허브(프라임 허브)이름 설정
from import_def import move, curve, clean, f_motor_run, b_motor_run, drive_base, f_m, b_m, a_m, e_m

'''
drive_base.use_gyro(False)
e_m.dc(100)
a_m.dc(100) 
wait(8000)
'''
import asyncio
from bleak import BleakScanner

async def main():
    print("블루투스 검색 중...")
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name:
            print(f"발견된 기기: {d.name} ({d.address})")

asyncio.run(main())