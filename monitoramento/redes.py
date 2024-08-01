import psutil
import time

def monitor_network():
    print("O monitoramento da rede ira iniciar \nCaso deseje parar aperte Ctrl + c")
    print("...")
    time.sleep(3)
    try:
        while True:
            net_io = psutil.net_io_counters()
            print(f"Bytes Recebidos: {net_io.bytes_recv}")
            print(f"Bytes Enviados: {net_io.bytes_sent}")
            time.sleep(3)
    except KeyboardInterrupt:
        print("...")
        print("\nInterrupção recebida. Encerrando o monitoramento...")


if __name__ == "__main__":
    monitor_network()

