"""LIB package"""
import sys
from pathlib import Path

path_test = Path(__file__).resolve().parents[1]
sys.path.append(str(path_test))
