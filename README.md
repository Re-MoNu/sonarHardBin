# sonarBins

This python module is meant to be used in conjuction with a sweeping ultrasonic module attached to a stepper motor (or any sort of module that may move to a set angle). It is meant to be used in a personal project, not to be deployed elsewhere.

---

## Requirements
- A function to move the sensor to an angle (degrees)
- A function to read distance (cm) or return `None` if invalid
- A function to call after a deviation in environment

---

## Create instance

```python
from sonarBins import sonarBins

scanner = sonarBins(
    move=move_servo,          # required: move(angle)
    read=read_ultrasonic,     # required: returns distance or None
    alert=on_alert,           # required: alert(angle)
    bins=60,                  # default
    step=2,                   # default
    start_angle=0,            # default
    end_angle=180,            # default
    error_margin=0.15,        # default (15% change per reading)
    error_ratio=0.6,          # default (60% of readings must fail to call alert())
    debug=False               # default
)
```

---

## Parameters

| Name | Description | Default |
|------|-------------|--------|
| `bins` | number of angular bins | 60 |
| `step` | sweep step size (deg) | 2 |
| `start_angle` | sweep start | 0 |
| `end_angle` | sweep end | 180 |
| `error_margin` | per-reading % change threshold | 0.15 |
| `error_ratio` | % of bad readings to trigger | 0.6 |
| `debug` | print debug info on trigger | False |

---

## Functions

### `initialize(sweeps=N)`
Builds baseline by sweeping forward and backward.

Example:
```python
scanner.initialize(sweeps=3)
```

- collects readings into bins
- stores median per bin in `self.baseline`

---

### `sweep()`
Performs one directional sweep.

example:
```python
triggered = scanner.sweep()
```

Returns:
- `True` → alert triggered
- `False` → no trigger

Behavior:
- collects readings per bin during sweep
- evaluates bin after leaving it
- calls `alert(angle)` on trigger
- stops immediately on trigger
- flips direction after full sweep

---

## Internal behavior (for tuning)

Per bin:

```python
abs(value - baseline) / baseline
```

- if above `error_margin` → counts as error
- if `error_count / total >= error_ratio` → triggers

---

## Notes

- `step` should be ≤ bin width (`(end-start)/bins`) or bins may be skipped
- baseline auto-adjusts slowly during non-triggered bins
- this module is a fast trigger layer (not precision mapping)
