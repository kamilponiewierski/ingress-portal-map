import gmplot


def coord(latlng):
    return latlng.split(',')


lat_list = []
lng_list = []
name_list = []
with open('portals.txt', encoding='utf-8') as f:
    for line in f:
        pair = line.split("\t")
        name_list.append(pair[0])
        lat, lng = coord(pair[1])
        lat_list.append(float(lat))
        lng_list.append(float(lng))

# gmap = gmplot.GoogleMapPlotter(51.919396, 19.145208, 7, apikey="AIzaSyCHHiyHAmqMBzE9A1LV3sLTq9T_P5i4pBU")
gmap = gmplot.GoogleMapPlotter(51.919396, 19.145208, 7)
gmap.heatmap(lat_list, lng_list)


# punkty
# gmap.scatter(lat_list, lng_list, '#3B0B39', size=40, marker=False)

# for i in range(0, len(lat_list)):
#     gmap.marker(lat_list[i], lng_list[i], title=name_list[i])


gmap.draw("map.html")
