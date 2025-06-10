# 📋 Sección 10: Metodologías Avanzadas para Código Limpio

Esta sección presenta cinco metodologías complementarias que te ayudarán a escribir código más profesional y mantenible. Cada metodología se enfoca en un aspecto específico del desarrollo:

## 🎯 Objetivos de Aprendizaje

Al finalizar esta sección serás capaz de:
- Aplicar nomenclatura efectiva usando **CLEAR**
- Diseñar funciones siguiendo los principios **FIRST**
- Implementar manejo robusto de errores con **ACID**
- Seleccionar estructuras de datos óptimas usando **TIME**
- Optimizar código aplicando **CLEAR-FAST**

---

## 🏷️ CLEAR - Nomenclatura Efectiva

### Principios CLEAR
- **C**lear (Claro): El propósito es evidente
- **L**ogical (Lógico): Sigue patrones consistentes
- **E**xpressive (Expresivo): Comunica la intención
- **A**ccurate (Preciso): Describe exactamente qué hace
- **R**eadable (Legible): Fácil de leer y pronunciar

### ❌ Antes (Nomenclatura Confusa)
```python
def calc(x, y, z):
    return x * y * z

data = [1, 2, 3, 4, 5]
avg = sum(data) / len(data)

class UM:
    def __init__(self):
        self.aus = {}
        self.fla = {}
    
    def val_usr(self, u, p):
        pass
```

### ✅ Después (Nomenclatura CLEAR)
```python
def calculate_box_volume(length, width, height):
    """Calcula el volumen de una caja rectangular."""
    return length * width * height

daily_sales = [150, 200, 175, 300, 225]
average_daily_sales = sum(daily_sales) / len(daily_sales)

class UserAccountManager:
    def __init__(self):
        self.active_user_sessions = {}
        self.failed_login_attempts = {}
    
    def validate_user_credentials(self, username, password):
        pass
```

---

## 🔧 FIRST - Diseño Funcional

### Principios FIRST
- **F**ast (Rápido): Ejecución eficiente
- **I**ndependent (Independiente): Sin dependencias externas
- **R**epeatable (Repetible): Resultados consistentes
- **S**elf-validating (Auto-validante): Resultado claro (pasa/falla)
- **T**imely (Oportuno): Cubre casos relevantes

### Ejemplo: Funciones Puras y Testeable
```python
import unittest
from typing import Optional

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Función pura - siempre retorna el mismo resultado."""
        return a + b
    
    @staticmethod
    def divide(dividend: float, divisor: float) -> Optional[float]:
        """Función con manejo de casos edge."""
        if divisor == 0:
            return None
        return dividend / divisor

class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):  # Fast & Independent
        result = Calculator.add(2, 3)
        self.assertEqual(result, 5)  # Self-validating
    
    def test_divide_by_zero(self):  # Timely - caso límite
        result = Calculator.divide(10, 0)
        self.assertIsNone(result)
    
    def test_operations_are_repeatable(self):  # Repeatable
        # Múltiples ejecuciones dan el mismo resultado
        for _ in range(100):
            self.assertEqual(Calculator.add(5, 3), 8)
```

---

## 🛡️ ACID - Manejo de Errores

### Principios ACID (Adaptados para Manejo de Errores)
- **A**tomic (Atómico): Operaciones todo-o-nada
- **C**onsistent (Consistente): Estado siempre válido
- **I**solated (Aislado): Errores no afectan otras operaciones
- **D**urable (Duradero): Logging persistente

### Ejemplo: Transferencia Bancaria Robusta
```python
import logging
from contextlib import contextmanager

# Configurar logging duradero
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('transactions.log'),
        logging.StreamHandler()
    ]
)

class BankAccount:
    def __init__(self, account_id: str, initial_balance: float = 0):
        self.account_id = account_id
        self.balance = initial_balance
        self.transaction_log = []
    
    @contextmanager
    def atomic_transaction(self, operation_name: str):
        """Contexto para operaciones atómicas."""
        initial_state = {
            'balance': self.balance,
            'log_size': len(self.transaction_log)
        }
        
        try:
            logging.info(f"Starting {operation_name} for {self.account_id}")
            yield
            logging.info(f"Completed {operation_name} successfully")
        except Exception as e:
            # Rollback atómico
            self.balance = initial_state['balance']
            self.transaction_log = self.transaction_log[:initial_state['log_size']]
            logging.error(f"Transaction {operation_name} failed: {e}")
            raise
    
    def transfer_money(self, target_account, amount: float):
        """Transferencia con propiedades ACID."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Operación atómica
        with self.atomic_transaction("money_transfer"):
            if self.balance < amount:
                raise ValueError("Insufficient funds")
            
            # Operación consistente - ambas cuentas se actualizan
            self.balance -= amount
            target_account.balance += amount
            
            # Log duradero
            self.transaction_log.append({
                'type': 'transfer_out',
                'amount': amount,
                'target': target_account.account_id
            })
```

---

## ⏱️ TIME - Selección de Estructuras de Datos

### Principios TIME
- **T**ime complexity (Complejidad temporal)
- **I**teration patterns (Patrones de iteración)
- **M**emory usage (Uso de memoria)
- **E**xpected operations (Operaciones esperadas)

### Guía de Selección
```python
from collections import deque, defaultdict, Counter
import bisect

# T - Complejidad Temporal
# ❌ MALO - O(n) para búsquedas frecuentes
users_list = [('alice', 25), ('bob', 30), ('charlie', 35)]
def find_user_slow(name):
    for user_name, age in users_list:
        if user_name == name:
            return age

# ✅ BUENO - O(1) para búsquedas frecuentes
users_dict = {'alice': 25, 'bob': 30, 'charlie': 35}
def find_user_fast(name):
    return users_dict.get(name)

# I - Patrones de Iteración
task_queue = deque()  # O(1) append/popleft para colas
call_stack = []       # O(1) append/pop para pilas

# M - Uso de Memoria
sparse_matrix = defaultdict(dict)  # Solo almacena valores no-cero
sparse_matrix[1000][2000] = 5     # Eficiente en memoria

# E - Operaciones Esperadas
word_frequencies = Counter()       # Optimizado para conteo
sorted_scores = [65, 70, 75, 80]  # Para búsqueda binaria O(log n)

def find_score_position(score):
    return bisect.bisect_left(sorted_scores, score)
```

---

## 🚀 CLEAR-FAST - Optimización

### Principios CLEAR-FAST
- **C**ache effectively (Cache efectivo)
- **L**azy evaluation (Evaluación perezosa)  
- **E**arly termination (Terminación temprana)
- **A**lgorithmic efficiency (Eficiencia algorítmica)
- **R**esource pooling (Pool de recursos)
- **F**unctional purity (Pureza funcional)
- **A**synchronous operations (Operaciones asíncronas) 
- **S**treaming data (Datos en streaming)
- **T**hreading/multiprocessing (Hilos/multiproceso)

### Ejemplos de Optimización
```python
from functools import lru_cache
import asyncio
from concurrent.futures import ThreadPoolExecutor

class OptimizedProcessor:
    
    # C - Cache efectivo
    @lru_cache(maxsize=128)
    def expensive_calculation(self, n):
        if n <= 1:
            return n
        return self.expensive_calculation(n-1) + self.expensive_calculation(n-2)
    
    # L - Evaluación perezosa
    def process_large_dataset(self, data_source):
        """Procesa datos solo cuando se necesitan."""
        for item in data_source:
            if self.should_process(item):
                yield self.transform_item(item)  # Lazy evaluation
    
    # E - Terminación temprana
    def find_first_match(self, items, condition):
        """Termina apenas encuentra el primer match."""
        for item in items:
            if condition(item):
                return item  # Early termination
        return None
    
    # A - Eficiencia algorítmica
    def efficient_deduplication(self, items):
        # O(n) con set vs O(n²) con listas anidadas
        return list(set(items))
    
    # R - Pool de recursos
    def process_parallel_tasks(self, tasks):
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(self.process_task, task) for task in tasks]
            return [future.result() for future in futures]
    
    # F - Pureza funcional
    def pure_transform(self, data, func):
        """Sin efectos secundarios."""
        return [func(item) for item in data]
    
    # A - Operaciones asíncronas
    async def fetch_multiple_urls(self, urls):
        async def fetch_url(url):
            # Simula I/O asíncrono
            await asyncio.sleep(0.1)
            return f"Data from {url}"
        
        tasks = [fetch_url(url) for url in urls]
        return await asyncio.gather(*tasks)
    
    # S - Streaming de datos
    def stream_process_file(self, filename, chunk_size=1024):
        """Procesa archivos grandes en chunks."""
        with open(filename, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield self.process_chunk(chunk)
```

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Aplicar CLEAR
Refactoriza este código aplicando nomenclatura CLEAR:

```python
def proc(d):
    r = []
    for i in d:
        if i % 2 == 0:
            r.append(i * 2)
    return r

class DataMgr:
    def __init__(self):
        self.d = {}
    
    def add(self, k, v):
        self.d[k] = v
```

### Ejercicio 2: Implementar FIRST
Crea una función que siga los principios FIRST para validar emails:

```python
# Tu función debe ser:
# - Fast: Rápida ejecución
# - Independent: Sin dependencias externas  
# - Repeatable: Mismo resultado siempre
# - Self-validating: Retorna True/False claramente
# - Timely: Cubre casos edge importantes

def validate_email(email: str) -> bool:
    # Tu implementación aquí
    pass
```

### Ejercicio 3: Manejo ACID
Implementa una clase `ShoppingCart` que maneje operaciones de forma ACID:

```python
class ShoppingCart:
    def __init__(self):
        # Tu implementación aquí
        pass
    
    def add_item(self, item, quantity, price):
        # Debe ser atómica y consistente
        pass
    
    def remove_item(self, item):
        # Con logging duradero
        pass
```

---

## ✅ Soluciones

### Solución Ejercicio 1: CLEAR
```python
def filter_and_double_even_numbers(input_numbers):
    """Filtra números pares y los multiplica por 2."""
    doubled_even_numbers = []
    for current_number in input_numbers:
        if current_number % 2 == 0:
            doubled_even_numbers.append(current_number * 2)
    return doubled_even_numbers

class DataStorageManager:
    def __init__(self):
        self.stored_key_value_pairs = {}
    
    def add_key_value_pair(self, storage_key, storage_value):
        self.stored_key_value_pairs[storage_key] = storage_value
```

### Solución Ejercicio 2: FIRST
```python
import re

def validate_email(email: str) -> bool:
    """
    Valida formato de email usando regex.
    
    Fast: Ejecución rápida con regex compilado
    Independent: Solo usa biblioteca estándar
    Repeatable: Mismo input = mismo output
    Self-validating: Retorna True/False
    Timely: Cubre casos edge comunes
    """
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

# Tests FIRST
def test_validate_email():
    # Fast tests
    assert validate_email("user@example.com") == True
    assert validate_email("invalid-email") == False
    
    # Edge cases (Timely)
    assert validate_email("") == False
    assert validate_email(None) == False
    assert validate_email("user@.com") == False
    
    print("All tests passed!")
```

### Solución Ejercicio 3: ACID
```python
import logging
from contextlib import contextmanager
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class ShoppingCart:
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.items = {}  # {item_name: {'quantity': int, 'price': float}}
        self.total_amount = 0.0
        self.transaction_log = []
    
    @contextmanager
    def atomic_operation(self, operation_name: str):
        """Garantiza atomicidad de operaciones."""
        initial_state = {
            'items': self.items.copy(),
            'total_amount': self.total_amount,
            'log_size': len(self.transaction_log)
        }
        
        try:
            logging.info(f"Starting {operation_name} for {self.customer_id}")
            yield
            logging.info(f"Successfully completed {operation_name}")
        except Exception as e:
            # Rollback atómico
            self.items = initial_state['items']
            self.total_amount = initial_state['total_amount']
            self.transaction_log = self.transaction_log[:initial_state['log_size']]
            logging.error(f"Operation {operation_name} failed: {e}")
            raise
    
    def add_item(self, item_name: str, quantity: int, price: float):
        """Añade item de forma ACID."""
        if quantity <= 0 or price < 0:
            raise ValueError("Invalid quantity or price")
        
        with self.atomic_operation("add_item"):
            if item_name in self.items:
                # Consistencia: actualizar cantidad y total
                old_quantity = self.items[item_name]['quantity']
                self.items[item_name]['quantity'] += quantity
                self.total_amount += quantity * price
            else:
                self.items[item_name] = {'quantity': quantity, 'price': price}
                self.total_amount += quantity * price
            
            # Log duradero
            self.transaction_log.append({
                'timestamp': datetime.now().isoformat(),
                'operation': 'add_item',
                'item': item_name,
                'quantity': quantity,
                'price': price
            })
    
    def remove_item(self, item_name: str):
        """Remueve item de forma ACID."""
        if item_name not in self.items:
            raise KeyError(f"Item {item_name} not found in cart")
        
        with self.atomic_operation("remove_item"):
            removed_item = self.items[item_name]
            item_total = removed_item['quantity'] * removed_item['price']
            
            # Operación consistente
            del self.items[item_name]
            self.total_amount -= item_total
            
            # Log duradero
            self.transaction_log.append({
                'timestamp': datetime.now().isoformat(),
                'operation': 'remove_item',
                'item': item_name,
                'removed_quantity': removed_item['quantity'],
                'removed_total': item_total
            })
```

---

## 📝 Checklist de Metodologías

### ✅ CLEAR - Nomenclatura
- [ ] Los nombres son autodescriptivos
- [ ] Siguen convenciones consistentes
- [ ] Expresan la intención claramente
- [ ] Son precisos y no ambiguos
- [ ] Son legibles y pronunciables

### ✅ FIRST - Funciones
- [ ] Ejecución rápida
- [ ] Independientes de estado externo
- [ ] Resultados repetibles
- [ ] Validación clara del resultado
- [ ] Cubren casos oportunos

### ✅ ACID - Errores
- [ ] Operaciones atómicas
- [ ] Estado siempre consistente
- [ ] Errores aislados
- [ ] Logging duradero

### ✅ TIME - Estructuras
- [ ] Complejidad temporal apropiada
- [ ] Patrones de iteración eficientes
- [ ] Uso de memoria optimizado
- [ ] Operaciones esperadas consideradas

### ✅ CLEAR-FAST - Optimización
- [ ] Cache implementado donde útil
- [ ] Evaluación perezosa aplicada
- [ ] Terminación temprana usada
- [ ] Algoritmos eficientes elegidos
- [ ] Pool de recursos cuando apropiado
- [ ] Funciones puras preferidas
- [ ] Operaciones asíncronas para I/O
- [ ] Streaming para datos grandes
- [ ] Paralelización para CPU intensivo

---

## 🎓 Proyecto Final: Sistema de Gestión de Biblioteca

Implementa un sistema que aplique todas las metodologías:

**Requisitos:**
1. **CLEAR**: Nomenclatura clara en todas las clases y métodos
2. **FIRST**: Funciones puras y bien testeadas
3. **ACID**: Manejo robusto de préstamos de libros
4. **TIME**: Estructuras de datos óptimas para búsquedas
5. **CLEAR-FAST**: Optimizaciones para consultas frecuentes

**Clases mínimas:**
- `LibraryBook` (información del libro)
- `LibraryMember` (información del miembro)
- `BookLoanManager` (gestión de préstamos)
- `LibrarySearchEngine` (búsquedas optimizadas)

**Bonus:** Incluye tests unitarios que sigan FIRST y documentación clara.

---

## 📚 Recursos Adicionales

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Effective Python by Brett Slatkin](https://effectivepython.com/)

---

## 🏁 Conclusión

Estas cinco metodologías te proporcionan un framework completo para escribir código profesional:

- **CLEAR** asegura que tu código sea comprensible
- **FIRST** garantiza funciones robustas y testeables  
- **ACID** proporciona manejo confiable de errores
- **TIME** optimiza el rendimiento mediante estructuras apropiadas
- **CLEAR-FAST** lleva tu código al siguiente nivel de eficiencia

La aplicación consistente de estos principios diferenciará tu código como verdaderamente profesional y mantenible.

¡Continúa practicando y aplicando estas metodologías en todos tus proyectos!