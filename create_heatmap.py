import gmplot
import csv


def csv_to_list(spreadsheet):
    text = []
    with open(spreadsheet, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new = [row['Portal Name'], row['Lat/Lon']]
            reformatted = '\t'.join(new)
            text.append(reformatted)
    return text


def draw_map(portal_list, map_name="map.html"):
    lat_list = []
    lng_list = []
    name_list = []
    for line in portal_list:
        pair = line.split("\t")
        name_list.append(pair[0])
        lat, lng = pair[1].split(",")
        lat_list.append(float(lat))
        lng_list.append(float(lng))

    gmap = gmplot.GoogleMapPlotter(51.919396, 19.145208, 7)
    gmap.heatmap(lat_list, lng_list)

    gmap.draw(map_name)


draw_map(csv_to_list("IPST.csv"))
