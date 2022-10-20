class DnsHeaderType:

    def __int__(self, pa_transaction_id = 0x1234, pa_flags = 0x0100, pa_question_count = 1, pa_answer_count = 0, pa_authority_count = 0, pa_additional_count = 0):
        self.translation = pa_transaction_id;
        self.flags = pa_flags;
        self.question = pa_question_count;
        self.answer = pa_answer_count;
        self.authority = pa_authority_count;
        self.additional = pa_additional_count;
        pass