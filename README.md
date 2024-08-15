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
