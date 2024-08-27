# servo.py

## servo.pyとはなに？

サーボモーター用のライブラリであり、`PWM`を用いたサーボモーターの角度と速度の制御が可能になります。

## 最初なにから始める？

`servo.py`を利用するには、`main.py`に`import`する必要があリます。

使用するマイコンは`raspberry pi pico`を使用します。

pico上に`main.py`と`servo.py`を保存します。

```python
from servo import Servo
```

## 関数の説明

```python
def __init__(self,servo_pins):
```

これはクラスのコンストラクタです。`Servo`クラスのインスタンスが作成されたときに自動的に呼び出されます。

### 引数

`servo_pins`サーボモーターを制御するための`PWM`ピンのリストを受け取ります。

### 役割

`self.servo_pins`インスタンス変数として受け取ったサーボピンのリストを保持します。

`self.angles`サーボごとの現在の角度を保持するリストを、すべて`0`で初期化します。

```python
def servo_num(self,index):
```

指定されたインデックスのサーボピンを返す関数です。

### 引数

`index`取得したいサーボピンのインデックスを指定します。

### 役割

`self.servo_pins[index]`指定されたインデックスに対応するサーボピンを返します。

```python
def get_angle(self,index):
```

指定されたインデックスのサーボの角度を返す関数です。

### 引数

`index`取得したいサーボの角度に対応するインデックスを指定します

### 役割

`self.angles[index]`指定されたインデックスに対応するサーボの現在の角度を返します。

```python
def set_init(self,pin,angle_init):
```

サーボモーターを初期角度に設定する関数です。

### 引数

`pin`初期角度を設定するサーボモーターのピン。

`angle_init`サーボモーターの初期角度を指定します。

### 役割

`pin.freq(50)`サーボモーターの周波数を`50`Hzに設定します。

`pin.duty_u16(int((angle_init * 9.5 / 180 + 2.5) * 65535 / 100))`指定された角度に基づいてサーボを制御するデューティサイクルを設定します。

`self.servo_pins.index(pin)`対応するピンのインデックスを取得します。

`self.angles[index] = angle_init`初期角度を保持するリストに保存します。

```python
def set_angle(self,pins,angles,speed):
```

サーボモーターを指定した角度にゆっくり動かすための関数です。1つのサーボモーターだけでなく、複数のサーボを同時に動かすこともできます。

### 引数

`pins`動かすサーボモーターのピンまたはピンのリスト。

`angles`目標角度、または複数のピンに対する角度のリスト。

`speed`サーボを動かすスピード（動作間の待機時間をミリ秒単位で指定）。

### 役割

`steps`現在の角度から目標角度までの最大ステップ数を計算します。

`for step in range(steps + 1)`各ステップごとにサーボを少しずつ動かします。

`pin.duty_u16(int((new_angle * 9.5 / 180 + 2.5) * 65535 / 100))`角度に基づいてサーボを動かすためのデューティサイクルを設定します。

`self.angles[index] = new_angle`サーボの角度を更新し、保持します。

```python
def show(self):
```

この関数はサーボモーターのピン情報や角度などを出力するためのものです。将来的にデバッグなどで役立つ関数になります。

## main.pyでの記述

### servo.pyをインポート

[最初なにから始めるを参照](https://github.com/mase114/Pico_Library?tab=readme-ov-file#最初なにから始める)

### サーボピンの設定

```python
#サーボの数に応じてpin設定を変える
servo_pwm_pin = [
    PWM(Pin(n)),
    PWM(Pin(n))
]
```

`servo_pwm_pin`リストは、各サーボに対応する`PWM`ピンのリストを作成します。

### Servoクラスのインスタンス作成

```python
servo = Servo(servo_pwm_pin)
```

`Servo`クラスのインスタンスを作成し、先ほど設定したサーボピンのリスト`servo_pwm_pin`を渡しています。これにより、`servo`オブジェクトは、複数のサーボモーターを管理・制御することが可能になります。

### サーボの初期位置設定

```python
servo.set_init(servo.servo_num(n), angle_init)
utime.sleep_ms(1000)
```

`set_init`メソッドを使って、各サーボの初期角度を設定しています。

`servo.servo_num(n)`は、リスト`servo_pwm_pin`の最初のピン`PWM(Pin(n))`に対応します。このサーボの初期角度を`angle_init`で設定します。

`utime.sleep_ms(1000)`で`1`秒（`1000`ミリ秒）間待機し、サーボモーターが初期位置に移動する時間を確保します。

### サーボの動作設定

```python
servo.set_angle(servo.servo_num(n),angles,speed)
servo.set_angle([servo.servo_num(n),servo.servo_num(n)],[angles,angles],speed)
```

`1`つのサーボ`servo_num(n)`の角度を`angles`で設定します。`speed`でミリ秒ごとにサーボを少しずつ動かして目標角度に到達さる時間を設定。

`2`つのサーボ`servo_num(n),servo_num(n)`を同時に動かします。それぞれの`angles`で角度を設定します。これも`speed`で速度をミリ秒ごとに設定します。

### ピン情報や角度の出力

```python
#未実装の為、仮とする
servo.show()
```

将来的にサーボごとの角度を出力することができるようにする。

## サンプルmain.pyコード

```python
from machine import Pin, PWM
import utime
# servo.pyをimport
from servo import Servo

# サーボピンの設定
servo_pwm_pin = [
    PWM(Pin(0)),
    PWM(Pin(1))
]

# Servoクラスのインスタンス作成
servo = Servo(servo_pwm_pin)

# サーボの初期位置設定
servo.set_init(servo.servo_num(0), 60)
servo.set_init(servo.servo_num(1), 140)
utime.sleep_ms(1000)

# サーボを同時に動かす
servo.set_angle(servo.servo_num(0), 30, 20)
servo.set_angle([servo.servo_num(0),servo.servo_num(1)], [60,120], 20)
```
