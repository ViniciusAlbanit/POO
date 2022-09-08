class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0
    
    def __repr__(self):
        return f'Canal: {self.canal} | Volume: {self.volume}'

    def aumentar_volume(self):
       self.volume += 1
    
    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal
                        
tv = Televisao()
tv.alterar_canal(6)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()

print(f'A tv está no canal {tv.canal}')    # A tv está no canal 6
print(f'A tv está no volume {tv.volume}')  # A tv está no volume 2         

