"""
data_loader 모듈 테스트
"""

import unittest
import pandas as pd
from pathlib import Path
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    """DataLoader 클래스 테스트"""
    
    def setUp(self):
        """테스트 준비"""
        self.loader = DataLoader(data_dir="data")
    
    def test_init(self):
        """초기화 테스트"""
        self.assertIsInstance(self.loader.data_dir, Path)
        self.assertEqual(self.loader.data_dir.name, "data")
    
    def test_data_dirs(self):
        """데이터 디렉토리 경로 테스트"""
        self.assertEqual(self.loader.raw_dir.name, "raw")
        self.assertEqual(self.loader.processed_dir.name, "processed")
        self.assertEqual(self.loader.sample_dir.name, "sample")


if __name__ == "__main__":
    unittest.main()
