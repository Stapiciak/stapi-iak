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

    def _format_domain_to_query_name(self, pa_domain):
        domain_splited = pa_domain
        qname_result = bytes()
        for label in domain_splited:
            print(label)
            qname_result += struct.pack("!B", len(label))
            qname_result += label.encode()
            qname_result += struct.pack("!B", 0)
            return qname_result
    pass

    def generate_query_body(self, pa_dns_query_body_model:DnsQueryBodyModel):
        qnameb = self._format_domain_to_query_name(pa_dns_query_body_model.domain)
        qtypeb = struct.pack("!H", pa_dns_query_body_model.type)
        qclassb = struct.pack("!H", pa_dns_query_body_model.qclass)
        pass