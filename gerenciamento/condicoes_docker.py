import subprocess

def start_service(service_name):
    subprocess.run(['sudo', 'systemctl', 'start', service_name])
        

def stop_service(service_name):
    subprocess.run(['sudo', 'systemctl', 'stop', service_name])

def restart_service(service_name):
    subprocess.run(['sudo', 'systemctl', 'restart', service_name])

def start_system(service_name):
    condicao = input()
    if condicao == "start":
        start_service(service_name)
    elif condicao == "stop":
        stop_service(service_name)
    elif condicao == "restart":
        restart_service(service_name)
    else:
        print("Essa condição não existe no sistema")

start_system("nginx")  
