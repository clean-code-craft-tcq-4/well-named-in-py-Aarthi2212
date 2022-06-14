from .constants import MAJOR_COLORS, MINOR_COLORS

def get_pair_number(major_color, minor_color):
  try:
    major_color_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major Color index out of range')
  try:
    minor_color_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor Color index out of range')
  return major_color_index * len(MINOR_COLORS) + minor_color_index + 1

def get_color(pair_number):
  zero_based_pair_number = pair_number - 1
  major_color_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_color_index >= len(MAJOR_COLORS):
    raise Exception('Major Color index out of range')
  minor_color_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_color_index >= len(MINOR_COLORS):
    raise Exception('Minor Color index out of range')
  return MAJOR_COLORS[major_color_index], MINOR_COLORS[minor_color_index]

def print_color_coding_manual():
  manual_format = '{:<{width}} | {:<{width}} | {:<{width}}'
  print(manual_format.format("Pair number", "Major color", "Minor color", width=11))
  total_pairs = 25
  for pair_number in range(1, total_pairs+1):
    major_color, minor_color = get_color(pair_number)
    print(manual_format.format(pair_number, major_color, minor_color, width=11))