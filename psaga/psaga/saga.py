
class Saga:
    def __init__(self, execute_func, rollback_func):
        self.execute_func = execute_func
        self.rollback_func = rollback_func

    def execute(self):
        self.execute_func()
        

    def rollback(self):
        self.rollback_func()