# cnsmi

More compact version of `nvidia-smi` tool. Useful for monitoring GPUs in tmux.

To refresh on an interval, you can run it with watch command e.g. `watch ./cnsmi.py`

Can also output json with `--json`, and pprint with `--pprint`.

# Dependencies

- Python 3.7
- working `nvidia-smi` on `$PATH` or specified via `--nvidia-smi-path`

# Examples

```
$ cnsmi/cnsmi.py --nvidia-smi-path ./nvidia-smi
GeForce GTX 960|77C|72%
880MiB / 2002MiB|102W / 130W
GeForce GTX 960|81C|81%
612MiB / 2000MiB|122W / 130W

$ cnsmi/cnsmi.py --nvidia-smi-path ./nvidia-smi --json
{"cards": [{"name": "GeForce GTX 960", "bus": "00000000:06:00.0", "memory": "880MiB / 2002MiB", "utilization": "84%", "fan": "72%", "temp": "77C", "mode": "P2", "power": "102W / 130W"}, {"name": "GeForce GTX 960", "bus": "00000000:07:00.0", "memory": "612MiB / 2000MiB", "utilization": "67%", "fan": "81%", "temp": "81C", "mode": "P2", "power": "122W / 130W"}], "processes": [{"gpu": "0", "pid": "14269", "name": "python", "memory": "869MiB"}, {"gpu": "1", "pid": "14269", "name": "python", "memory": "601MiB"}], "time": "Tue Jun 4 23:41:18 2019", "driver_version": "418.67", "cuda_version": "10.1"}

$ cnsmi/cnsmi.py --nvidia-smi-path ./nvidia-smi --pprint
{'cards': [{'bus': '00000000:06:00.0',
            'fan': '72%',
            'memory': '880MiB / 2002MiB',
            'mode': 'P2',
            'name': 'GeForce GTX 960',
            'power': '102W / 130W',
            'temp': '77C',
            'utilization': '84%'},
           {'bus': '00000000:07:00.0',
            'fan': '81%',
            'memory': '612MiB / 2000MiB',
            'mode': 'P2',
            'name': 'GeForce GTX 960',
            'power': '122W / 130W',
            'temp': '81C',
            'utilization': '67%'}],
 'cuda_version': '10.1',
 'driver_version': '418.67',
 'processes': [{'gpu': '0',
                'memory': '869MiB',
                'name': 'python',
                'pid': '14269'},
               {'gpu': '1',
                'memory': '601MiB',
                'name': 'python',
                'pid': '14269'}],
 'time': 'Tue Jun 4 23:41:18 2019'}

```

# License

Licensed with a LICENSE file. MIT License. Author: Nemanja Milosevic (nmilosev@dmi.rs)
