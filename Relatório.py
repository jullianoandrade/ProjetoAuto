import pyautogui
import time

# Coleta de dados
data = input('Olá! Poderia me dizer a data de hoje? ')
CódCliente = input('Qual seria o código do cliente que você quer tirar relatório? ')

# Acessa o Zeta
pyautogui.click(x=892, y=1057)

# Relatórios
pyautogui.click(x=283, y=47)

# Vendas
pyautogui.click(x=308, y=85)

# Geral
pyautogui.click(x=499, y=76)
time.sleep(0.5)

# Esquemas
pyautogui.click(x=638, y=307)

# Equipamentos locados
pyautogui.click(x=593, y=355)
time.sleep(0.5)

# Data final
pyautogui.click(x=1048, y=417)
pyautogui.click(x=1048, y=417)
pyautogui.press("backspace")
pyautogui.write(data)

# Filtros
pyautogui.click(x=585, y=251)

# Desmarcar filiais
pyautogui.click(x=600, y=469)
pyautogui.click(x=907, y=475)
pyautogui.click(x=918, y=497)
pyautogui.click(x=904, y=592)
pyautogui.click(x=1094, y=659)

# Ajustar situação do item
pyautogui.click(x=683, y=830)
pyautogui.click(x=1068, y=627)
pyautogui.click(x=920, y=626)
pyautogui.click(x=1027, y=654)

# Filtrar entidades
pyautogui.click(x=660, y=249)
pyautogui.click(x=800, y=304)
pyautogui.write(CódCliente)
pyautogui.press("tab")

# Imprimir
pyautogui.click(x=1243, y=871)