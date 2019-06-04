#!/usr/bin/env python3
import os
from pprint import pprint
import json
import sys

"""
More compact version of nvidia-smi tool. Useful for monitoring GPUs in tmux.

To refresh on an interval, you can run it with watch command e.g. "watch ./cnsmi.py"

Can also output json with --json, and pprint with --pprint.

"""

NVIDIA_SMI_PATH = ('nvidia-smi' if '--nvidia-smi-path' not in sys.argv 
    else sys.argv[sys.argv.index('--nvidia-smi-path') + 1])


def handle_gpu_info(l):
    # 81%   81C    P2   122W / 130W
    # fan, temp, mode, power
    l = l.split()
    return l[0], l[1], l[2], ' '.join(l[3:]) 


def handle_process(l):
    # |    0     14269      C   python                                       869MiB |
    l = l.split()
    return { 'gpu': l[1], 'pid': l[2], 'name': l[4], 'memory': l[5] }


def clean(n):
    return (n.replace('Off', '').replace('On', '')
             .replace(' 1 ', '').replace(' 0 ', '')
             .replace('Default', '').replace('  ', ' ')
             .rstrip().lstrip())
   

def compact_print(data):
    for card in data['cards']:
        print(card['name'], card['temp'], card['fan'], sep='|')
        print(card['memory'], card['power'], sep='|')


def main():
    output = os.popen(NVIDIA_SMI_PATH).read().split('\n')

    data = { 'cards': [], 'processes': [] }

    for line_number, line in enumerate(output):
        if line_number == 0:
            data['time'] = clean(line)
        elif 'NVIDIA-SMI' in line:
            line = line.split()
            data['driver_version'] = line[line.index('Driver') + 2]
            data['cuda_version'] = line[line.index('CUDA') + 2]
        elif '%' in line:
            line = line.split('|')
            prev_line = output[line_number - 1].split('|')

            card_data = {}
            card_data['name'] = clean(prev_line[1])
            card_data['bus'] = clean(prev_line[2])
            card_data['memory'] = clean(line[2])
            card_data['utilization'] = clean(line[3])
        
            fan, temp, mode, power = handle_gpu_info(line[1])
            card_data['fan'] = fan
            card_data['temp'] = temp
            card_data['mode'] = mode
            card_data['power'] = power

            data['cards'].append(card_data)
        elif 'Processes' in line:
            i = line_number + 3
            while '+-' not in output[i]:
                data['processes'].append(handle_process(output[i]))
                i += 1

    if '--json' in sys.argv:
        print(json.dumps(data))
    elif '--pprint' in sys.argv:
        pprint(data)
    else:
        compact_print(data)


if __name__ == '__main__':
    main()
