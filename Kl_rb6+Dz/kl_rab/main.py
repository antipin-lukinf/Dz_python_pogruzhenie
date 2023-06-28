import zd_2
import sys

init_numbers = list(map(int, [i for i in sys.argv][1:]))

zd_2.gues_f(*(init_numbers))