from machine import Pin, PWM
import utime

class Servo:
    def __init__(self,servo_pins):
        self.servo_pins = servo_pins
        self.angles = [0] * len(servo_pins)  # 各サーボの角度を保持するリスト

    # サーボ番号
    def servo_num(self,index):
        return self.servo_pins[index]
    
    # 角度取得
    def get_angle(self,index):
        return self.angles[index]
    
    # 初期位置
    def set_init(self,pin,angle_init):
        pin.freq(50)
        pin.duty_u16(int((angle_init * 9.5 / 180 + 2.5) * 65535 / 100))
        index = self.servo_pins.index(pin)
        self.angles[index] = angle_init  # 初期角度をリストに保存
    
    # サーボを動かす
    def set_angle(self,pins,angles,speed):
        if isinstance(pins,(list,tuple)):
            # 最大ステップ数を計算
            steps = max(abs(self.get_angle(self.servo_pins.index(pin)) - angle) for pin, angle in zip(pins,angles))
            
            for step in range(steps + 1):
                for pin, target_angle in zip(pins,angles):
                    index = self.servo_pins.index(pin)
                    current_angle = self.get_angle(index)
                    direction = 1 if target_angle > current_angle else -1
                    # 1ステップだけ動かす
                    if current_angle != target_angle:
                        new_angle = current_angle + direction
                        pin.duty_u16(int((new_angle * 9.5 / 180 + 2.5) * 65535 / 100))
                        self.angles[index] = new_angle
                utime.sleep_ms(speed)
        else:
            index = self.servo_pins.index(pins)  # ピンのインデックスを取得
            if self.get_angle(index) - angles < 0:
                direction = 1
            else:
                direction = -1
            for angle_i in range(self.get_angle(index),angles + direction,direction):
                pins.duty_u16(int((angle_i * 9.5 / 180 + 2.5) * 65535 / 100))
                utime.sleep_ms(speed)
            self.angles[index] = angles  # 角度をリストに保存

    def show(self):
        pass
