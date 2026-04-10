# 프록시 패턴
# 실제 서버에 접근하기 전 요청 등을 가로채서 지정된 작업(해킹 의심 등)을 실행

class Server:
    def response_request(self, ip):
        print(f'{ip}의 요청을 처리')

class ProxyServer:
    def __init__(self):
        self.server = Server() # 속성으로 실제로 요청 들어갈 서버 할당
        self.blocked_ips = ['666.666.666'] # 속성으로 차단 IP 설정
    
    def check_request(self, ip):
        if ip in self.blocked_ips:
            print(f'{ip}는 블록 IP라 요청 차단')
            return
        self.server.response_request(ip)

proxy = ProxyServer()
proxy.check_request('666.666.666')