"""
공공데이터 중간 프로젝트 메인 스크립트
Public Data Mid-term Project Main Script

시작일: 2025년 11월 5일 (251105)
"""

from src.data_loader import DataLoader
from src.data_processor import DataProcessor


def main():
    """메인 함수"""
    print("=" * 50)
    print("공공데이터 중간 프로젝트")
    print("Public Data Mid-term Project")
    print("시작일: 2025년 11월 5일 (251105)")
    print("=" * 50)
    
    # DataLoader 초기화
    loader = DataLoader(data_dir="data")
    print("\n✓ DataLoader 초기화 완료")
    
    # DataProcessor 초기화
    processor = DataProcessor()
    print("✓ DataProcessor 초기화 완료")
    
    print("\n프로젝트가 준비되었습니다!")
    print("\n사용 가능한 모듈:")
    print("  - DataLoader: 데이터 로드 및 저장")
    print("  - DataProcessor: 데이터 전처리 및 분석")
    
    print("\n자세한 사용법은 README.md를 참조하세요.")


if __name__ == "__main__":
    main()
