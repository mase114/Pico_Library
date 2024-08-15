# servo.py

## servo.pyとはなに？

サーボモーター用のライブラリであり、PWMを用いたサーボモーターの角度と速度の制御が可能になります。

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

`servo_pins`サーボモーターを制御するためのPWMピンのリストを受け取ります。

### 役割

`self.servo_pins`インスタンス変数として受け取ったサーボピンのリストを保持します。

`self.angles`サーボごとの現在の角度を保持するリストを、すべて0で初期化します。

```python
def servo_pin(self,index):
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

`pin.freq(50)`サーボモーターの周波数を50Hzに設定します。

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

この関数はサーボモーターのピン情報などを表示するためのものです。将来的にデバッグなどで役立つ関数になります。

## main.pyでの記述







