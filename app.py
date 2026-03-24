#!/usr/bin/env python3
"""Detect and remove silent sections from media."""
import argparse, shutil, subprocess

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('output'); p.add_argument('--threshold',default='-35dB'); p.add_argument('--min-silence',type=float,default=0.5); p.add_argument('--dry-run',action='store_true')
    a=p.parse_args(); require('ffmpeg')
    af=f'silenceremove=stop_periods=-1:stop_duration={a.min_silence}:stop_threshold={a.threshold}'
    cmd=['ffmpeg','-y','-i',a.input,'-af',af,a.output]
    print(' '.join(cmd));
    if not a.dry_run: subprocess.check_call(cmd)
if __name__ == '__main__': main()
