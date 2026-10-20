#!/usr/bin/env python3
"""Gjør en CSV med tidsstemplede GPS-punkter om til en KML-fil for Google Earth.

Skrevet til en innlevering i device forensics der posisjonsdata var eksportert
fra en telefon som CSV. Hver rad blir et punkt med tidsstempelet som navn.

Bruk:
    python csv_to_kml.py locations.csv [-o locations.kml]
        [--time DateTime] [--lat LAT] [--lng LNG]
"""
import argparse
import csv
from xml.etree.ElementTree import Element, ElementTree, SubElement


def convert(csv_path, kml_path, time_col, lat_col, lng_col):
    kml = Element("kml", xmlns="http://www.opengis.net/kml/2.2")
    doc = SubElement(kml, "Document")
    SubElement(doc, "name").text = "Tidslinje over posisjoner fra CSV"

    count = 0
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ts, lat, lng = row[time_col], row[lat_col], row[lng_col]
            pm = SubElement(doc, "Placemark")
            SubElement(pm, "name").text = ts
            SubElement(pm, "description").text = f"Tidspunkt: {ts}\nBreddegrad: {lat}\nLengdegrad: {lng}"
            point = SubElement(pm, "Point")
            SubElement(point, "coordinates").text = f"{lng},{lat},0"  # KML vil ha lengdegrad,breddegrad
            count += 1

    ElementTree(kml).write(kml_path, encoding="utf-8", xml_declaration=True)
    return count


def main(argv=None):
    ap = argparse.ArgumentParser(description="CSV med GPS-punkter til KML")
    ap.add_argument("csv", help="CSV-fil som input")
    ap.add_argument("-o", "--out", default="locations.kml", help="KML-fil som skal lages")
    ap.add_argument("--time", default="DateTime", help="navn på kolonnen med tidspunkt")
    ap.add_argument("--lat", default="LAT", help="navn på kolonnen med breddegrad")
    ap.add_argument("--lng", default="LNG", help="navn på kolonnen med lengdegrad")
    a = ap.parse_args(argv)
    n = convert(a.csv, a.out, a.time, a.lat, a.lng)
    print(f"Skrev {n} punkter til {a.out}")


if __name__ == "__main__":
    main()
