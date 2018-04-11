#!/usr/bin/env python
from argparse import ArgumentParser
import os.path
import psonic as ps


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


parser = ArgumentParser(prog="whistle.py",
                        description="Play a string of UAI")
parser.add_argument(dest="inputFile",
                    help="input file with UAI text", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()
with open(args.inputFile, "r") as f:
    text = f.read().lower()

accept = "auiáúíâûî"
notes = {"u": 65, # C#6
         "a": 68, # E6
         "i": 73} # A6
tempo = {"short": 0.200,
         "long": 0.500}
words = text.split(" ")
silence = 2
ps.use_synth(ps.SINE)
for word in words:
    for letter in word:
        if letter in accept:
            ps.play(notes[letter],
                    attack=0,
                    decay=0,
                    sustain_level=1,
                    sustain=tempo["short"],
                    release=0)

            ps.sleep(0.1)
    ps.sleep(1)
