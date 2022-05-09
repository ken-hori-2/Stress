import matplotlib.pyplot as plt ### fig:class_world1

class World:         
    def __init__(self):
        self.objects = []             # ここにロボットなどのオブジェクトを登録
        
    def append(self,obj):             # オブジェクトを登録するための関数
        self.objects.append(obj)
    
    def draw(self):
        fig = plt.figure(figsize=(8,8))                # 8x8 inchの図を準備
        ax = fig.add_subplot(111)                      # サブプロットを準備
        ax.set_aspect('equal')                         # 縦横比を座標の値と一致させる
        ax.set_ylim(-5,5)                              # Y軸も同様に
        ax.set_xlabel("X",fontsize=20)                 # X軸にラベルを表示
        ax.set_ylabel("Y",fontsize=20)                 # 同じくY軸に
        
        for obj in self.objects: obj.draw(ax)           # appendした物体を次々に描画
            
        plt.show()
        
world = World()     ### fig:class_world3
world.draw()