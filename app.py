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
            qrg = filas['kHz:75']
            if filas['Days:59'] is '':
                filas['Days:59'] = 'all'
            if filas['Lng:49'] is '':
                filas['Lng:49'] = 'n/a'
            datos[qrg] = {
                'station': filas['Station:201'],
                'time': filas['Time(UTC):93'],
                'days': filas['Days:59'],
                'region': filas['ITU:49'],
                'language': filas['Lng:49'],
                'remarks': filas['Remarks:135']
            }

    with open(fichj, 'w') as fj:
        fj.write(json.dumps(datos, indent=4))


if __name__ == '__main__':
    tratar_csv(f_eibi_csv, f_eibi_json)
    # tratar_csv(f_hfcc_csv, f_hfcc_json)
    # tratar_csv(f_ncb_csv, f_ncb_json)
    escribir_bbdd()
