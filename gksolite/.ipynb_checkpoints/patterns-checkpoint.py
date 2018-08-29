import random 

def pad(literal):
    if not literal:
        return "  \n  "
    lines = ['', *literal.splitlines(), '']
    width = max(len(line) for line in lines)
    return '\n'.join(' ' + line.ljust(width) + ' ' for line in lines)


def create_random_literal():
    number_lines = random.randint(1, 10)
    number_columns = random.randint(1, 10)
    
    literal =""
    for line in range(0, number_lines):
        col_str = ""
        for col in range(0, number_columns):
            rand = random.randint(0,1)
            if rand == 0:
                col_str+="#"
            else:
                col_str+=" "
        literal += col_str.rstrip()+"\n"
    return literal

BLOCK = pad("""\
##
##
""")

BLINKER = pad("""\

###

""")

BLINKER3 = pad("""\
     #
###  # ###
     #
""")

PULSAR = pad("""\
  ###

#    #
#    #
#    #
  ###
""")

PENTADECATHLON = pad("""\
  #  #    # #
###  ###### ###
  #  #    # #
""")

PINWHEEL = pad("""\
 ####
#  # #
##   #
# #  #
#    #
 ####
""")

GLIDER = pad("""\
 #
  #
###
""")

DIEHARD = pad("""\
      #
##
 #   ###
""")

GLIDER_GUN = pad("""\
                        #
                      # #
            ##      ##            ##
           #   #    ##            ##
##        #     #   ##
##        #   # ##    # #
          #     #       #
           #   #
            ##
""")

PENTOMINO = pad("""\
 ##
##
 #
""")

BASELINE = pad("""\
######## #####   ###      ####### #####
""")

RANDOM = pad(create_random_literal())

PATTERNS = [
    'BLOCK', 'BLINKER', 'BLINKER3', 'PULSAR', 'PENTADECATHLON', 'PINWHEEL', 'GLIDER', 'DIEHARD', 'GLIDER_GUN',
    'PENTOMINO', 'RANDOM'
]

__all__ = PATTERNS[:]


print (create_random_literal())