#
# 矩形を検出.
#

##################################################
# import
##################################################
import sensor
import image
import lcd

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(True)

##################################################
# main
##################################################
while(True):
    # カメラ画像を取得
    img = sensor.snapshot()
    # 矩形を検出
    res = img.find_rects()
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            print(i)
            # 矩形を描画
            img.draw_rectangle(i.x(), i.y(), i.w(), i.h(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)
