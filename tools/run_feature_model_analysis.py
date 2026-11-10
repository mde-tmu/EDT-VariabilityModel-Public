#!/usr/bin/env python3
"""Run the SERP4IoT scenarios through FeatureIDE's actual Java library."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugins', type=Path, default=Path(os.environ.get(
        'FEATUREIDE_PLUGINS', '/Applications/Eclipse.app/Contents/Eclipse/plugins')))
    args = parser.parse_args()
    required = args.plugins / 'de.ovgu.featureide.fm.core_3.12.0.202603112104.jar'
    if not required.is_file():
        parser.error('Set --plugins to the Eclipse plugins directory containing FeatureIDE 3.12.0.202603112104.')
    for executable in ('java', 'javac'):
        if not shutil.which(executable):
            parser.error(f'{executable} is required (tested with Java 21).')
    classpath = str(args.plugins / '*')
    with tempfile.TemporaryDirectory(prefix='dt-featureide-') as build:
        subprocess.run(['javac', '-proc:none', '-sourcepath', '', '-cp', classpath,
                        '-d', build, str(root / 'tools/FeatureModelAnalysis.java')], check=True)
        subprocess.run(['java', '-cp', build + os.pathsep + classpath, 'FeatureModelAnalysis',
                        str(root / 'DT-Builder-VariabilityModel/FeatureModelDT_v2/model.xml'),
                        str(root / 'evidence/scenarios.tsv'),
                        str(root / 'evidence/analysis.json'),
                        str(root / 'DT-Builder-VariabilityModel/FeatureModelDT_v2/configs')], check=True)


if __name__ == '__main__':
    main()
