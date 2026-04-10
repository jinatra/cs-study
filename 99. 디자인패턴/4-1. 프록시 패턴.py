# 프록시 패턴: 객체에 접근하기 전에 가로채서 필터링/제어하는 패턴
# 클라이언트는 프록시를 쓰든 실제 서버를 쓰든 같은 방식(handle_request)으로 사용

# --- 실제 서버 ---
class Server:
    def handle_request(self, ip):
        print(f"{ip} 요청 처리 완료")

# --- 프록시 (서버 앞에서 요청을 가로채는 역할) ---
class ProxyServer:
    def __init__(self):
        self.server = Server()  # 실제 서버 정보를 프로퍼티로 갖고 있음 (나중에 전달해주기 위해)
        self.blocked_ips = ["666.666.666.666"]  # 차단할 IP 목록

    # 실제 서버와 같은 이름의 메서드 → 클라이언트는 프록시인지 서버인지 구분할 필요 없음
    def handle_request(self, ip):
        if ip in self.blocked_ips:  # 요청을 가로채서 검사
            print(f"{ip} 차단됨!")
            return
        self.server.handle_request(ip)  # 문제 없으면 내가 갖고 있는 실제 서버의 handle_request 실행

# --- 사용 ---
proxy = ProxyServer()
proxy.handle_request("123.456.789.0")    # 123.456.789.0 요청 처리 완료
proxy.handle_request("666.666.666.666")  # 666.666.666.666 차단됨!