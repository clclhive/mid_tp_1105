"""
데이터 처리 모듈
Data Processor Module

공공데이터를 전처리하고 분석하는 기능을 제공합니다.
"""

import pandas as pd
from typing import List, Optional


class DataProcessor:
    """공공데이터를 처리하는 클래스"""
    
    def __init__(self):
        """DataProcessor 초기화"""
        pass
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        데이터를 정제합니다.
        
        Args:
            df: 원본 데이터프레임
        
        Returns:
            pd.DataFrame: 정제된 데이터프레임
        """
        # 결측치 제거
        df_cleaned = df.dropna()
        
        # 중복 제거
        df_cleaned = df_cleaned.drop_duplicates()
        
        return df_cleaned
    
    def filter_columns(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        필요한 컬럼만 선택합니다.
        
        Args:
            df: 데이터프레임
            columns: 선택할 컬럼 리스트
        
        Returns:
            pd.DataFrame: 컬럼이 선택된 데이터프레임
        """
        return df[columns]
    
    def aggregate_data(self, df: pd.DataFrame, group_by: str, 
                      agg_column: str, agg_func: str = "mean") -> pd.DataFrame:
        """
        데이터를 집계합니다.
        
        Args:
            df: 데이터프레임
            group_by: 그룹화할 컬럼
            agg_column: 집계할 컬럼
            agg_func: 집계 함수 ('mean', 'sum', 'count', 'min', 'max')
        
        Returns:
            pd.DataFrame: 집계된 데이터프레임
        """
        return df.groupby(group_by)[agg_column].agg(agg_func).reset_index()
