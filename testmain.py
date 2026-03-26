from sonarBins import sonarBins
import random

random.seed()
def move_servo(angle):
    pass
def read_ultrasonic():
    if scanner.current_angle > 150 and scanner.current_angle < 160:
        return random.randint(90,150)
    return random.randint(90,100)

def on_alert(angle):
    print("Alert at ", angle)

scanner = sonarBins(
    move=move_servo,          # required: move(angle)
    read=read_ultrasonic,     # required: returns distance or None
    alert=on_alert,           # required: alert(angle)
    bins=60,                  # default
    step=1,                   # default
    start_angle=0,            # default
    end_angle=180,            # default
    error_margin=0.15,        # default (15% change per reading)
    error_ratio=0.6,          # default (60% of readings must fail to call alert())
    debug=True               # default
)

scanner.initialize(3)
for x in range(100):
    print(scanner.sweep())