import socket


class DnsSocketServce:

    def __init__(self, pa_dns_server = "8.8.8.8") -> None:
        self.dns_server = pa_dns_server
        self.dns_port = 53
        self._listen_on = "0.0.0.0"
        self.dns_client_port = 60000
        self.socket = None

    def init_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.socket)
        self.socket.bind(self._listen_on, self.dns_client_port)

    def send_data(self, data:bytes):
        self.socket.sendto(data, (self.dns_server, self.dns_port))

    def gen_response(self):
        return self.socket.recvfrom(1000)

    def destroy_socket(self):
        self.socket.close()