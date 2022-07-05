import pypyodbc 

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=EXCALIBUR-PC;'
    'Database=deneme;'
    'Trusted_Connection=True;'
)

cursor = db.cursor()


def ekle():    
    
    print("Konu baslık numaraları Pyhton = 1 , Siber tehdit türleri = 2 Yöntemler = 3 ")
    konuNo = input("Konu baslık numarası girin  :  ")
    konuBaslık = input ("Konu baslığını giriniz : ")
    konuDetay = input ("Konuyla ilgili detay : ")
    
    veri1= ( konuNo , konuBaslık, konuDetay)
    eklekomut = 'INSERT INTO odev VALUES (?,?,?)'
    

    calıstır = cursor.execute(eklekomut,veri1)
    db.commit()

def sorguOdev():
    cursor.execute('SELECT * FROM odev')
    odevsorgu = cursor.fetchall()
    for i in odevsorgu:
        print(i)


def sorguTerim():
    cursor.execute('SELECT * FROM Terimler')
    terimsorgu = cursor.fetchall()
    for i in terimsorgu:
        print(i)

def silme():
    sorguOdev()
    veri2 = [input("Silinmesini istediğiniz kişinin id adresini giriniz = ")]
    silkomut = 'DELETE FROM odev WHERE id=(?)'
    sil = cursor.execute(silkomut , veri2)
    db.commit()

sorguTerim()

  