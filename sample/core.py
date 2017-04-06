# This Python file uses the following encoding: utf-8
from collections import Counter

import Connection

import re
import string

conexion = Connection.Conection()
cliente = conexion.conected()
def analIce(inputString):

    """las stopwords son las palabras que debe ignorar el ñrograma a la hora de contar palabras"""
    stopWords = "a about above after again against all am an and any are aren't as at be because been before being below" \
                " between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few " \
                "for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him " \
                "himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself" \
                " no nor not of off on once only or other ought our ours 	ourselves out over own same shan't she she'd she'll she's " \
                "should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd " \
                "they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't " \
                "what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're" \
                " you've your yours yourself yourselves ".split()
    if (inputString is None):
        raise TypeError


    uniInput = unicode(inputString,encoding='utf-8')

    """las palabras aceptadas son las que estén formadas por letras de la a-z(tanto minúscula como mayúscula), números del 0 al 9,
     y letras con tildes, incluidas en los codigos utf-8 especificados"""
    rexUnPoliciaDiferente = r"[a-zA-Z'0-9\xed\xc1\xe1\xc9\xcd\xd1\xda\xf1\xf3\xfa\xfc\xe9\xd3\xdc]+"


    matches = re.findall(rexUnPoliciaDiferente,uniInput)
    coolWords = [match.lower()for match in matches if match.lower() not in stopWords]
    utf8Result = filter (lambda x: x.encode('utf8'),coolWords)

    return Counter(utf8Result).most_common()

"""La función create crea el documento que contiene el diccionario obtenido a través del String inputString y lo inserta en la colección words de mongo.
    Si la función no recibe ningúnstring, devuelve None."""
def Create(inputString,cliente):
    if(not inputString):
        return None
    diccionario = {}


    diccionario.update({'palabras':inputString})
    #print diccionario
    return cliente.words.insert(diccionario)

"""La función Read devuelve el diccionario cuyo identificador se introduce como variable. Si no hay ningún documento con ese ID, devuelve un None"""
def Read(identificador,db):
    try:
        diccionarioLeido=db.words.find({'_id': identificador}).next()
    except StopIteration:
        return None
    return diccionarioLeido

"""La función Update modifica el contador de la palabra introducida como key al valor value. Si no se introduce una clave o un valor, devuelve None"""
def Update(identificador,db,key,value):
    if(not value or not key):
        return None
    db.words.update({'_id':identificador},{'$set':{key:value}})
    res=db.words.aggregate([{'$match':{'_id':identificador}},{'$project':{'_id':0,'palabras':1}}]).next()['palabras']['key']
    return res

"""La función Delete borra el documento con el identificador introducido"""
def Delete(identificador,db):
    db.words.remove({'_id': identificador})


if __name__ == "__main__":
    palabra=[]
    #palabra=analIce("Hola hey hey HEY Aquíaaa AquÍaaa.  Á  É  Í Ñ Ó Ú Ü á é í  ó ú ü ñu I'm a about ab1ba ")
    #palabra={'key':'value'}
    palabra = {'key': 'value', 'hola':'adios'}
    id= Create(palabra,cliente)

    #Update(id,cliente,'palabras.key',43)
    #print Read(0,cliente)['palabras']['key']
    #print cliente.words.aggregate([{'$project':{'_id':0,'palabras':1}}]).next()['palabras']['key']
    #identificador=cliente.words.aggregate([{'$project':{'_id':1}},{'$limit':1}]).next()
    #print identificador['_id']
    #print Read(identificador['_id'],cliente)
    #Update(identificador['_id'],cliente,'palabras.1.1',17)
    #Delete(1,cliente)


#print dict
"""
Como crear la conexión

 conexion= connection.Conection()
    cliente=conexion.conected() #Conexion creada


    contenido=cliente.city.find_one() #city es la coleccion de la base de datos en la querramos hacer la operación find_one

"""