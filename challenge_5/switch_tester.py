from functools import partial

damage_type = {'FRONT END': 49,
               'MECHANICAL': 2,
               'MINOR DENT/SCRATCHES': 3,
               'BIOHAZARD/CHEMICAL': 1,
               'STRIPPED': 1,
               'WATER/FLOOD': 2,
               'ALL OVER': 10,
               'SIDE': 14,
               'UNDERCARRIAGE': 2,
               'REAR END': 6,
               'VANDALISM': 1,
               'ROLLOVER': 7,
               'NORMAL WEAR': 2}


exclude_type = {'REAR END', 'FRONT END', 'MINOR DENT/SCRATCHES', 'UNDERCARRIAGE'}

misc_type = {x: damage_type[x] for x in damage_type
                if x not in exclude_type}

def rear_one(damage_type_disc):
    return f"REAR END: {damage_type_disc['REAR END']}"

def front_end(damage_type_disc):
    return f"FRONT END: {damage_type_disc['FRONT END']}"

def minor_dent_scratches(damage_type_disc):
    return f"MINOR DENT/SCRATCHES: {damage_type_disc['MINOR DENT/SCRATCHES']}"

def undercarriage(damage_type_disc):
    return f"UNDERCARRIAGE: {damage_type_disc['UNDERCARRIAGE']}"

def default(misc_type_disc):
    return f"MISC: {misc_type_disc}"


def count_type(argument, damage_type_disc):
    switcher = {
        1: partial(rear_one, damage_type_disc),
        2: partial(front_end, damage_type_disc),
        3: partial(minor_dent_scratches, damage_type_disc),
        4: partial(undercarriage,damage_type_disc),
        5: partial(default,damage_type_disc)
    }

    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: default(damage_type_disc))
    print(func())

count_type(1, damage_type)
count_type(2, damage_type)
count_type(3, damage_type)
count_type(4, damage_type)
count_type(5, misc_type)