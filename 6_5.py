class Stationary:
    def __init__(self):
        self.title = 'title'
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationary):
    def draw(self):
        print('Буквы для письма я пишу сама')
class Pencil(Stationary):
    def draw(self):
        print('Рисую и живопишУ, Ваш портрет я напишу')
class Handle(Stationary):
    def draw(self):
        print('Маркеры - вот инструмент для того, кто превосходит себя самого')

calamus_scriptorius = Stationary()
bic = Pen()
koh_i_noor = Pencil()
stabilo = Handle()
for st_ry in [calamus_scriptorius, bic, koh_i_noor, stabilo]:
    st_ry.draw()
    print('* '*15)