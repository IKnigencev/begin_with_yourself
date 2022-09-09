import folium

from .models import IdeaModel


DEFAULT_JS = [
    ('leaflet',
     'https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js'),
    ('jquery',
     'https://code.jquery.com/jquery-1.12.4.min.js'),
    ('bootstrap',
     'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js'),
    ('awesome_markers',
     'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js'),  # noqa
    ]

DEFAULT_CSS = [
    ('leaflet_css',
     'https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css'),
    ('bootstrap_css',
     'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css'),
    ('bootstrap_theme_css',
     'https://code.jquery.com/jquery-1.12.4.min.js'),
    ('awesome_markers_css',
     'https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css'),
    ]


COLOR_DICT = {
    'ПОД': 'gray',
    'ДВО': 'red',
    'РАЙ': 'blue',
    'ГОР': 'black',
    'ОБЛ': 'green',
    'СТР': 'white'
}


def generate_map() -> None:

    ideas = IdeaModel.objects.select_related('author').all()

    map = folium.Map(
        location=[56.828446, 60.637575],
        zoom_start=11.5,
        tiles="CartoDB dark_matter")
    map.default_css = DEFAULT_CSS
    map.default_js = DEFAULT_JS

    for i in range(len(ideas)):
        color = COLOR_DICT[ideas[i].scale]
        folium.Marker(
            location=[ideas[i].coordinate_x, ideas[i].coordinate_y],
            popup=ideas[i].text[:10],
            fill_color=color,
            color=color,
            radius=9,
            fill_opacity=0.9
        ).add_to(map)

    map.save('templates/includes/mapFolium.html')
