import simple_draw as sd


def smile(smile_center, colour):
    # Лицо
    center_position = sd.get_point(smile_center[0], smile_center[1])
    sd.circle(center_position, radius=200, color=colour, width=0)

    # Рот
    sd.line(start_point=sd.get_point(smile_center[0] - 120, smile_center[1] - 75),
            end_point=sd.get_point(smile_center[0] + 120, smile_center[1] - 75),
            color=(0, 0, 0), width=20)

    # Глаза
    sd.line(start_point=sd.get_point(smile_center[0] - 145, smile_center[1] + 50),
            end_point=sd.get_point(smile_center[0] - 55, smile_center[1] + 50),
            color=(0, 0, 0), width=15)

    sd.line(start_point=sd.get_point(smile_center[0] + 145, smile_center[1] + 50),
            end_point=sd.get_point(smile_center[0] + 55, smile_center[1] + 50),
            color=(0, 0, 0), width=15)

    # Shit happens
    sd.lines(point_list=[sd.get_point(smile_center[0] - 200, smile_center[1] - 210),
                         sd.get_point(smile_center[0] - 210, smile_center[1] - 210),
                         sd.get_point(smile_center[0] - 210, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 200, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 200, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 210, smile_center[1] - 230), ],
             color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 195, smile_center[1] - 210),
            end_point=sd.get_point(smile_center[0] - 195, smile_center[1] - 230), color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 195, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 185, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 185, smile_center[1] - 230)],
             color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 180, smile_center[1] - 220),
            end_point=sd.get_point(smile_center[0] - 180, smile_center[1] - 230),
            color=(255, 255, 255), width=2)
    sd.circle(center_position=sd.get_point(smile_center[0] - 179, smile_center[1] - 215), radius=2,
              color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 170, smile_center[1] - 210),
            end_point=sd.get_point(smile_center[0] - 170, smile_center[1] - 230),
            color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 175, smile_center[1] - 215),
            end_point=sd.get_point(smile_center[0] - 165, smile_center[1] - 215),
            color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 150, smile_center[1] - 210),
            end_point=sd.get_point(smile_center[0] - 150, smile_center[1] - 230), color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 150, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 140, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 140, smile_center[1] - 230)],
             color=(255, 255, 255), width=2)
    sd.square(left_bottom=sd.get_point(smile_center[0] - 135, smile_center[1] - 230),
              side=10, color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 125, smile_center[1] - 217),
            end_point=sd.get_point(smile_center[0] - 125, smile_center[1] - 231),
            color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 120, smile_center[1] - 240),
                         sd.get_point(smile_center[0] - 120, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 110, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 110, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 120, smile_center[1] - 230), ],
             color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 105, smile_center[1] - 240),
                         sd.get_point(smile_center[0] - 105, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 95, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 95, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 105, smile_center[1] - 230), ],
             color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 80, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 90, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 90, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 80, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 80, smile_center[1] - 225),
                         sd.get_point(smile_center[0] - 90, smile_center[1] - 225)],
             color=(255, 255, 255), width=2)
    sd.line(start_point=sd.get_point(smile_center[0] - 75, smile_center[1] - 218),
            end_point=sd.get_point(smile_center[0] - 75, smile_center[1] - 231), color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 75, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 65, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 65, smile_center[1] - 231), ],
             color=(255, 255, 255), width=2)
    sd.lines(point_list=[sd.get_point(smile_center[0] - 60, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 50, smile_center[1] - 230),
                         sd.get_point(smile_center[0] - 50, smile_center[1] - 225),
                         sd.get_point(smile_center[0] - 60, smile_center[1] - 225),
                         sd.get_point(smile_center[0] - 60, smile_center[1] - 220),
                         sd.get_point(smile_center[0] - 50, smile_center[1] - 220), ],
             color=(255, 255, 255), width=2)


smile(smile_center=(300, 300), colour=(255, 255, 0))
sd.pause()
