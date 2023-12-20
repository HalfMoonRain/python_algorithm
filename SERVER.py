import socket

# 서버 설정
server_port = 6000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', server_port))
server_socket.listen(5)
print(f"서버가 {server_port} 포트에서 대기 중...")

# 서버 10번 반복
server_count = 0
try:
    while server_count < 10:
        client_socket, client_addr = server_socket.accept()
        client_count = 0  # 클라이언트 요청 수를 세는 변수

        while client_count < 5:
            data = client_socket.recv(1024).decode()

            if data == "red":  # 검증할 데이터 조건
                print("True")
            else:
                print("False")

            client_count += 1

        # 클라이언트와의 연결을 종료
        client_socket.close()

        # 연결 종료하고나면 다시 반복
        server_count += 1

except Exception as e:
    raise e