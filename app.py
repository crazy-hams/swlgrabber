# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" SWL Grabber """

__devteam__ = 'CrazyHams'
__date__ = "15/03/2020"

import json
import csv
import re

# Ficheros de entrada en formato CSV
f_eibi_csv = 'sked-b19.csv'
f_hfcc_csv = ''
f_ncb_csv = ''

# Fichero de salida en formato JSON
f_eibi_json = 'eibi.json'
f_hfcc_json = 'hfcc.json'
f_ncb_json = 'ncb.json'

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']


def escribir_bbdd():
    """
    Esta función escribe un JSON de entrada en una base de datos relacional
    :param: a JSON (application/json)
    :return: a relational database recordset
    """
    pass


def tratar_csv(fichc, fichj, delim):
    """
    Esta función trata un CSV de entrada y genera un JSON de salida
    :param: a CSV (application/text)
    :return: a JSON (application/json)
    """

    with open(fichc, encoding='utf-8') as fc:
        f = csv.DictReader(fc, delimiter=delim)
        datos = {}
        i = 1

        for filas in f:

            # ------------------------------------------------------------------------------------

            qrg = filas['kHz:75']
            days = filas['Days:59']
            language = filas['Lng:49']
            station = filas['Station:201']
            time = filas['Time(UTC):93']
            region = filas['ITU:49']
            remarks = filas['Remarks:135']

            if language is '':
                language = 'n/a'
            if remarks is '':
                remarks = 'n/a'

            # ------------------------------------------------------------------------------------

            try:
                if len(days) == 0:
                    days = '1234567'
                else:
                    # Funciones para determinar el índice numérico del día inicial y
                    # final de la transmisión de radio
                    d_sta = week.index(re.findall(r'^[\w]{2}', days).pop()) + 1
                    d_sto = week.index(re.findall(r'[\w]{2}$', days).pop()) + 1

                    # Funciones para determinar si una transmisión de radio sucede
                    # un dia o un rango de días
                    d_sep1 = re.findall(r'[-,]', days)
                    d_sep2 = re.findall(r'[-,]', days)
                    d_sep3 = re.findall(r'[-,]', days)

                    if not d_sep1:
                        if d_sta == d_sto:
                            days = '1234567'
                        elif d_sta > d_sto:
                            days = '{}{}'.format(d_sto, d_sta)
                        else:
                            days = '{}{}'.format(d_sta, d_sto)
                    elif d_sep2.pop() == '-':
                        if d_sta == d_sto:
                            days = '1234567'
                        elif d_sta > d_sto:
                            days = ''
                            j = 1
                            while j <= d_sto:
                                days = days + str(j)
                                j += 1
                            while d_sta <= 7:
                                days = days + str(d_sta)
                                d_sta += 1
                        else:
                            days = ''
                            while d_sta <= d_sto:
                                days = days + str(d_sta)
                                d_sta += 1
                    elif d_sep3.pop() == ',':
                        if d_sta == d_sto:
                            days = '1234567'
                        elif d_sta > d_sto:
                            days = '{}{}'.format(d_sto, d_sta)
                        else:
                            days = '{}{}'.format(d_sta, d_sto)
                    else:
                        days = 'n/a'
            except:
                pass

            # ------------------------------------------------------------------------------------

            datos[i] = {
                'qrg': qrg,
                'station': station,
                'time': time,
                'days': days,
                'region': region,
                'language': language,
                'remarks': remarks
            }

            i += 1

    with open(fichj, 'w') as fj:
        fj.write(json.dumps(datos, sort_keys=False, indent=4))


if __name__ == '__main__':
    tratar_csv(f_eibi_csv, f_eibi_json, ';')
    # tratar_csv(f_hfcc_csv, f_hfcc_json, ',')
    # tratar_csv(f_ncb_csv, f_ncb_json, '|')
    escribir_bbdd()
