from cycle.constants import Frame, SeatType, HandleType, Wheel

frame_dict = {Frame.CANTILEVER.name: 2000,
              Frame.ORDINARY.name: 1500,
              Frame.DIAMOND.name: 3000}

seat_dict = {SeatType.COMFORT.name: 2000,
             SeatType.ORDINARY.name: 1000}

handle_dict = {HandleType.ORDINARY.name: 1500,
               HandleType.DROP.name: 2000}

wheel_dict = {Wheel.TUBLESS.name: 2000,
              Wheel.WIHTTUBE.name: 1000}
