class TrafficLight:
    import time
    __color = ('red', 'yellow', 'green')
    def running(self,i):
            if self.__color[0] != 'red' or self.__color[1] != 'yellow' or self.__color[2] != 'green':
                print('Некорректная последовательность цветов, работа не будет продолжена!')
            else:
                self.i = i
                for i in range(0,i):
                    print(f"\033[31m{self.__color[0]}")
                    self.time.sleep(7)
                    print(f"\033[33m{self.__color[1]}")
                    self.time.sleep(2)
                    print(f"\033[32m{self.__color[2]}")
                    self.time.sleep(8)
                    i += 1
                print(f"\033[4m\033[37m\033[44mend\033[0m")

tl = TrafficLight()
tl.running(int(input('Введите количество циклов светофора: ')))