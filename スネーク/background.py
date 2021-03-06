# pygameを読み込む
import pygame
# randomライブラリのrandint, randrange関数を読み込む
from random import randint, randrange

class BG:
  """
  BGクラス
  """
  def __init__(self, surface):
    """
    初期化関数
    """
    # Surfaceクラスのインスタンス
    self.surf = surface
    # 背景の四角形
    self.max_obj = 500
    # 画面の横幅
    self.width = surface.get_width()
    # 画面の縦幅
    self.height = surface.get_height()
    # 四角形のx座標の位置をランダムに設定。リストで管理
    self.x = [randrange(-self.width, 2 * self.width) for i in range(self.max_obj)]
    # 四角形のy座標の位置をランダムに設定。リストで管理
    self.y = [randrange(-self.height, 2 * self.height) for i in range(self.max_obj)]
    # 四角形の大きさ
    self.side = [randint(2, 5) for i in range(self.max_obj)]
    # 移動スピード
    self.speed = [randint(1, 4) for i in range(self.max_obj)]
    # 色をランダムに設定
    self.color = [(randrange(255), randrange(255), randrange(255)) for i in range(self.max_obj)]

  def draw(self, direction):
    """
    背景を描画
    """

    # snakeの移動方向と逆方向に背景の四角形も動かす。スピードのスカラ値（スピードの大きさ）を移動方向に足す・引いて動かす
    if direction == "l":
      self.x = [x + r for x, r in zip(self.x, self.speed)]
    elif direction == "r":
      self.x = [x - r for x, r in zip(self.x, self.speed)]
    elif direction == "u":
      self.y = [y + r for y, r in zip(self.y, self.speed)]
    elif direction == "d":
      self.y = [y - r for y, r in zip(self.y, self.speed)]

    # 四角形を描画。四角形の20%は色を描画の都度変える（チカチカさせる処理）
    [pygame.draw.rect(self.surf, self.color[i], (self.x[i], self.y[i], self.side[i], self.side[i])) if i % 5 else pygame.draw.rect(self.surf, (randrange(255), randrange(255), randrange(255)),(self.x[i], self.y[i], self.side[i], self.side[i])) for i in range(self.max_obj)]
