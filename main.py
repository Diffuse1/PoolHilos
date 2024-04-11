import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
print('---------------------------------------------------------')
print('Dos hilos')
#---------------------------------------------------------------------------
global_arrayNum =[]
def contador2(inicio,fin):
    logging.info(f'Funciones con rango: {inicio} - {fin}')
    for i in range(inicio,fin+1):
        global_arrayNum.append( i )
        time.sleep(0.01)
    return 0
t0 = time.time()
lista_hilos=[]
t = threading.Thread(target=contador2, args=(1,50))
lista_hilos.append(t)
t.start()
t = threading.Thread(target=contador2, args=(51,100))
lista_hilos.append(t)
t.start()

for i in lista_hilos:
    t.join()
tf = time.time()-t0
global_arrayNum.sort()
print(f'Tiempo de ejecución: {tf}')
print(global_arrayNum)
print('------------------------------------------------------------------')
print('Pool de Hilos')
def printHW():
    logging.info(f'Funcion HW')
    print('Hola mundo :)')


global_arrayNum =[]
with ThreadPoolExecutor( max_workers=2) as executor:
    for i in range(1,201,50):
        executor.submit(contador2,i,i + 49 if i + 49 <=200 else 200)
tf = time.time()-t0
global_arrayNum.sort()
print(f'Tiempo de ejecución: {tf}')
print(global_arrayNum)