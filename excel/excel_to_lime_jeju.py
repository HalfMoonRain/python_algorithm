import pandas as pd
import cx_Oracle
import datetime
import socket

# 엑셀 파일 경로
excel_file_path = 'test.xlsx'

# 처리할 시트 범위 설정 (예: 시트 2부터 시트 4까지)
start_sheet_index = 2  # Python은 0부터 인덱싱합니다.
end_sheet_index = 8

# 데이터베이스 연결
cursor = conn.cursor()

# 컬럼명 매칭 사전 (종료일자에 '29991231' 고정값, '코드_한의과'는 제외)
column_mapping = {
    '명칭': 'MEFE_HNM',
    '산정명칭': 'CMPT_NM',
    '단가': 'HSGR_MRTH_UNPR',
    '소정점수': 'RLVL_PNT',
    '수술여부': 'OP_YN',
    '적용개시일': 'APLY_STRT_DD',
    '코드_의·치과': 'MEFE_CD',
    # '코드_한의과'는 DB에 입력하지 않으므로 제외
}

# 현재 시간
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# 컴퓨터의 호스트 이름과 IP 주소 가져오기
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

xlsx = pd.ExcelFile(excel_file_path)
sheets_to_process = xlsx.sheet_names[start_sheet_index:end_sheet_index + 1]

for sheet_name in sheets_to_process:
    df = pd.read_excel(xlsx, sheet_name=sheet_name)

    for index, row in df.iterrows():
        # 종료일자에 고정값 '29991231' 설정
        # row['적용종료일자'] = '29991231'

        # 매칭된 컬럼명으로 데이터 준비 (코드_한의과 제외)
        values = {db_col: row[excel_col] for excel_col, db_col in column_mapping.items() if excel_col in row}
        values['APLY_STRT_DD'] = values['APLY_STRT_DD'].strftime("%Y%m%d") if isinstance(values['APLY_STRT_DD'], datetime.datetime) else values['APLY_STRT_DD'].replace('-', '')
        values['OP_YN'] = '9' if values['OP_YN'] == '수술' else '0' # 9 수술 0 비수술
        values['RGST_DT'] = current_time
        values['UPDT_DT'] = current_time
        values['RGST_IP'] = ip_address
        values['UPDT_IP'] = ip_address

        # 데이터 조회 및 삽입 로직 (unique_column과 your_table은 예시로 사용)
        # TODO: 실제 유니크 컬럼과 테이블 이름으로 변경해야 합니다.
        select_query = f"SELECT COUNT(*) FROM BIEDI001 WHERE MEFE_CD = '{values['MEFE_CD']}' "
        cursor.execute(select_query)
        result = cursor.fetchone()

        if result[0] == 0:  # 데이터가 없으면 삽입
            columns = ', '.join(values.keys())
            placeholders = ', '.join([f" '{col}' " for col in values.values()])
            placeholders = placeholders.replace("'nan'", "NULL")
            insert_query = f"INSERT INTO BIEDI001 ({columns}) VALUES ({placeholders})"
            cursor.execute(insert_query)
            print(f"Executed Query: {cursor.statement}")  # 사용된 쿼리문 출력

conn.commit()
cursor.close()
conn.close()
