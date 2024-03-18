
SHARPNESS_MODIFIER = {
    'RED': {'attack': 0.5, 'element': 0.25}, 
    'ORANGE': {'attack': 0.75, 'element': 0.5}, 
    'YELLOW': {'attack': 1, 'element': 0.75}, 
    'GREEN': {'attack': 1.125, 'element': 1}, 
    'BLUE': {'attack': 1.25, 'element': 1.0625}, 
    'WHITE': {'attack': 1.3, 'element': 1.125}, 'PURPLE': {'attack': 1.5, 'element': 1.2}
    }

def calculate_raw(weapon_class, raw_attack, raw_element, sharpness):

    true_raw = calculate_true_raw(weapon_class, raw_attack)

    true_element = calculate_true_element(weapon_class, raw_element)

    true_raw, true_element = apply_sharpness(sharpness, true_raw, true_element)

    return true_raw, true_element


def calculate_true_raw(weapon_class, raw_attack):

    if weapon_class in ["LS", "longsword", "GS", "great-sword"]:
        return raw_attack / 4.8
    
    elif weapon_class in ["SNS", "sword-and-shield", "DB", "dual-blades"]:
        return raw_attack / 1.4
    
    elif weapon_class in ["HAM", "hammer", "HH", "hunting-horn"]:
        return raw_attack / 5.2

    elif weapon_class in ["LN", "lance", "GL", "gun-lance"]:
        return raw_attack / 2.3

def calculate_true_element(weapon_class, raw_element):
    if weapon_class in ["DB", "dual-blades"]:
        return raw_element / 10 * 0.7
    
    else:
        return raw_element / 10
    

def apply_sharpness(sharpness, raw_attack, raw_element):

    return (
        raw_attack * SHARPNESS_MODIFIER[sharpness]["attack"], 
        raw_element *SHARPNESS_MODIFIER[sharpness]["element"]
        )
