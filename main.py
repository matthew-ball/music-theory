
tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def wrap(number, length): return number % length

# ERROR: only increases
def step(note, interval):
    position = tones.index(note)
    return tones[wrap(position + interval, len(tones))]

# TODO: step_increase()
# def step_increase(note, interval):
#     position = tones.index(note)
#     return tones[wrap(position + interval, len(tones))]

# TODO: step_decrease()
# def step_decrease(note, interval):
#     position = tones.index(note)
#     retuurn tones[wrap(position - interval, len(tones))]

def half_step(note): return step(note, 1)
def whole_step(note): return step(note, 2)
def whole_and_half_step(note): return step(note, 3)
# def double_step(note): return step(note, 4)

# --- scales ---
def create_scale(root, pattern):
    result = []
    result.append(root)
    for step in pattern:
        if step == 'W':
            result.append(whole_step(result[-1]))
        elif step == 'H':
            result.append(half_step(result[-1]))
        elif step == 'D':
            result.append(whole_and_half_step(result[-1]))
    return result

def major_scale(root): return create_scale(root, ['W', 'W', 'H', 'W', 'W', 'W', 'H'])
def minor_scale(root): return create_scale(root, ['W', 'H', 'W', 'W', 'H', 'W', 'W'])
def major_pentatonic_scale(root): return create_scale(root, ['W', 'W', 'D', 'W', 'D'])
def minor_pentatonic_scale(root): return create_scale(root, ['D', 'W', 'W', 'D', 'W'])

# --- chords ---
