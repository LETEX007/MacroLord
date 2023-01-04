from ppadb.client import Client as AdbClient
import numpy as np
import pyautogui as py
#from pytesseract import *
import io
import os
import cv2
import PIL.Image as Image
from PIL import ImageOps
import keyboard
import time
import random
import pytesseract #C:\Program Files\Tesseract-OCR\tesseract.exe
import sys
import threading
import sqlite3
from sqlite3 import Error
import ctypes
import subprocess
from datetime import datetime
import requests

def license():
    # The list with all keys.
    keys = requests.get("https://raw.githubusercontent.com/LETEX007/MacroLord/main/licence.txt").text
    # keys = ["key1", "key2", "key3"]

    # License key from user.
    keyfromuser = "F8C588F4C1C8D"

    for key in keys.splitlines():
        if key == keyfromuser:
            # Code when key match.
            return

    # Code if the key don't match.
    exit()
license()

#adbstart = subprocess.Popen([r'C:\Users\Rodrigo\Documents\platform-tools_r33.0.2-windows\platform-tools\adb.exe', 'start-server'])
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#elbueno#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#ruta donde se encuentre su tresseract

if getattr(sys, 'frozen', False):
    _path = os.path.join(sys._MEIPASS, './Tesseract-OCR/tesseract.exe')
    #print(_path)
    pytesseract.pytesseract.tesseract_cmd =_path
     #the .exe will look here
else:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #ruta donde se encuentre su tresseract

#Mapeo 0-9
c1 = 843,183
c2 = 932,183
c3 = 1020,183
c4 = 843,248
c5 = 932,248
c6 = 1020,248
c7 = 843,311
c8 = 932,313
c9 = 1020,313
c0 = 865,377
# mapeo 2 tp
c2_1=865,295
c2_2=955,296
c2_3=1043,294
c2_4=865,360
c2_5=955,363
c2_6=1043,361
c2_7=865,427
c2_8=955,426
c2_9=1043,425
c2_0=890,489
#resetdeadb con cmd py
f = open(r"C:\ProgramData\BlueStacks_nxt\bluestacks.conf", "r")
data = f.read()
cropline = data[data.find("status.adb_port")+17:]
croplineindex = cropline.find('"')
puerto = data[data.find("status.adb_port")+17:data.find("status.adb_port")+17+croplineindex]
client = AdbClient(host="127.0.0.1", port=5037)
##HACER DINAMICO CONEXION EL ADB Y COMPILAR DENUEVO CON TESERACT Y FOTOS
##HACER DINAMICO CONEXION EL ADB Y COMPILAR DENUEVO CON TESERACT Y FOTOS
##HACER DINAMICO CONEXION EL ADB Y COMPILAR DENUEVO CON TESERACT Y FOTOs
ip = "127.0.0.1:"+str(puerto)
adbstart = subprocess.Popen([r'C:\Users\Rodrigo\Documents\platform-tools_r33.0.2-windows\platform-tools\adb.exe', 'connect',ip])

while True:
    try:
        devices = client.devices()
        if len(devices) == 1:
            device = devices[0]
            print("BOT 1 ACTIVADO")
            break
        print("Buscando Emulador...")
        time.sleep(2)
    except:
        print("Buscando Conexion del Servicio ADB...")
        time.sleep(2)
        continue
#result = device.screencap()
##print(type(result))
# guardar screenshot to pil
#image = Image.open(io.BytesIO(result))
#image.save(savepath)
## guardar screenshot nativo
#with open("screen.png", "wb") as fp:
  #  fp.write(result) 
##print(type(image))
# foto original region=(506,40, 74, 21)
##print(bazinga)
#SQLITE
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
database = r"C:\sqlite\db\pythonsqlite.db"

sql_create_rss_table = """ CREATE TABLE IF NOT EXISTS rssinfo (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    fecha text,
                                    comida real NOT NULL,
                                    piedra real NOT NULL,
                                    madera real NOT NULL,
                                    mineral real NOT NULL,
                                    oro real NOT NULL
                                ); """
sql_create_totales_table = """CREATE TABLE IF NOT EXISTS rsstotal (
                                    id integer PRIMARY KEY,
                                    username text NOT NULL,
                                    comida real NOT NULL,
                                    piedra real NOT NULL,
                                    madera real NOT NULL,
                                    mineral real NOT NULL,
                                    oro real NOT NULL
                                );"""
sql_create_errorlog_table = """CREATE TABLE IF NOT EXISTS logserror (
                                    id integer PRIMARY KEY,
                                    mensaje text,
                                    error text,
                                    tipoerror text
                                );"""

# create a database connection
conn = create_connection(database)

# create tables
if conn is not None:
    # create rss table
    create_table(conn, sql_create_rss_table)
    create_table(conn, sql_create_totales_table)
    create_table(conn, sql_create_errorlog_table)
else:
    print("Error! cannot create the database connection.")


def create_project(conn, project):
    """
    Create a new project into the rssinfo table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO rssinfo(name,fecha,comida,piedra,madera,mineral,oro)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
def create_tryexp(conn, project):
    """
    Create a new project into the logserror table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO logserror(mensaje,error,tipoerror)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
def create_total(conn, project):
    """
    Create a new project into the rsstotal table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' REPLACE INTO rsstotal(id,username,comida,piedra,madera,mineral,oro)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id,cast(SUM(comida) as integer),cast(SUM(piedra) as integer),cast(SUM(madera) as integer),cast(SUM(mineral) as integer),cast(SUM(oro) as integer) FROM rssinfo WHERE name=?", (priority,))

    row = cur.fetchone()
    return row
def select_task_by_totaluser(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id,comida,piedra,madera,mineral,oro FROM rsstotal WHERE username=?", (priority,))

    row = cur.fetchone()
    return row


def enviarRecursos(tipo,cantidad,usernameUI):
    time.sleep(0.4)
    #Capacidad Suministro
    recursos = screenshot()
    suministroimg = recursos.crop((950,460,107+950,26+460))
    #suministroimg = py.screenshot('capacidad.png',region=(950,460,107,26))
    resize = tuple(8*x for x in suministroimg.size)
    suministroimg = suministroimg.resize(resize, Image.Resampling.LANCZOS)
    outputsuministro = pytesseract.image_to_string(suministroimg,config='--psm 7')
    capacidad = str(outputsuministro.replace(',', ''))
    #Bono Fiscal
    bonifiscal = recursos.crop((858,331,258+858,26+331))
    #bonifiscal = py.screenshot('bonifiscal.png',region=(858,331,258,26))
    resize = tuple(8*x for x in bonifiscal.size)
    bonifiscal = bonifiscal.resize(resize, Image.Resampling.LANCZOS)
    outputbonifiscal = pytesseract.image_to_string(bonifiscal,config='--psm 7')
    bonofiscal = str(outputbonifiscal[-7:].replace('%', '')).strip()
    bonofiscal = str(bonofiscal.replace(':', ''))
   
    capacidad_enviada = str(capacidad)
    #j 1 ya que se envio 1 antes y no parte en 0
    j = 1
    total=int(capacidad_enviada)
    output = cantidad*1000000

    resto = str(int(output%int(capacidad_enviada) + int(capacidad_enviada)*(float(str(bonofiscal))+2)/100))
    # referencia carretas a enviar
    cociente = output//int(capacidad_enviada)

    for i in range(0,cociente+1):
        ejercitomax = screenshot()
        limiteimg = py.locate(resource_path('limite-confirmar.png'),ejercitomax,region=(449,340,381,83),grayscale=True,confidence=0.8)
        if limiteimg != None:
            while True:
                time.sleep(np.random.uniform(0.6, 0.8))
                device.shell(f'input tap 635 381')
                time.sleep(np.random.uniform(0.6,0.8))
                device.shell(f'input tap 741 344')
                time.sleep(1.5)
                device.shell(f'input tap 1008 123')
                time.sleep(np.random.uniform(0.6,0.8))
                device.shell(f'input tap 367 329')
                limiteimg2 = py.locate(resource_path('limite-confirmar.png'),screenshot(),region=(449,340,381,83),grayscale=True,confidence=0.8)
                if limiteimg2 == None:
                    
                    break
                time.sleep(8)
        if i == cociente: 
            time.sleep(np.random.uniform(0.6, 0.8))
            time.sleep(0.8)
            if tipo == 'comida':
                device.shell(f'input tap 660 260')
            if tipo == 'piedra':
                device.shell(f'input tap 660 354')
            if tipo == 'madera':
                device.shell(f'input tap 660 452')
            if tipo == 'mineral':
                device.shell(f'input tap 660 546')
            if tipo == 'oro':
                device.shell(f'input tap 660 643')
            time.sleep(np.random.uniform(0.6,0.8))
            for i in range(0,len(resto)):
                if resto[i] == '0':
                    time.sleep(0.3)
                    device.shell(f'input tap {c0[0]} {c0[1]}')
                    time.sleep(0.3)
                elif resto[i] == '1':
                    device.shell(f'input tap {c1[0]} {c1[1]}')
                    time.sleep(0.3)
                elif resto[i] == '2':
                    device.shell(f'input tap {c2[0]} {c2[1]}')
                    time.sleep(0.3)
                elif resto[i] == '3':
                    device.shell(f'input tap {c3[0]} {c3[1]}')
                    time.sleep(0.3)
                elif resto[i] == '4':
                    device.shell(f'input tap {c4[0]} {c4[1]}')
                    time.sleep(0.3)
                elif resto[i] == '5':
                    device.shell(f'input tap {c5[0]} {c5[1]}')
                    time.sleep(0.3)
                elif resto[i] == '6':
                    device.shell(f'input tap {c6[0]} {c6[1]}')
                    time.sleep(0.3)
                elif resto[i] == '7':
                    device.shell(f'input tap {c7[0]} {c7[1]}')
                    time.sleep(0.3)
                elif resto[i] == '8':
                    device.shell(f'input tap {c8[0]} {c8[1]}')
                    time.sleep(0.3)
                elif resto[i] == '9':
                    device.shell(f'input tap {c9[0]} {c9[1]}')
                    time.sleep(0.3)
            # Seguimiento de ruta a castillo
            time.sleep(np.random.uniform(0.5, 0.6))
            # ok verde
            device.shell(f'input tap 998 372')
            time.sleep(np.random.uniform(0.8,1))#suministrar
            device.shell(f'input tap 994 660')
            time.sleep(np.random.uniform(0.8,1))#confirmar
            device.shell(f'input tap 740 340')
            time.sleep(0.1)
            device.shell(f'input tap 740 380')
            
            time.sleep(1)
            device.shell(f'input tap 1236 42')
            time.sleep(1)
            device.shell(f'input tap 1236 42')
            break
        else:
            if tipo == 'comida':
                device.shell(f'input tap 660 305')
            if tipo == 'piedra':
                device.shell(f'input tap 649 402')
            if tipo == 'madera':
                device.shell(f'input tap 660 499')
            if tipo == 'mineral':
                device.shell(f'input tap 660 595')
            if tipo == 'oro':
                device.shell(f'input tap 660 692')
            time.sleep(np.random.uniform(0.1, 0.3))
            

        # Seguimiento de ruta a castillo
        device.shell(f'input tap 998 372')
        time.sleep(np.random.uniform(0.8,1))#suministrar
        device.shell(f'input tap 994 660')
        time.sleep(np.random.uniform(0.8,1))#confirmar
        device.shell(f'input tap 740 340')
        time.sleep(0.1)
        device.shell(f'input tap 740 380')
        time.sleep(1.5)
        device.shell(f'input tap 1008 123')
        time.sleep(np.random.uniform(0.5,0.8))
        device.shell(f'input tap 659 329')
        total+=int(capacidad_enviada)
        j+=1
        time.sleep(np.random.uniform(1, 1.5))
    descontarRSS(tipo,cantidad*1000000,usernameUI)
def update_comida(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE rsstotal
              SET comida = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
def update_piedra(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE rsstotal
              SET piedra = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
def update_madera(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE rsstotal
              SET madera = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    #print("ACTUALIZADO")
def update_mineral(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE rsstotal
              SET mineral = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
def update_oro(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE rsstotal
              SET oro = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
def descontarRSS(tipo,cantidad, username):
    conn = create_connection(database)
    with conn:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        id = select_task_by_priority(conn, username)
        #print("id",id)
        if tipo == "comida":
            updatetipo = id[1]
            update = (updatetipo-cantidad, id[0])
            rssinfo = (username,dt_string,-cantidad,0,0,0,0)
            rssinfodb = create_project(conn, rssinfo)
            update_comida(conn, update)
        elif tipo == "piedra":
            updatetipo = id[2]
            update = (updatetipo-cantidad, id[0])
            rssinfo = (username,dt_string,0,-cantidad,0,0,0)
            rssinfodb = create_project(conn, rssinfo)
            update_piedra(conn, update)
        elif tipo == "madera":
            updatetipo = id[3]
            #print(cantidad)
            #print(updatetipo)
            #print(updatetipo-cantidad)
            update = (updatetipo-cantidad, id[0])
            rssinfo = (username,dt_string,0,0,-cantidad,0,0)
            rssinfodb = create_project(conn, rssinfo)
            update_madera(conn, update)
        elif tipo == "mineral":
            updatetipo = id[4]
            update = (updatetipo-cantidad, id[0])
            rssinfo = (username,dt_string,0,0,0,-cantidad,0)
            rssinfodb = create_project(conn, rssinfo)
            update_mineral(conn, update)
        elif tipo == "oro":
            updatetipo = id[5]
            update = (updatetipo-cantidad, id[0])
            rssinfo = (username,dt_string,0,0,0,0,-cantidad)
            rssinfodb = create_project(conn, rssinfo)
            update_oro(conn, update)

def screenshot():
    result = device.screencap()
    image = Image.open(io.BytesIO(result))
    return image

def cmd_madera(screen):
    screen = screen
    imgstone1 = py.locate(resource_path('madera.png'),screen,region=(436,36,198,28),grayscale=True,confidence=0.8)
    if imgstone1 != None:
        imgtxt = screen.crop((imgstone1[0]+82,imgstone1[1],34+imgstone1[0]+83,18+imgstone1[1]))
        #hola = imgtxt.save("cropmadera.png")
        #imgtxt = py.screenshot('cantidad-madera.png',region=(imgstone1[0]+82,imgstone1[1],34,19))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgstone1[0]} {imgstone1[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                sumarsspermiso = select_task_by_priority(conn, output1[index:].rstrip())
            resize = tuple(4*x for x in imgtxt.size)
            imgtxtresized = imgtxt.resize(resize, Image.Resampling.LANCZOS)
            output = pytesseract.image_to_string(imgtxtresized,config='--psm 7 --oem 3')
            #una carreta
            outputstr = str(output.replace('.', ''))
            output = int(output.rstrip())
            outputint = output
            if len(outputstr.rstrip())<= 3:
                outputint = output*1000000
            #print(outputint)
            #print(sumarsspermiso)
            #print(output1[index:].rstrip())
            if sumarsspermiso[3] < outputint:
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 630 162')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 276 263') #asunto
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "Banco de recursos"') #asunto-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input keyevent 66') #enter
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 203 403') #cuerpo
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "No tienes recursos en el banco"') #cuerpo-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 635 110') #back
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 638 663')
                time.sleep(np.random.uniform(1,1.1))
                device.shell(f'input tap 1235 44')
                time.sleep(0.5)
                device.shell(f'input tap 1235 44')
                time.sleep(5)
            else:
                time.sleep(np.random.uniform(0.1, 0.2))
                #enviarRecursos(usuarioimg2,'stone',output,limite)
                device.shell(f'input tap 279 525')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 635 181')
                time.sleep(np.random.uniform(1, 1.2))
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.3, 0.5))
                device.shell(f'input tap 632 327')
                time.sleep(np.random.uniform(0.4,0.5))
                enviarRecursos('madera',output, output1[index:].rstrip())
                time.sleep(5)
        else:
            device.shell(f'input tap 1236 44')
            time.sleep(5)
            
def cmd_piedra(screen):
    screen = screen
    imgstone1 = py.locate(resource_path('piedra.png'),screen,region=(436,36,198,28),grayscale=True,confidence=0.8)
    if imgstone1 != None:
        imgtxt = screen.crop((imgstone1[0]+82,imgstone1[1],34+imgstone1[0]+83,19+imgstone1[1]))
        #hola = imgtxt.save("crop.png")
        #imgtxt = py.screenshot('cantidad-madera.png',region=(imgstone1[0]+82,imgstone1[1],34,19))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgstone1[0]} {imgstone1[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                sumarsspermiso = select_task_by_priority(conn, output1[index:].rstrip())
            resize = tuple(4*x for x in imgtxt.size)
            imgtxtresized = imgtxt.resize(resize, Image.Resampling.LANCZOS)
            output = pytesseract.image_to_string(imgtxtresized,config='--psm 7 --oem 3')
            #una carreta
            outputstr = str(output.replace('.', ''))
            output = int(output.rstrip())
            outputint = output
            if len(outputstr.rstrip())<= 3:
                outputint = output*1000000
            #print(output)
            #print(sumarsspermiso)
            #print(output1[index:].rstrip())
            if sumarsspermiso[2] < outputint:
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 630 162')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 276 263') #asunto
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "Banco de recursos"') #asunto-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input keyevent 66') #enter
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 203 403') #cuerpo
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "No tienes recursos en el banco"') #cuerpo-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 635 110') #back
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 638 663')
                time.sleep(np.random.uniform(1,1.1))
                device.shell(f'input tap 1235 44')
                time.sleep(0.5)
                device.shell(f'input tap 1235 44')
                time.sleep(5)
            else:
                time.sleep(np.random.uniform(0.1, 0.2))
                #enviarRecursos(usuarioimg2,'stone',output,limite)
                device.shell(f'input tap 279 525')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 635 181')
                time.sleep(np.random.uniform(1, 1.2))
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.3, 0.5))
                device.shell(f'input tap 632 327')
                time.sleep(np.random.uniform(0.4,0.5))
                enviarRecursos('piedra',output, output1[index:].rstrip())
                time.sleep(5)
        else:
            device.shell(f'input tap 1236 44')
            time.sleep(5)
			
def cmd_comida(screen):
    screen = screen
    imgstone1 = py.locate(resource_path('comida.png'),screen,region=(436,36,198,28),grayscale=True,confidence=0.8)
    if imgstone1 != None:
        imgtxt = screen.crop((imgstone1[0]+82,imgstone1[1],34+imgstone1[0]+83,19+imgstone1[1]))
        #hola = imgtxt.save("crop.png")
        #imgtxt = py.screenshot('cantidad-madera.png',region=(imgstone1[0]+82,imgstone1[1],34,19))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgstone1[0]} {imgstone1[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        #hola = rangosimg.save("QUERANGOS.png")
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                sumarsspermiso = select_task_by_priority(conn, output1[index:].rstrip())
            resize = tuple(4*x for x in imgtxt.size)
            imgtxtresized = imgtxt.resize(resize, Image.Resampling.LANCZOS)
            output = pytesseract.image_to_string(imgtxtresized,config='--psm 7 --oem 3')
            #una carreta
            outputstr = str(output.replace('.', ''))
            output = int(output.rstrip())
            outputint = output
            if len(outputstr.rstrip())<= 3:
                outputint = output*1000000
            #print(output)
            #print(sumarsspermiso)
            #print(output1[index:].rstrip())
            if sumarsspermiso[1] < outputint:
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 630 162')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 276 263') #asunto
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "Banco de recursos"') #asunto-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input keyevent 66') #enter
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 203 403') #cuerpo
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "No tienes recursos en el banco"') #cuerpo-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 635 110') #back
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 638 663')
                time.sleep(np.random.uniform(1,1.1))
                device.shell(f'input tap 1235 44')
                time.sleep(0.5)
                device.shell(f'input tap 1235 44')
                time.sleep(5)
            else:
                time.sleep(np.random.uniform(0.1, 0.2))
                #enviarRecursos(usuarioimg2,'stone',output,limite)
                device.shell(f'input tap 279 525')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 635 181')
                time.sleep(np.random.uniform(1, 1.2))
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.3, 0.5))
                device.shell(f'input tap 632 327')
                time.sleep(np.random.uniform(0.4,0.5))
                enviarRecursos('comida',output, output1[index:].rstrip())
                time.sleep(5)
        else:
            device.shell(f'input tap 1236 44')
            time.sleep(5)

def cmd_mineral(screen):
    screen = screen
    imgstone1 = py.locate(resource_path('mineral.png'),screen,region=(436,36,198,28),grayscale=True,confidence=0.8)
    if imgstone1 != None:
        imgtxt = screen.crop((imgstone1[0]+82,imgstone1[1],34+imgstone1[0]+83,19+imgstone1[1]))
        #hola = imgtxt.save("crop.png")
        #imgtxt = py.screenshot('cantidad-madera.png',region=(imgstone1[0]+82,imgstone1[1],34,19))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgstone1[0]} {imgstone1[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                sumarsspermiso = select_task_by_priority(conn, output1[index:].rstrip())
            resize = tuple(4*x for x in imgtxt.size)
            imgtxtresized = imgtxt.resize(resize, Image.Resampling.LANCZOS)
            output = pytesseract.image_to_string(imgtxtresized,config='--psm 7 --oem 3')
            #una carreta
            outputstr = str(output.replace('.', ''))
            output = int(output.rstrip())
            outputint = output
            if len(outputstr.rstrip())<= 3:
                outputint = output*1000000
            #print(output)
            #print(sumarsspermiso)
            #print(output1[index:].rstrip())
            if sumarsspermiso[4] < outputint:
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 630 162')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 276 263') #asunto
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "Banco de recursos"') #asunto-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input keyevent 66') #enter
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 203 403') #cuerpo
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "No tienes recursos en el banco"') #cuerpo-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 635 110') #back
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 638 663')
                time.sleep(np.random.uniform(1,1.1))
                device.shell(f'input tap 1235 44')
                time.sleep(0.5)
                device.shell(f'input tap 1235 44')
                time.sleep(5)
            else:
                time.sleep(np.random.uniform(0.1, 0.2))
                #enviarRecursos(usuarioimg2,'stone',output,limite)
                device.shell(f'input tap 279 525')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 635 181')
                time.sleep(np.random.uniform(1, 1.2))
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.3, 0.5))
                device.shell(f'input tap 632 327')
                time.sleep(np.random.uniform(0.4,0.5))
                enviarRecursos('mineral',output, output1[index:].rstrip())
                time.sleep(5)
        else:
            device.shell(f'input tap 1236 44')
            time.sleep(5)
			
def cmd_oro(screen):
    screen = screen
    imgstone1 = py.locate(resource_path('oro.png'),screen,region=(436,36,198,28),grayscale=True,confidence=0.8)
    if imgstone1 != None:
        imgtxt = screen.crop((imgstone1[0]+40,imgstone1[1],34+imgstone1[0]+41,18+imgstone1[1]))
        #hola = imgtxt.save("crop.png")
        #imgtxt = py.screenshot('cantidad-madera.png',region=(imgstone1[0]+82,imgstone1[1],34,19))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgstone1[0]} {imgstone1[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                sumarsspermiso = select_task_by_priority(conn, output1[index:].rstrip())
            resize = tuple(4*x for x in imgtxt.size)
            imgtxtresized = imgtxt.resize(resize, Image.Resampling.LANCZOS)
            output = pytesseract.image_to_string(imgtxtresized,config='--psm 7 --oem 3')
            #una carreta
            outputstr = str(output.replace('.', ''))
            output = int(output.rstrip())
            outputint = output
            if len(outputstr.rstrip())<= 3:
                outputint = output*1000000
            #print(output)
            #print(sumarsspermiso)
            #print(output1[index:].rstrip())
            if sumarsspermiso[5] < outputint:
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 630 162')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 276 263') #asunto
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "Banco de recursos"') #asunto-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input keyevent 66') #enter
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 203 403') #cuerpo
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input text "No tienes recursos en el banco"') #cuerpo-msj
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 635 110') #back
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 638 663')
                time.sleep(np.random.uniform(1,1.1))
                device.shell(f'input tap 1235 44')
                time.sleep(0.5)
                device.shell(f'input tap 1235 44')
                time.sleep(5)
            else:
                time.sleep(np.random.uniform(0.1, 0.2))
                #enviarRecursos(usuarioimg2,'stone',output,limite)
                device.shell(f'input tap 279 525')
                time.sleep(np.random.uniform(0.2, 0.3))
                device.shell(f'input tap 635 181')
                time.sleep(np.random.uniform(1, 1.2))
                device.shell(f'input tap 1008 123') # click ruedaa
                time.sleep(np.random.uniform(0.3, 0.5))
                device.shell(f'input tap 632 327')
                time.sleep(np.random.uniform(0.4,0.5))
                enviarRecursos('oro',output, output1[index:].rstrip())
                
                time.sleep(5)
        else:
            device.shell(f'input tap 1236 44')
            time.sleep(5)
#screen = screenshot()
#screen.save('spampasos.png')
#image = screen.crop((87,161,25+87,36+161))
##region=(81,161,38,228)
#image.save("construicon.png")

def cmd_spam(screen):
    screenspam = screen
    imgspam = py.locate(resource_path('spam.png'),screenspam,region=(436,36,198,28),grayscale=True,confidence=0.85)
    if imgspam != None:
        spamtxt = screenspam.crop((imgspam[0]+61,imgspam[1],40+imgspam[0]+65,18+imgspam[1]))
        time.sleep(np.random.uniform(0.3, 0.4))
        device.shell(f'input tap {imgspam[0]} {imgspam[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            #print("FUNCA RANGO")
            #resize = tuple(8*x for x in spamtxt.size)
            #imgtxtresized = spamtxt.resize(resize, Image.Resampling.LANCZOS)
            outputspam = pytesseract.image_to_string(spamtxt,config='--psm 7')
            #una carreta
            outputspam = int(str(outputspam))
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            contruicon = py.locate(resource_path('construicon.png'),screenspam,grayscale=True,confidence=0.8)
            if contruicon != None:
                #print(contruicon)
                for i in range(0,outputspam):
                    device.shell(f'input tap {contruicon[0]+308} {contruicon[1]}')
                    time.sleep(0.4)
                    device.shell(f'input tap 667 390')
                    time.sleep(0.4)
                # mejorar 1
                    device.shell(f'input tap 1095 633')
                    time.sleep(0.4) 
                #mejorar 2
                    device.shell(f'input tap 811 620')
                    time.sleep(0.4)
                    imgarmaduraspam = py.locate(resource_path('armadura-spam.png'),screenshot(),region=(449,311,383,62),grayscale=True,confidence=0.8)
                    if imgarmaduraspam != None:
                        device.shell(f'input tap 643 345')
                        time.sleep(0.4)
                        device.shell(f'input tap 1030 295')
                        time.sleep(0.4)
                        device.shell(f'input tap 811 620')
                    construcolor = screenshot()
                    pxc = construcolor.getpixel((396,168))
                    stop = py.locate(resource_path('stop-spam.png'),construcolor,region=(436,36,198,28),grayscale=True,confidence=0.8)
                    if stop != None:
                        break
                    if pxc[0] >= 230 and pxc[1] <= 87 and pxc >= 230:
                        #print("morado")
                        device.shell(f'input tap {contruicon[0]+308} {contruicon[1]}')
                    else:
                        # ayuda amarillo
                        device.shell(f'input tap {contruicon[0]+308} {contruicon[1]}')
                        time.sleep(0.6)
                        device.shell(f'input tap 667 430')
                        time.sleep(0.4)
                        device.shell(f'input tap 885 643')
                        time.sleep(0.4)
                        device.shell(f'input tap 741 416')
                        time.sleep(0.8)
                time.sleep(5)
        else:
            device.shell(f'input tap 1235 44')
            time.sleep(5)
            

def comandos():

    #try:
        screen = screenshot()
        regRSS(screen)
        cmd_comida(screen)
        cmd_piedra(screen)
        cmd_mineral(screen)
        cmd_oro(screen)
        cmd_madera(screen)
        cmd_spam(screen)
        statsrss(screen)
        statsrssuser(screen)
        ###HACER QUE DESCUENTE RSS AL CONFIRMAR LOS RSS
    #except Exception as err:
      #  #print(err)
        #continue
    
    
def sanar(poor):
    if len(poor)<=3:
        return float(poor)
    if poor.find(",")!=-1:
        poorsano = poor.replace(",",".")
        poorsano.strip()
        return float(poorsano)
    elif poor.find("K")!=-1:
        poorsano = poor.replace("K","")
        poorsano.strip()
        return float(poorsano)*1000
    elif poor.find("M")!=-1:
        poorsano = poor.replace("M","")
        poorsano.strip()
        return float(poorsano)*1000000
    else:
        return 0
def statsrss(screen): #empezar desde aca
    screenspam = screen
    imgstats = py.locate(resource_path('rssadmincommand.png'),screenspam,region=(436,36,198,28),grayscale=True,confidence=0.85)
    if imgstats != None:
        notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
        if notinUIX != None:
                device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                time.sleep(np.random.uniform(0.2, 0.3))
                while True:
                    screen = screenshot()
                    notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
                    if notinUIX != None:
                        device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                        time.sleep(np.random.uniform(0.2, 0.3))
                    else:
                        break
        screen = screenshot()
        device.shell(f'input tap {imgstats[0]} {imgstats[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            imagecomida = screen.crop((1147,8,95+1147,26+8))
            imagepiedra = screen.crop((1149,46,88+1148,31+46))
            imagemadera = screen.crop((1149,86,89+1149,30+86))
            imagemineral = screen.crop((1148,125,90+1148,30+125))
            imageoro = screen.crop((1146,163,93+1146,31+163))
            #imagecomida.save("rssadmincropc.png")
            #imagepiedra.save("rssadmincropp.png")
            #imagemadera.save("rssadmincropm.png")
            #imagemineral.save("rssadmincropmi.png")
            #imageoro.save("rssadmincropor.png")
            output1 = pytesseract.pytesseract.image_to_string(imagecomida,config='--psm 7 --oem 3')
            output2 = pytesseract.pytesseract.image_to_string(imagepiedra,config='--psm 7 --oem 3')
            output3 = pytesseract.pytesseract.image_to_string(imagemadera,config='--psm 7 --oem 3')
            output4= pytesseract.pytesseract.image_to_string(imagemineral,config='--psm 7 --oem 3')
            output5 = pytesseract.pytesseract.image_to_string(imageoro,config='--psm 7 --oem 3')
            #print(output1)
            #print(output2)
            #print(output3)
            #print(output4)
            #print(output5)
            #print("FUNCA RANGO")
            device.shell(f'input tap 1008 123') # click ruedaa
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 630 162')
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 276 263') #asunto
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Banco de recursos"') #asunto-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input keyevent 66') #enter
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 203 403') #cuerpo
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Comida: {output1} \nPiedra: {output2} \nMadera: {output3} \nMineral: {output4} \nOro: {output5}"') #cuerpo-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 638 663')
            time.sleep(np.random.uniform(1,1.1))
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
        else:
            device.shell(f'input tap 1008 123') # click ruedaa
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 630 162')
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 276 263') #asunto
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Acceso denegado"') #asunto-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 203 403') #cuerpo
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "No tienes los permisos suficientes para ver los recursos del banco."') #cuerpo-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 638 663')
            time.sleep(np.random.uniform(1,1.1))
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
        time.sleep(5)
#screen = screenshot()
#comando = screen.crop((521,36,105+521,28+36))
#comando.save("rrsusercommand.png")
#exit()
def statsrssuser(screen): #empezar desde aca
    screenspam = screen
    imgstats = py.locate(resource_path('rrsusercommand.png'),screenspam,region=(436,36,198,28),grayscale=True,confidence=0.85)
    if imgstats != None:
        notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
        if notinUIX != None:
                device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                time.sleep(np.random.uniform(0.2, 0.3))
                while True:
                    screen = screenshot()
                    notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
                    if notinUIX != None:
                        device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                        time.sleep(np.random.uniform(0.2, 0.3))
                    else:
                        break
        device.shell(f'input tap {imgstats[0]} {imgstats[1]}')
        #click(imgstone1[0],imgstone1[1])
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 1156 653')
        time.sleep(np.random.uniform(0.1, 0.2))
        device.shell(f'input tap 400 535')
        time.sleep(np.random.uniform(0.2, 0.3))
        device.shell(f'input tap 640 180')
        time.sleep(np.random.uniform(0.6, 0.7))
        #foto = py.screenshot('r4.png',region=(279,525,39,38))
        rangosimg = screenshot()
        usuarioimg2 = py.locate(resource_path('rango-4.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr5 = py.locate(resource_path('rango-5.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr3 = py.locate(resource_path('rango-3.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr2 = py.locate(resource_path('rango-2.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        usuarioimgr1 = py.locate(resource_path('rango-1.png'),rangosimg,region=(220,78,54,51),grayscale=True,confidence=0.8)
        if usuarioimg2 != None or usuarioimgr5 != None or usuarioimgr3 != None or usuarioimgr2 != None or usuarioimgr1 != None:
            screen = screenshot()
            nombreUI = screen.crop((269,81,344+269,45+81))
            #nombreUI.save("usernameUI.png")
            output1 = pytesseract.pytesseract.image_to_string(nombreUI,config='--psm 7 --oem 3')
            index = output1.index("]")+1
            conn = create_connection(database)
            with conn:
                outputuserrss = select_task_by_priority(conn, output1[index:].rstrip())
            #print("FUNCA RANGO")
            device.shell(f'input tap 1008 123') # click ruedaa
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 630 162')
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 276 263') #asunto
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Banco de recursos"') #asunto-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input keyevent 66') #enter
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 203 403') #cuerpo
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Comida: {outputuserrss[1]:,} \nPiedra: {outputuserrss[2]:,} \nMadera: {outputuserrss[3]:,} \nMineral: {outputuserrss[4]:,} \nOro: {outputuserrss[5]:,}"') #cuerpo-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 638 663')
            time.sleep(np.random.uniform(1,1.1))
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
        else:
            device.shell(f'input tap 1008 123') # click ruedaa
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 630 162')
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 276 263') #asunto
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "Acceso denegado"') #asunto-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input tap 203 403') #cuerpo
            time.sleep(np.random.uniform(0.2, 0.3))
            device.shell(f'input text "No tienes los permisos suficientes para ver los recursos del banco."') #cuerpo-msj
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 635 110') #back
            time.sleep(np.random.uniform(0.1, 0.2))
            device.shell(f'input tap 638 663')
            time.sleep(np.random.uniform(1,1.1))
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
            device.shell(f'input tap 1235 44')
            time.sleep(0.5)
        time.sleep(5)
def regRSS(screenrss):

        try:
            screen = screenrss
            #screenrss.save('regRSS.png')
            px = screen.getpixel((1,1))
            if px[0] <= 67 and px[1] >= 111:
                #print("VIENDO VERDE DE ENVIARRS")
                notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
                if notinUIX != None:
                    device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                    time.sleep(np.random.uniform(0.2, 0.3))
                    while True:
                        screen = screenshot()
                        notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
                        if notinUIX != None:
                            device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                            time.sleep(np.random.uniform(0.2, 0.3))
                        else:
                            break
                device.shell(f'input tap 700 670')
                time.sleep(np.random.uniform(0.1, 0.2))
                device.shell(f'input tap 1193 280')
                time.sleep(np.random.uniform(0.2, 0.3))
                while True:
                    screen = screenshot()
                    #image = screen.crop((189,194,62+189,49+194))
                    #image.save('regRSSIcon.png')
                    regrssicon = py.locate(resource_path('regRSSIcon.png'),screen,grayscale=True,confidence=0.8)
                    if regrssicon != None:
                        #print(regrssicon)
                        px = screen.getpixel((regrssicon[0]+58,regrssicon[1]-20))
                        #print(px)
                        if px[0] >= 196 and px[1] <= 60:
                            #print("ES NUEVO RSS")
                            device.shell(f'input tap {regrssicon[0]} {regrssicon[1]}')
                            #print("Leyendo rss entrantes... despues de 3 sec.")
                            time.sleep(3.1)
                            i=0
                            screen = screenshot()
                            for posentrante in py.locateAll(resource_path('regRSSentrante.png'),screen,grayscale=True,confidence=0.945):
                                if i>2:
                                    #print("Hay mas de 3 reportes - revisar: " + outputhistorial + " Fecha: " + outputhistorialfecha)
                                    break
                                #print(posentrante)
                                ## Imagen c/u
                                imagehistorial = screen.crop((418,posentrante[1],400+250,35+posentrante[1]))
                                #imagehistorial.save("nombrehistory.png")
                                imagehistorialfecha = screen.crop((950,posentrante[1],184+950,36+posentrante[1]))
                                #imagehistorial.save("imagehistorialrsss2.png")
                                imagecomida = screen.crop((345,posentrante[1]+55,91+345,37+posentrante[1]+55))
                                imagepiedra = screen.crop((506,posentrante[1]+55,91+506,37+posentrante[1]+55))
                                imagemadera = screen.crop((666,posentrante[1]+55,91+666,37+posentrante[1]+55))
                                imagemineral = screen.crop((820,posentrante[1]+55,91+820,37+posentrante[1]+55))
                                imageoro = screen.crop((976,posentrante[1]+55,91+976,37+posentrante[1]+55))
                                #resize = tuple(8*x for x in image.size)
                                #rss = image.resize(resize, Image.Resampling.LANCZOS)
                                #rss.save("regRSSINFODATA.png")
                                outputhistorialfecha = pytesseract.pytesseract.image_to_string(imagehistorialfecha,config='--psm 11 --oem 3')
                                outputhistorial = pytesseract.pytesseract.image_to_string(imagehistorial,config='--psm 11 --oem 3')
                                outputcomida = pytesseract.pytesseract.image_to_string(imagecomida,config='--psm 7 --oem 3')
                                outputpiedra = pytesseract.pytesseract.image_to_string(imagepiedra,config='--psm 7 --oem 3')
                                outputmadera = pytesseract.pytesseract.image_to_string(imagemadera,config='--psm 7 --oem 3')
                                outputmineral = pytesseract.pytesseract.image_to_string(imagemineral,config='--psm 7 --oem 3')
                                outputoro = pytesseract.pytesseract.image_to_string(imageoro,config='--psm 7 --oem 3')
                                ## METER DATA SANA A SQLITE
                                conn = create_connection(database)
                                with conn:
                                    # guardar historial
                                    rssinfo = (outputhistorial.rstrip(),outputhistorialfecha.rstrip(),sanar(outputcomida),sanar(outputpiedra),sanar(outputmadera),sanar(outputmineral),sanar(outputoro))
                                    rssinfodb = create_project(conn, rssinfo)
                                    sumarss = select_task_by_priority(conn, outputhistorial.rstrip())
                                    ## guardar SUM en rsstotal
                                    rssplus = (sumarss[0],outputhistorial.rstrip(),sumarss[1],sumarss[2],sumarss[3],sumarss[4],sumarss[5]);
                                    rssinfodb = create_total(conn, rssplus)
                                    #print("GUARDADO EN SQLITE")
                                #print(outputhistorial)
                                #print(outputhistorialfecha)
                                ## Sanitizar float
                                #print(sanar(outputcomida))
                                #print(sanar(outputpiedra))
                                #print(sanar(outputmadera))
                                #print(sanar(outputmineral))
                                #print(sanar(outputoro))
                                ## Sanitizar las variables
                                #outputcomida
                                #outputpiedra
                                #outputmadera
                                #outputmineral
                                #outputoro
                                ## DECODIFICAR NOMBRE Y FECHA PARA REGISTRO Y CONTROL DE ERRORES
                                ## DECODIFICAR NOMBRE Y FECHA PARA REGISTRO Y CONTROL DE ERRORES
                                ## DECODIFICAR NOMBRE Y FECHA PARA REGISTRO Y CONTROL DE ERRORES
                                
                                #text_file = open("C:/Users/Rodrigo/Documents/lord/ADB/RSS.txt", "a")
                                #text_file.writelines(outputhistorial)
                                #text_file.writelines(outputhistorialfecha)
                                #text_file.writelines(outputcomida+" - "+outputpiedra+" - "+outputmadera+" - "+outputmineral+" - "+outputoro)
                                #text_file.close()
                                i+=1
                        ## Cierre de ciclo data rss
                            device.shell(f'input tap 1233 42')
                            time.sleep(0.1)
                            device.shell(f'input tap 1233 42')
                            #print("FIN CICLO")
                            break
        except Exception as err:
            conn = create_connection(database)
            with conn:
                rssplusex = ("Bloque regRSS - Registro de RSS ",str(err),str(type(err)));
                rssinfodbex = create_tryexp(conn, rssplusex)
            print(err)
            screen = screenshot()
            notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
            if notinUIX != None:
                device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                time.sleep(np.random.uniform(0.2, 0.3))
                while True:
                    screen = screenshot()
                    notinUIX = py.locate(resource_path('notinUIX.png'),screen,grayscale=True,confidence=0.8)
                    if notinUIX != None:
                        device.shell(f'input tap {notinUIX[0]} {notinUIX[1]}')
                        time.sleep(np.random.uniform(0.2, 0.3))
                    else:
                        break
            pass
            ##Guardar un log en sqlite. a codearlo...
#statsrss()
##print("SCREEN EN path")
#screen = screenshot()
#screen.save('rssadminchat.png')
#image = screen.crop((521,36,100+521,28+36))
#image.save("rssadmincommand.png")


#image = screen.crop((1143,4,93+1143,193+4))

print("MacroLord - Personal Bot")
print("Introducir los comandos en el chat de tu gremio: \n !spam y !stop \n !comida \n !piedra \n !madera \n !mineral \n !oro \n Vadminrss \n Vuserbank")
print("Uso del comando !spam para generar 120 ayudas -> !spam 120")
print("Uso del comando !stop para detener las ayudas -> !stop")
print("Uso del comando !comida para pedir 100millones del banco -> !comida 100")
print("Uso del comando !piedra para pedir 100millones del banco -> !piedra 100")
print("Uso del comando !madera para pedir 100millones del banco -> !madera 100")
print("Uso del comando !mineral para pedir 100millones del banco -> !mineral 100")
print("Uso del comando !oro para pedir 100millones del banco -> !oro 100")
print("Uso del comando Vadminrss para ver los recursos del banco -> Vadminrss")
print("Uso del comando Vuserbank para ver los recursos enviados hacia el banco -> Vuserbank")
#t1 = threading.Thread(target=comandos)
#t2 = threading.Thread(target=regRSS)

while keyboard.is_pressed('q') == False:
    try:
        comandos()
        ###HACER QUE DESCUENTE RSS AL CONFIRMAR LOS RSS
    except Exception as err:
        print(err)
        continue
