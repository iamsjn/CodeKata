from typing import List, Tuple, Set


def select_activity(activities: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    selected_activities = set()
    selected_activity_index = 0

    activities.sort(key=lambda x: x[1])
    selected_activities.add(activities[selected_activity_index])

    for activity_index in range(1, len(activities)):
        if activities[activity_index][0] >= activities[selected_activity_index][1]:
            selected_activities.add(activities[activity_index])
            selected_activity_index = activity_index

    return selected_activities


if __name__ == "__main__":
    activity_list = [(1, 4), (3, 5), (0, 6),
                    (5, 7), (3, 8), (5, 9),
                    (6, 10), (8, 11), (8, 12),
                    (2, 13), (12, 14)]
    print(select_activity(activities=activity_list))
