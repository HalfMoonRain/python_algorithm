# pip install pandas openpyxl cx_Oracle
import pandas as pd
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_21")

# 데이터베이스 연결 설정
dsn_tns = cx_Oracle.makedsn('호스트명', '포트', service_name='서비스명')
conn = cx_Oracle.connect(user='사용자명', password='비밀번호', dsn=dsn_tns)

# Excel 파일 읽기
file_name = '엑셀파일명'
xls = pd.ExcelFile(file_name)


def extract_component_info(cell_value):
    # ComponentInfo() 안의 문자열을 추출하는 함수
    # 주어진 셀 값에서 "ComponentInfo("로 시작하여 ")"로 끝나는 문자열을 추출
    start = cell_value.find("ComponentInfo(")
    if start == -1:
        return None
    # 괄호 카운트를 시작하여 쌍을 맞춤
    end = start
    counter = 1  # 이미 "("를 찾았으므로 1부터 시작
    for char in cell_value[start + len("ComponentInfo("):]:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter == 0:
                break
        end += 1
    return cell_value[start + len("ComponentInfo("):end].strip()


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
                data = {col.split('=')[0].strip(): col.split('=')[1].strip() for col in component_info_str.split(', ')
                        if '=' in col}
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