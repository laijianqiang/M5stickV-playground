#
# ヒストグラム平坦化.
#

##################################################
# import
##################################################
import lcd
import sensor

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # ヒストグラム平坦化
    img.histeq(adaptive = True, clip_limit = 3)
    # 画像をLCDに描画
    lcd.display(img)
