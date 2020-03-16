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
    with open(fichc) as fc:
        f = csv.DictReader(fc, delimiter=';')
        for filas in f:

            # -----------------------------------

            qrg = filas['kHz:75']
            days = filas['Days:59']
            language = filas['Lng:49']
            station = filas['Station:201']
            time = filas['Time(UTC):93']
            region = filas['ITU:49']
            remarks = filas['Remarks:135']

            if days is '':
                days = '1234567'

            if language is '':
                language = 'n/a'

            # -----------------------------------

            datos[qrg] = {
                'station': station,
                'time': time,
                'days': days,
                'region': region,
                'language': language,
                'remarks': remarks
            }

    with open(fichj, 'w') as fj:
        fj.write(json.dumps(datos, indent=4))


if __name__ == '__main__':
    tratar_csv(f_eibi_csv, f_eibi_json)
    # tratar_csv(f_hfcc_csv, f_hfcc_json)
    # tratar_csv(f_ncb_csv, f_ncb_json)
    escribir_bbdd()
