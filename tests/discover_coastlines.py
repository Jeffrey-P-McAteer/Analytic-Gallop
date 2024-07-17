
# This script scans an XYZ tile server's most-detailed layer (z=13)
# for places where dark pixels meet light pixels.
# It takes these locations and plots them in a database,
# and displays the database contents as a ???

import analytic_gallop

format_url = 'https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/13/{y}/{x}'

def url_for(x, y):
  return format_url.format(x=x, y=y)


# TODO do something useful with format_url, transforming into ???




