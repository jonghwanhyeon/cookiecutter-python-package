import sys
from pathlib import Path

import pytest

tests_path = Path(__file__).parent.absolute()
sys.path.append(str(tests_path))
