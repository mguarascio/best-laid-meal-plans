import requests


def get_pins():
    r = requests.get('https://api.pinterest.com/v1/boards/kmg011/recipes/pins?fields=metadata,image,id,url,note&access_token=AQ5Y21USrQ0SlhHeN1cdqIh93AUXFI8-HMxRX51Dn2TR5WAtSwAAAAA')

    pins = []
    for rawpin in r.json()['data']:
        pin = {'id': rawpin['id'],
               'url': rawpin['url'],
               'note': rawpin['note'],
               'image': rawpin['image']['original']['url'],
               'title': get_recipe_name(rawpin)
               }
        pins.append(pin)

    return pins


def get_recipe_name(rawpin):
    name = ''
    if 'recipe' in rawpin['metadata']:
        name = rawpin['metadata']['recipe']['name']
    return name
