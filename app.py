# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" SWL Grabber """

__devteam__ = 'CrazyHams'
__date__ = "15/03/2020"

import json
import csv

# Ficheros de entrada en formato CSV
f_eibi_csv = 'sked-b19.csv'
f_hfcc_csv = ''
f_ncb_csv = ''

# Fichero de salida en formato JSON
f_eibi_json = 'eibi.json'
f_hfcc_json = 'hfcc.json'
f_ncb_json = 'ncb.json'


def escribir_bbdd():
    pass


def tratar_csv(fichc, fichj):
    """
    Esta función trata un CSV de entrada y genera un JSON de salida
    :param: a CSV (application/text)
    :return: a JSON (application/json)
    """
    datos = {}
    with open(fichc, encoding='utf-8') as fc:
        f = csv.DictReader(fc, delimiter=';')
        i=1
        for filas in f:

            # -----------------------------------

            qrg = filas['kHz:75']
            days = filas['Days:59']
            language = filas['Lng:49']
            station = filas['Station:201']
            time = filas['Time(UTC):93']
            region = filas['ITU:49']
            remarks = filas['Remarks:135']

            if days is '': days = '1234567'
            elif days == 'Mo-Sa': days = '123456'
            elif days == 'Mo-Fr': days = '12345'
            elif days == 'Mo-Th': days = '1234'
            elif days == 'Mo-We': days = '123'
            elif days == 'Mo,Su': days = '17'
            elif days == 'Mo,Sa': days = '16'
            elif days == 'Mo,Fr': days = '15'
            elif days == 'Mo,Th': days = '14'
            elif days == 'Mo,We': days = '13'
            elif days == 'Mo-Tu': days = '12'
            elif days == 'Mo,Tu': days = '12'
            elif days == 'Mo'   : days = '1'
            elif days == 'Tu-Su': days = '234567'
            elif days == 'Tu-Sa': days = '23456'
            elif days == 'Tu-Fr': days = '2345'
            elif days == 'Tu-Th': days = '234'
            elif days == 'Tu,Su': days = '27'
            elif days == 'Tu,Sa': days = '26'
            elif days == 'Tu,Fr': days = '25'
            elif days == 'Tu,Th': days = '24'
            elif days == 'Tu-We': days = '23'
            elif days == 'Tu,We': days = '23'
            elif days == 'Tu'   : days = '2'
            elif days == 'We-Mo': days = '345671'
            elif days == 'We-Su': days = '34567'
            elif days == 'We-Sa': days = '3456'
            elif days == 'We-Fr': days = '345'
            elif days == 'We,Su': days = '37'
            elif days == 'We,Sa': days = '36'
            elif days == 'We,Fr': days = '35'
            elif days == 'We-Th': days = '34'
            elif days == 'We,Th': days = '34'
            elif days == 'We,Th': days = '34'
            elif days == 'We'   : days = '3'
            elif days == 'Th-Tu': days = '456712'
            elif days == 'Th-Su': days = '4567'
            elif days == 'Th-Sa': days = '456'
            elif days == 'Th,Su': days = '47'
            elif days == 'Th,Sa': days = '46'
            elif days == 'Th-Fr': days = '45'
            elif days == 'Th,Fr': days = '45'
            elif days == 'Th'   : days = '4'
            elif days == 'Fr-We': days = '567123'
            elif days == 'Fr-Mo': days = '5671'
            elif days == 'Fr-Su': days = '567'
            elif days == 'Fr,Su': days = '57'
            elif days == 'Fr,Sa': days = '56'
            elif days == 'Fr-Sa': days = '56'
            elif days == 'Fr'   : days = '5'
            elif days == 'Sa-Fr': days = '6712345'
            elif days == 'Sa-Th': days = '671234'
            elif days == 'Sa-We': days = '67123'
            elif days == 'Sa-Tu': days = '6712'
            elif days == 'Sa-Mo': days = '671'
            elif days == 'SaSu' : days = '67'
            elif days == 'Sa'   : days = '6'
            elif days == 'Su-Fr': days = '712345'
            elif days == 'Su-Th': days = '71234'
            elif days == 'Su-We': days = '7123'
            elif days == 'Su-Tu': days = '712'
            elif days == 'Su-Mo': days = '71'
            elif days == 'Su'   : days = '7'

            if language is '':
                language = 'n/a'

            # -----------------------------------

            datos[i] = {
                'qrg': qrg,
                'station': station,
                'time': time,
                'days': days,
                'region': region,
                'language': language,
                'remarks': remarks
            }

            i+=1

    with open(fichj, 'w') as fj:
        fj.write(json.dumps(datos, sort_keys=False, indent=4))


if __name__ == '__main__':
    tratar_csv(f_eibi_csv, f_eibi_json)
    # tratar_csv(f_hfcc_csv, f_hfcc_json)
    # tratar_csv(f_ncb_csv, f_ncb_json)
    escribir_bbdd()
