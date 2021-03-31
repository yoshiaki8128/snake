# pygameを読み込む
import pygame

class Snake:
  """
  Snakeクラス
  """

  # snakeの色
  COLOR = [0, 170, 0]
  # snakeの長辺の長さ
  SIDE = 15
  # snakeの長さ
  lenght = 2
  # snakeの移動速度（velocity）
  vel = 10

  def __init__(self, surface):
    """
    初期化関数
    """
    # Surfaceクラスのインスタンス
    self.surface = surface
    # 画面の横幅の整数値（//は割った商の整数）
    self.x = surface.get_width() // 2
    # 画面の縦幅の整数値（//は割った商の整数）
    self.y = surface.get_height() // 4
    # 画面の縦横のタプルをリストに入れる
    self.XY = [(self.x, self.y)]
    # 移動方向、l=左、r=右、d=下、u=上
    self.direction = "d"

  def add_lenght(self):
    """
    snakeを長くする
    """
    # 1長くする
    self.lenght += 1
    # 長辺の長さを1長くする
    self.SIDE += 1
    # RGBのGを濃くする
    self.COLOR[1] += 1
    # RGBのGの最大値は255、min関数は2つのうちに小さい方を選ぶ
    self.COLOR[1] = min(self.COLOR[1], 255)

  def get_snake(self):
    """
    snakeを描画
    """
    self.XY += [(self.x, self.y)]
    self.XY = self.XY[-self.lenght:]
    # snakeの体をブロックごとに描画
    for kx, ky in self.XY:
      pygame.draw.rect(self.surface, self.COLOR, (kx, ky , self.SIDE, self.SIDE))

  def move_snake(self, key):
    """
    snakeをキー操作
    """

    # 左へ操作
    if key == "l":
      # 左方向へ速度を加算
      self.x -= self.vel
      self.get_snake()
    # 右へ操作
    if key == "r":
      # 右方向へ速度を加算
      self.x += self.vel
      self.get_snake()
    # 下へ操作
    if key == "u":
      # 下方向へ速度を加算
      self.y -= self.vel
      self.get_snake()
    # 上へ操作
    if key == "d":
      # 上方向へ速度を加算
      self.y += self.vel
      self.get_snake()
