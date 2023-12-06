# Тестовое задание:

## Вопрос 1

```
def isEven(value):
    """First (example) realization"""
    return value % 2 == 0


def is_even(value):
    """Second (my) realization"""
    return not value & 1
```

#### Плюсы и минусы каждой реализации:

| Реализация | Плюсы                                                                                                                                                                              | Минусы                                                                                                                                                         |
|:----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1      | Простота реализации                                                                                                                                                                | Использование оператора _%_ для вычисления остатка от деления может быть более трудозатратным, чем другие методы проверки четности, особенно для больших чисел |
|     2      | Использование поразрядной операции _&_ более эффективно с точки зрения производительности, особенно на уровне железа, потому что оно просто выполняет проверку нулевого бита числа | Сложность понимания                                                                                                                                            |

--------------------------

## Вопрос 2

### Реализация 1: На основе списка

```
class CircularBufferList:
    """First realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, value):
        if len(self.buffer) < self.capacity:
            self.buffer.append(value)
        else:
            self.buffer = self.buffer[1:] + [value]

    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.pop(0)
```

### Реализация №2: На основе массива и указателей

```
class CircularBufferArray:
    """Second realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = self.tail = self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            self.dequeue()
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size = max(self.size - 1, 0)
        return value
```

### Реализация 3: На основе связанного списка

```
class CircularBufferLinkedList:
    """Third realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            return None
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

#### Плюсы и минусы каждой реализации:

| Реализация | Плюсы                                                                                                                    | Минусы                                                                                                                                                                                     |
|:----------:|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1      | Простота реализации                                                                                                      | Добавлении нового элемента за _O(1)_, при этом удаление элемента в начале списка происходит за _O(n)_, что делает операцию dequeue менее эффективной, особенно при больших размерах буфера |
|     2      | Такая реализация обеспечивает добавление и удаление за _O(1)_, что делает ее более эффективной при большом объеме данных | Сложность реализации                                                                                                                                                                       |
|     3      | Использование связанного списка упрощает операции вставки и удаления элементов, не требуя сдвига других элементов        | Связанный список может потреблять больше памяти из-за дополнительной структуры узлов                                                                                                       |

--------------------------

## Вопрос 3

```
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [n for n in arr if n < pivot]
    middle = [n for n in arr if n == pivot]
    right = [n for n in arr if n > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

Пояснение:

- **Разделяй и властвуй**: Быстрая сортировка использует стратегию "разделяй и властвуй", разбивая массив на более
  мелкие подмассивы, сортируя их, а затем объединяя весь массив воедино.
- **Средняя сложность**: В среднем случае быстрая сортировка имеет время выполнения _O(n log n)_, что делает ее очень
  эффективной для больших массивов чисел.

Также возможно использование констант для достижения большего быстродействия по сравнению с сортировкой слиянием.

