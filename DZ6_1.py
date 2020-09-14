import time


class TrafficLight:
    __color = ""

    def running(self):
        while True:
            __color = "red"
            print(__color)
            time.sleep(7)
            __color = "yellow"
            print(__color)
            time.sleep(2)
            __color = "green"
            print(__color)
            time.sleep(7)
            __color = "yellow"
            print(__color)
            time.sleep(2)


a = TrafficLight()
a.running()
