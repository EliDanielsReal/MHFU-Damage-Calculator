
ELEMENT_COLOURS = {
    "FIRE"  : "red1",
    "WATER" : "steel_blue",
    "THUNDER" : "yellow1",
    "ICE": "blue1",
    "DRAGON" : "grey3",

    "POISON": "bright_magenta",
    "PARA": "yellow3",
    "SLEEP" : "red"

}

def raw_display(sharpness, raw_damage):
    return f'[italic green]({sharpness})[/italic green] [white]{int(raw_damage)} RAW [/white]'

def element_display(element_type, element_value):
    if element_type is None:
        return ''
    
    colour = ELEMENT_COLOURS[element_type]
    return f'[{colour}] {int(element_value)} {element_type} [/{colour}]'