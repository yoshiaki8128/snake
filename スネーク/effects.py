# pygameを読み込む
import pygame
# randomライブラリのrandint,choice関数を読み込む
from random import randint, choice

class Effect:
  """
  Effectクラス
  """
  # 破片の大きさ
  RANGE = 30
  # 破片の数
  NUMBER = 15

  # 色
  color = 255
  list_effects = []
  directions = []
  sizes = []

  def __init__(self, surf):
    """
    初期化関数
    """
    # Surfaceクラスのインスタンス
    self.surf = surf

  def run(self, trigger, x, y):
    # effectトリガーがTrueなら以下を実行
    if trigger:
      self.color = 255

      # effectの破片それぞれの座標をランダムで設定してリストに入れる
      self.list_effects = [(randint(x - self.RANGE + 12, x + self.RANGE + 12),
      randint(y - self.RANGE + 12, y + self.RANGE - 12))
      for i in range(self.NUMBER)]
      # 破片の速度ベクトルをランダムに設定。リストで管理
      self.directions = [(randint(-1, 1), randint(-1, 1)) for i in range(self.NUMBER)]
      # 破片の大きさをランダムで設定。リストで管理
      self.sizes = [(randint(1, 7), randint(1, 7)) for i in range(self.NUMBER)]

    # 破片を描画
    for i, xy in enumerate(self.list_effects):
      pygame.draw.rect(self.surf, (max(self.color, 120), 0, 0), (*xy, *self.sizes[i]))

    # 速度ベクトルの方向へ破片を動かす
    self.list_effects = [(xy[0] - d[0], xy[1] - d[1]) for xy, d in zip(self.list_effects, self.directions)]

    # 破片を黒にして見えなくする
    self.color -= 3
