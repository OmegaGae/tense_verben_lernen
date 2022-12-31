""" Scripts for VerbenLernen App as helper"""
import sys
from pathlib import Path

path_test = Path(__file__).resolve().parents[1]
sys.path.append(str(path_test))

from scripts.file_cleaner import clean_file

__all__ = [clean_file]
