from collections import deque

from saga import Saga

class SagaOrchestrator():
    def __init__(self):
        self.execuute_queue = deque()
        self.rollback_stack = deque()


    def add_transaction(self, saga):
        if isinstance(saga, Saga):
            raise ValueError("parameter is not saga object")

        self.execuute_queue.append(saga)

        return self
        

    def execute_transactions(self):
        try:
            for item in self.execuute_queue:
                item.execute()
                self.rollback_stack.append(item)
        except Exception:
            self._rollback_transaction()


    def _rollback_transaction(self):
        for item in reversed(self.rollback_stack):
            item.rollback()