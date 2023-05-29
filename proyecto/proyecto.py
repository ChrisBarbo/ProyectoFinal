from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt
AgenciApp = Flask(__name__)
AgenciApp.config['MYSQL_HOST']='localhost'
AgenciApp.config['MYSQL_USER']='root'
AgenciApp.config['MYSQL_PASSWORD']='mysql'
AgenciApp.config['MYSQL_DB']='proyecto'
AgenciApp.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(AgenciApp)

@AgenciApp.route('/')
def index():
    return render_template('login.html')

@AgenciApp.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:	

        Usuario     =   request.form["Usuario"]
        nombrec     =   request.form["nombrec"]
        correoc     =   request.form["correoc"]
        direccion   =   request.form["direccion"]
        telefonoc   =   request.form["telefonoc"]
        clave       =   request.form["clave"].encode('utf-8')
        ClaveCifrada    = bcrypt.hashpw(clave,bcrypt.gensalt())
        regCliente = mysql.connection.cursor()
        regCliente.execute("INSERT INTO cliente (nombrec,correoc,direccion,telefonoc,clave,Usuario) VALUES (%s,%s,%s,%s,%s,%s)", (nombrec,correoc,direccion,telefonoc,ClaveCifrada,Usuario))
        mysql.connection.commit()
        return redirect(url_for('login')) 

@AgenciApp.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        Usuario = request.form["Usuario"]
        clave   = request.form["clave"].encode('utf-8')
        selCli = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selCli.execute("SELECT * FROM cliente WHERE Usuario = %s",(Usuario,))
        c = selCli.fetchone()
        selCli.close()
        if c is not None:
            if bcrypt.hashpw(clave, c['clave'].encode('utf-8')) == c['clave'].encode('utf-8'):
                session['nombrec'] = c['nombrec']
                return redirect(url_for('home'))
            else:
                    flash('ERROR: Contraseña Incorrecta')
                    return redirect(request.url)
        else:
                    flash('ERROR: El Usuario no Existe')
                    return redirect(request.url)
    else:
        return render_template('login.html')

@AgenciApp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@AgenciApp.route('/home')
def home():
    return render_template('home.html')  

#--------------------------------------------------------C L I E N T E ----------------------------------------------------------------------#
#------ Select -------#
@AgenciApp.route('/sCliente')
def sCliente():
    selCliente = mysql.connection.cursor()
    selCliente.execute("SELECT * FROM cliente")
    c = selCliente.fetchall()
    selCliente.close()
    return render_template('cliente.html', cliente = c)

#----------Registrar---------------------------------#    

@AgenciApp.route('/iCliente', methods=["POST"])
def iCliente():
    Usuario     =   request.form["Usuario"]
    nombrec     =   request.form["nombrec"]
    correoc     =   request.form["correoc"]
    direccion   =   request.form["direccion"]
    telefonoc   =   request.form["telefonoc"]
    clave       =   request.form["clave"].encode('utf-8')
    ClaveCifrada    = bcrypt.hashpw(clave,bcrypt.gensalt())
    regCliente = mysql.connection.cursor()
    regCliente.execute("INSERT INTO cliente (Usuario,nombrec,correoc,direccion,telefonoc,clave) VALUES(%s,%s,%s,%s,%s,%s)",(Usuario,nombrec,correoc,direccion,telefonoc,ClaveCifrada))
    mysql.connection.commit()
    return redirect(url_for('sCliente'))

 #-----------------Actualizar--------------------------#

@AgenciApp.route('/uCliente', methods=["POST"])
def uCliente():
    Usuario     =   request.form["Usuario"]
    nombrec     =   request.form["nombrec"]
    correoc     =   request.form["correoc"]
    direccion   =   request.form["direccion"]
    telefonoc   =   request.form["telefonoc"]
    clave       =   request.form["clave"].encode('utf-8')
    idcliente   =   request.form["idcliente"]
    ClaveCifrada    = bcrypt.hashpw(clave,bcrypt.gensalt())
    actCliente = mysql.connection.cursor()
    actCliente.execute("UPDATE cliente SET Usuario = %s, nombrec = %s, correoc = %s, direccion = %s, telefonoc = %s, clave = %s WHERE idcliente = %s", (Usuario,nombrec,correoc,direccion,telefonoc,ClaveCifrada,idcliente))
    mysql.connection.commit()
    return redirect(url_for('sCliente'))


#----------Eliminar-------#
@AgenciApp.route('/dCliente/<string:IdCliente>', methods= ["GET"])
def dCliente(IdCliente):
        delCliente = mysql.connection.cursor()
        delCliente.execute("DELETE FROM cliente WHERE IdCliente = %s",(IdCliente,))
        mysql.connection.commit()
        return redirect(url_for('sCliente'))


#------------------------------------------------- T R A N S P O R T E --------------------------------------------------#
#---------Select----------------#
@AgenciApp.route('/sTrans')
def sTrans():
    selTrans = mysql.connection.cursor()
    selTrans.execute("SELECT * FROM transporte")
    t = selTrans.fetchall()
    selTrans.close()
    return render_template('transporte.html', transporte = t)

#---------- Registrar---------#
@AgenciApp.route('/iTrans', methods=["POST"])
def iTrans():
    tipot   =   request.form["tipot"]
    clase   =   request.form["clase"]
    preciot =   request.form["preciot"]
    marca   =   request.form["marca"]
    regTransporte = mysql.connection.cursor()
    regTransporte.execute("INSERT INTO transporte (tipot,clase,preciot,marca) VALUES (%s,%s,%s,%s)", (tipot,clase,preciot,marca))
    mysql.connection.commit()
    return redirect(url_for('sTrans'))   

#---------- Actualizar --------------#
@AgenciApp.route('/uTrans', methods=["POST"])
def uTrans():
    tipot   =   request.form["tipot"]
    clase   =   request.form["clase"]
    preciot =   request.form["preciot"]
    marca   =   request.form["marca"]
    idtransporte    =   request.form["idtransporte"]
    actTransporte = mysql.connection.cursor()
    actTransporte.execute("UPDATE transporte SET tipot = %s, clase = %s, preciot = %s, marca = %s WHERE idtransporte = %s", (tipot,clase,preciot,marca,idtransporte))
    mysql.connection.commit()
    return redirect(url_for('sTrans'))

#------------ Eliminar -------------#
@AgenciApp.route('/dTrans/<string:idtransporte>', methods= ["GET"])
def dTrans(idtransporte):
        delTransporte = mysql.connection.cursor()
        delTransporte.execute("DELETE FROM transporte WHERE idtransporte = %s",(idtransporte,))
        mysql.connection.commit()
        return redirect(url_for('sTrans'))   

#-------------------------------------------------------------------HOSPEDAJE (D)-------------------------------------------------------------------------#
#---------Select----------------#
@AgenciApp.route('/sHosp')
def sHosp():
    selHosp = mysql.connection.cursor()
    selHosp.execute("SELECT * FROM hospedaje")
    h = selHosp.fetchall()
    selHosp.close()
    return render_template('hospedaje.html', hospedaje = h)

#---------- Registrar---------#
@AgenciApp.route('/iHosp', methods=["POST"])
def iHosp():
    descripcion   =   request.form["descripcion"]
    nombreh =   request.form["nombreh"]
    valoracion   =   request.form["valoracion"]
    estancia    =   request.form["estancia"]
    regHospedaje = mysql.connection.cursor()
    regHospedaje.execute("INSERT INTO hospedaje (descripcion,nombreh,valoracion,estancia) VALUES (%s,%s,%s,%s)", (descripcion,nombreh,valoracion,estancia))
    mysql.connection.commit()
    return redirect(url_for('sHosp'))   

#---------- Actualizar --------------#
@AgenciApp.route('/uHosp', methods=["POST"])
def uHosp():
    descripcion   =   request.form["descripcion"]
    nombreh =   request.form["nombreh"]
    valoracion   =   request.form["valoracion"]
    estancia    =   request.form["estancia"]
    idhotel    =   request.form["idhotel"]
    actHospedaje = mysql.connection.cursor()
    actHospedaje.execute("UPDATE hospedaje SET descripcion = %s, nombreh = %s, valoracion = %s, estancia = %s WHERE idhotel = %s", (descripcion,nombreh,valoracion,estancia,idhotel))
    mysql.connection.commit()
    return redirect(url_for('sHosp'))

#------------ Eliminar -------------#
@AgenciApp.route('/dHosp/<string:idhotel>', methods= ["GET"])
def dHosp(idhotel):
    delHospedaje = mysql.connection.cursor()
    delHospedaje.execute("DELETE FROM hospedaje WHERE idhotel = %s",(idhotel,))
    mysql.connection.commit()
    return redirect(url_for('sHosp'))   




#-----------------------------------------------------------RESERVACION (F)--------------------------------------------------------#
#---------Select----------------#
@AgenciApp.route('/sResv')
def sResv():
    selReservacion  =   mysql.connection.cursor()
    selReservacion.execute("SELECT * FROM reservacion INNER JOIN cliente ON reservacion.idcliente = cliente.idcliente INNER JOIN transporte ON reservacion.idtransporte = transporte.idtransporte INNER JOIN hospedaje ON reservacion.idhotel = hospedaje.idhotel")     
    r       =   selReservacion.fetchall()
    selReservacion.close()

    selCliente     =   mysql.connection.cursor()
    selCliente.execute("SELECT * FROM cliente")
    c      =   selCliente.fetchall()
    selCliente.close()

    selTrans     =   mysql.connection.cursor()
    selTrans.execute("SELECT * FROM transporte")
    t      =   selTrans.fetchall()
    selTrans.close()

    selHosp     =   mysql.connection.cursor()
    selHosp.execute("SELECT * FROM hospedaje")
    h      =   selHosp.fetchall()
    selHosp.close()

    return render_template('reservacion.html', reservaciones = r, clientes = c, transportes = t, hospedajes = h)


#---------- Registrar---------#
@AgenciApp.route('/iResv', methods=["POST"])
def iResv(): #---idreservacion	idcliente	idhotel	idtransporte nombrec  nombreh	tipot	cantdias	cantpersonas	llegadah	salidah--#
    idcliente =   request.form["idcliente"]
    idhotel =   request.form["idhotel"]
    idtransporte =   request.form["idtransporte"]     
    cantdias  =   request.form["cantdias"]
    cantpersonas    =   request.form["cantpersonas"]
    llegadah =   request.form["llegadah"]
    salidah =   request.form["salidah"]
    ubicacion =   request.form["ubicacion"]  
    regReservacion = mysql.connection.cursor()
    regReservacion.execute("INSERT INTO reservacion (idcliente,idhotel,idtransporte,cantdias,cantpersonas,llegadah,salidah,ubicacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (idcliente,idhotel,idtransporte,cantdias,cantpersonas,llegadah,salidah,ubicacion))
    mysql.connection.commit()
    return redirect(url_for('sResv'))   

#---------- Actualizar --------------#
@AgenciApp.route('/uResv', methods=["POST"])
def uResv():
    idcliente =   request.form["idcliente"]
    idhotel =   request.form["idhotel"]
    idtransporte =   request.form["idtransporte"]     
    cantdias  =   request.form["cantdias"]
    cantpersonas    =   request.form["cantpersonas"]
    llegadah =   request.form["llegadah"]
    salidah =   request.form["salidah"]
    ubicacion =   request.form["ubicacion"] 
    idreservacion   =   request.form["idreservacion"]  
    actHospedaje = mysql.connection.cursor()
    actHospedaje.execute("UPDATE reservacion SET idcliente = %s, idhotel = %s, idtransporte = %s, cantdias = %s, cantpersonas = %s, llegadah = %s, salidah = %s, ubicacion = %s WHERE idreservacion = %s", (idcliente,idhotel,idtransporte,cantdias,cantpersonas,llegadah,salidah,ubicacion,idreservacion))
    mysql.connection.commit()
    return redirect(url_for('sResv'))

#------------ Eliminar -------------#
@AgenciApp.route('/dResv/<string:idreservacion>', methods= ["GET"])
def dResv(idreservacion):
    delReservacion = mysql.connection.cursor()
    delReservacion.execute("DELETE FROM reservacion WHERE idreservacion = %s",(idreservacion,))
    mysql.connection.commit()
    return redirect(url_for('sResv'))



    

             
if __name__=='__main__': 
    AgenciApp.secret_key='secreto'
    AgenciApp.run(port=3000,debug=True)
