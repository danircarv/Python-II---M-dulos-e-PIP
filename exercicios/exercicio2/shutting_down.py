import os

# 1 - Desligar o computador
# os.system("shutdown /s") # Desliga o computador em 60s
# os.system("shutdown /s /t 0") # Desliga o computador imediatamente

# 2 - Cancelar o desligamento
# os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")
    
def turn_off_half_hour():
    os.system("shutdown /s /t 1800")
    
def cancel_shutdown():
    os.system("shutdown /a")
    
turn_off_one_hour()
cancel_shutdown()
zap()
