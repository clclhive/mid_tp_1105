"""
data_processor 모듈 테스트
"""

import unittest
import pandas as pd
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    """DataProcessor 클래스 테스트"""
    
    def setUp(self):
        """테스트 준비"""
        self.processor = DataProcessor()
        
        # 테스트용 샘플 데이터
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 2, 3, None],
            'B': [10, 20, 20, 30, 40],
            'C': ['a', 'b', 'b', 'c', 'd']
        })
    
    def test_clean_data(self):
        """데이터 정제 테스트"""
        cleaned = self.processor.clean_data(self.sample_data)
        
        # 결측치와 중복이 제거되어야 함
        self.assertEqual(len(cleaned), 3)
        self.assertFalse(cleaned.isnull().any().any())
    
    def test_filter_columns(self):
        """컬럼 필터링 테스트"""
        filtered = self.processor.filter_columns(self.sample_data, ['A', 'C'])
        
        self.assertEqual(list(filtered.columns), ['A', 'C'])
        self.assertEqual(len(filtered.columns), 2)


if __name__ == "__main__":
    unittest.main()
