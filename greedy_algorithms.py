timetable = {
    'paint': {
        'start': '9:00',
        'end': '10:00'
    },
    'english': {
        'start': '9:30',
        'end': '10:30'
    },
    'math': {
        'start': '10:00',
        'end': '11:00'
    },
    'info': {
        'start': '10:30',
        'end': '11:30'
    },
    'music': {
        'start': '11:00',
        'end': '12:00'
    }
}


def scheduling(table: dict) -> dict:
    """
    Поиск оптимального расписания занятий с использованием жадных алгоритмов.

    :param table: Словарь с возможными занятиями.
    :return: Словарь с готовым расписанием.
    """
    timetable_new = {}
    processed = []
    start = '9:00'
    for lesson, time in table.items():
        if lesson not in processed:
            if time['start'] == start:
                timetable_new[lesson] = time
                start = time['end']
                processed.append(lesson)
    return timetable_new


# print(scheduling(timetable))

stations_data = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}
states_needed_data = {'wa', 'mt', 'id', 'or', 'nv', 'ut', 'ca', 'az'}


def find_optimal_set_station(stations: dict, states_needed: set) -> set:
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = {}
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


print(find_optimal_set_station(stations_data, states_needed_data))
