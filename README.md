# psaga

psaga is simple a saga ochestrator package.

## Install
```python
git clone https://github.com/nosyos/psaga.git
cd psaga
pip install -e .
```

## Uninstall
```python
pip uninstall psaga
```

## Usage
```python
from psaga import Saga, SagaOrchestrator

def main():
    sagaOrc = SagaOrchestrator()

    saga_01 = Saga(exec_func_01, rollback_func_01)
    saga_02 = Saga(exec_func_02, rollback_func_02)
    saga_03 = Saga(exec_func_03, rollback_func_03)

    sagaOrc.add_transaction(saga_01) \
        .add_transaction(saga_02) \
        .add_transaction(saga_03)

    sagaOrc.execute_transactions()


def exec_func_01():
    print(f"This is exec_func_01")

def rollback_func_01():
    print("This is rollback_func_01")

def exec_func_02():
    print(f"This is exec_func_02")

def rollback_func_02():
    print("This is rollback_func_02")

def exec_func_03():
    raise Exception("raise Exception")

def rollback_func_03():
    print("This is rollback_func_03")


if __name__ == '__main__':
    main()
```