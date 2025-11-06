"""
데이터 로더 모듈
Data Loader Module

공공데이터를 불러오고 처리하는 기능을 제공합니다.
"""

import pandas as pd
from pathlib import Path


class DataLoader:
    """공공데이터를 불러오는 클래스"""
    
    def __init__(self, data_dir: str = "data"):
        """
        DataLoader 초기화
        
        Args:
            data_dir: 데이터 디렉토리 경로
        """
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
        self.sample_dir = self.data_dir / "sample"
    
    def load_csv(self, filename: str, data_type: str = "raw") -> pd.DataFrame:
        """
        CSV 파일을 불러옵니다.
        
        Args:
            filename: 파일명
            data_type: 데이터 타입 ('raw', 'processed', 'sample')
        
        Returns:
            pd.DataFrame: 불러온 데이터프레임
        """
        if data_type == "raw":
            filepath = self.raw_dir / filename
        elif data_type == "processed":
            filepath = self.processed_dir / filename
        elif data_type == "sample":
            filepath = self.sample_dir / filename
        else:
            raise ValueError(f"Invalid data_type: {data_type}")
        
        return pd.read_csv(filepath)
    
    def save_csv(self, df: pd.DataFrame, filename: str, data_type: str = "processed"):
        """
        데이터프레임을 CSV 파일로 저장합니다.
        
        Args:
            df: 저장할 데이터프레임
            filename: 파일명
            data_type: 데이터 타입 ('raw', 'processed', 'sample')
        """
        if data_type == "raw":
            filepath = self.raw_dir / filename
        elif data_type == "processed":
            filepath = self.processed_dir / filename
        elif data_type == "sample":
            filepath = self.sample_dir / filename
        else:
            raise ValueError(f"Invalid data_type: {data_type}")
        
        # 디렉토리가 없으면 생성
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        df.to_csv(filepath, index=False)
