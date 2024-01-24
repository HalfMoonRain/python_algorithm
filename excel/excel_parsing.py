# pip install pandas openpyxl cx_Oracle
import re

import pandas as pd
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_21")

# 데이터베이스 연결 설정
dsn_tns = cx_Oracle.makedsn('호스트명', '포트', service_name='서비스명')
conn = cx_Oracle.connect(user='사용자명', password='비밀번호', dsn=dsn_tns)


# Excel 파일 읽기
file_name = '엑셀'
xls = pd.ExcelFile(file_name)


# ComponentInfo 문자열 추출 함수
def extract_component_info(cell_value):
    return cell_value[15:-1]


# 알려진 키 목록
known_keys = [
    'SHEETCODE', 'DCCODE', 'SORTSEQ', 'ENABLEFLAG', 'TEXT', 'ATTRIBUTE',
    'LOCATIONX', 'LOCATIONY', 'WIDTH', 'HEIGHT', 'FONTNAME', 'FONTSIZE',
    'BOLD', 'FORECOLOR', 'BACKCOLOR', 'GROUPCODE', 'EDITABLE', 'RESIZEABLE',
    'TEXTALIGN', 'TABSTOP', 'TABINDEX', 'PAGENUMBER'
]

# 알려진 키를 기반으로 문자열 파싱
def parse_component_info(component_info_str, known_keys):
    data = {}
    # 알려진 키들의 패턴을 만듭니다. 예: (?<=SHEETCODE=|DCCODE=|...)([^,]+)
    pattern = '|'.join([f'(?<={key}=)' for key in known_keys])
    # 찾은 값을 저장할 임시 변수입니다.
    temp_values = re.split(pattern, component_info_str)[1:]  # 첫 번째 빈 문자열은 무시합니다.

    # 키와 임시 값들을 매핑합니다.
    for key, value in zip(known_keys, temp_values):
        # 다음 키를 찾기 전까지의 값, 또는 문자열의 끝까지를 추출합니다.
        end = value.find(', ' + known_keys[known_keys.index(key) + 1] + '=') if known_keys.index(key) + 1 < len(known_keys) else len(value)
        # 추출된 값을 데이터에 추가합니다.
        data[key] = value[:end].strip()

    return data


# 각 시트 처리
for sheet_name in xls.sheet_names:
    # 시트 데이터 로드
    df = pd.read_excel(xls, sheet_name)

    # 각 행을 반복 처리
    for index, row in df.iterrows():
        # 각 셀을 순회하며 ComponentInfo 데이터 추출
        for cell in row:
            if pd.isnull(cell):
                continue  # NaN 값은 건너뜀
            component_info_str = extract_component_info(str(cell))
            if component_info_str:
                # 컬럼명과 값 매핑
                data = parse_component_info(component_info_str, known_keys)

                columns, values = zip(*data.items())

                query = f"INSERT INTO EMR_MST_SHEET_DATACOMPONENT ({', '.join(columns)}) VALUES ({', '.join([':' + str(i + 1) for i in range(len(values))])})"

                try:
                    # 위치 지정자를 실제 값으로 대체
                    formatted_query = query
                    for i, value in enumerate(values):
                        formatted_query = formatted_query.replace(f":{i + 1}", f"'{value}'")

                    print("Formatted Query:", formatted_query)
                    # 데이터베이스에 삽입
                    cursor = conn.cursor()
                    cursor.execute(query, values)
                    conn.commit()
                except cx_Oracle.DatabaseError as e:
                    print(f"An error occurred: {e}")
                    conn.rollback()
                    break  # 또는 continue, 오류에 따라 적절히 처리

# 데이터베이스 연결 종료
conn.close()
print('JOB Done')

# def extract_component_info(cell_value):
#     return cell_value[15:-1]
#
#
#
# # 필드 파싱
# def parse_component_info(component_info_str):
#     # 알려진 모든 필드 키의 리스트
#     known_keys = ['SHEETCODE', 'DCCODE', 'SORTSEQ', 'ENABLEFLAG', 'TEXT', 'ATTRIBUTE', 'LOCATIONX', 'LOCATIONY',
#                   'WIDTH', 'HEIGHT', 'FONTNAME', 'FONTSIZE', 'BOLD', 'FORECOLOR', 'BACKCOLOR', 'GROUPCODE', 'EDITABLE',
#                   'RESIZEABLE', 'TEXTALIGN', 'TABSTOP', 'TABINDEX', 'PAGENUMBER']
#     data = {}
#     buffer = ""
#     current_key = None
#
#     # 문자열을 한 글자씩 순회합니다.
#     for char in component_info_str:
#         buffer += char
#         # 현재 버퍼가 알려진 키 중 하나로 시작하는지 확인합니다.
#         if any(buffer.strip().endswith(key + '=') for key in known_keys):
#             if current_key:
#                 # 이전 값을 저장합니다. 마지막 쉼표와 키를 제거합니다.
#                 data[current_key] = buffer.rsplit(', ', 1)[0].strip()
#             # 새로운 키를 추출하고 버퍼를 리셋합니다.
#             current_key, buffer = buffer.strip().rsplit('=', 1)
#         elif char == ',':
#             # 쉼표가 나타나면 버퍼를 잠시 지웁니다.
#             buffer = buffer.rsplit(',', 1)[-1]
#
#     # 마지막 키-값 쌍을 저장합니다.
#     if current_key and buffer:
#         data[current_key] = buffer.strip()
#
#     return data
#
#
# # 각 시트 처리
# for sheet_name in xls.sheet_names:
#     # 시트 데이터 로드
#     df = pd.read_excel(xls, sheet_name)
#
#     # 각 행을 반복 처리
#     for index, row in df.iterrows():
#         # 각 셀을 순회하며 ComponentInfo 데이터 추출
#         for cell in row:
#             if pd.isnull(cell):
#                 continue  # NaN 값은 건너뜀
#             component_info_str = extract_component_info(str(cell))
#             if component_info_str:
#                 # 컬럼명과 값 매핑
#                 data = parse_component_info(component_info_str)
#
#                 columns, values = zip(*data.items())
#
#                 query = f"INSERT INTO EMR_MST_SHEET_DATACOMPONENT ({', '.join(columns)}) VALUES ({', '.join([':' + str(i + 1) for i in range(len(values))])})"
#
#                 try:
#                     # 위치 지정자를 실제 값으로 대체
#                     formatted_query = query
#                     for i, value in enumerate(values):
#                         formatted_query = formatted_query.replace(f":{i + 1}", f"'{value}'")
#
#                     print("Formatted Query:", formatted_query)
#                     # 데이터베이스에 삽입
#                     cursor = conn.cursor()
#                     cursor.execute(query, values)
#                     conn.commit()
#                 except cx_Oracle.DatabaseError as e:
#                     print(f"An error occurred: {e}")
#                     conn.rollback()
#                     break  # 또는 continue, 오류에 따라 적절히 처리
#
# # 데이터베이스 연결 종료
# conn.close()
# print('JOB Done')

# def extract_component_info(row):
#     """
#     ComponentInfo() 안의 문자열을 추출하는 함수
#     """
#     start = row.find("ComponentInfo(")
#     if start == -1:
#         return None
#
#     end = start
#     counter = 0
#     for char in row[start:]:
#         if char == '(':
#             counter += 1
#         elif char == ')':
#             counter -= 1
#             if counter == 0:
#                 break
#         end += 1
#
#     return row[start + 14:end]  # 'ComponentInfo(' 길이를 더해 시작점 이동
#
# # 트랜잭션
# try:
#     # 각 시트 처리
#     for sheet_name in xls.sheet_names:
#         # 시트 데이터 로드
#         df = pd.read_excel(xls, sheet_name)
#
#         # 각 행을 반복 처리
#         for index, row in df.iterrows():
#             # ComponentInfo() 부분 추출
#             component_info_str = extract_component_info(str(row))
#             if component_info_str:
#                 # 컬럼명과 값 매핑
#                 data = {col.split('=')[0].strip(): col.split('=')[1].strip() for col in component_info_str.split(', ') if
#                         '=' in col}
#
#                 # 컬럼명과 값 목록 분리
#                 columns, values = zip(*data.items())
#
#                 # SQL 쿼리 생성
#                 query = f"INSERT INTO EMR_MST_SHEET_DATACOMPONENT ({', '.join(columns)}) VALUES ({', '.join([':' + str(i + 1) for i in range(len(values))])})"
#
#                 # SQL 쿼리 출력
#                 print("Executing SQL Query:", query)
#
#                 # 위치 지정자를 실제 값으로 대체
#                 formatted_query = query
#                 for i, value in enumerate(values):
#                     formatted_query = formatted_query.replace(f":{i + 1}", f"'{value}'")
#
#                 print("Formatted Query:", formatted_query)
#
#                 # 데이터베이스에 삽입
#                 cursor = conn.cursor()
#                 cursor.execute(query, values)
#                 conn.commit()
#
# except cx_Oracle.DatabaseError as e:
#             print(f"An error occurred: {e}")
#             conn.rollback()  # 오류 발생 시 롤백
# # 데이터베이스 연결 종료
#
# conn.close()