import struct

import DnsHeader
from DnsQueryBodyModel import DnsQueryBodyModel


class DnsServcice:

    def generate_header(self, pa_dns_header_model:DnsHeader):
        return struct.pack("!2H", pa_dns_header_model.translation_id,
                           pa_dns_header_model.flags,
                           pa_dns_header_model.question,
                           pa_dns_header_model.answer,
                           pa_dns_header_model.authority,
                           pa_dns_header_model.additional)

    def generate_query_body(self, pa_dns_query_body_model:DnsQueryBodyModel):

        qtypeb = struct.pack("!H", pa_dns_query_body_model.type)
        qclassb = struct.pack("!H", pa_dns_query_body_model.qclass)
        pass