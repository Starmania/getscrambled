import os
import glob

# Script file path
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
ARTIFACTS_PATH = os.path.join(SCRIPT_PATH, 'artifacts')


def _glob_ignore_keep():
    files = glob.glob(os.path.join(ARTIFACTS_PATH, '*'))
    if '.gitkeep' in files:
        files.remove('.gitkeep')
    return files


def _clean_artifacts():
    os.makedirs(ARTIFACTS_PATH, exist_ok=True)

    files = _glob_ignore_keep()
    for f in files:
        os.remove(f)

    with open(os.path.join(ARTIFACTS_PATH, '.gitkeep'), 'w') as f:
        pass


if not os.path.exists(ARTIFACTS_PATH) or len(_glob_ignore_keep()) != 0:
    _clean_artifacts()
