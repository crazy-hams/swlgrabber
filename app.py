# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

""" SWL Grabber """

__devteam__ = 'CrazyHams'
__date__ = "15/03/2020"

import json
import csv

# Variables
fichero_csv = 'sked-b19.csv'
fichero_json = 'salida.json'


def tratar_csv():
    """
    Esta función trata un CSV de entrada y genera un JSON de salida
    :param: None
    :return: a JSON (application/json)
    """

    datos = {}
    with open(fichero_csv) as fc_csv:
        f = csv.DictReader(fc_csv)

        for filas in f:
            qrg = filas['kHz:75']
            datos[qrg] = filas

    with open(fichero_json, 'w') as fj:
        fj.write(json.dumps(datos, indent=4))


if __name__ == '__main__':
    tratar_csv()


