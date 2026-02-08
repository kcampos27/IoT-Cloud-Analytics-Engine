import psutil, time
from psutil._common import bytes2human
def cpu_ram():
    while True:
        cpu = psutil.cpu_percent(interval=15, percpu=True)
        media_cpu= sum(cpu)/len(cpu)
        ram = getattr(psutil.virtual_memory(), 'percent')
        print("CPU: %" + str(media_cpu) + "\t RAM: %" + str(ram))
        time.sleep(5)

if __name__ == '__main__':
    cpu_ram()