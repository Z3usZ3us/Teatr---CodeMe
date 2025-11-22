"""
Moduł z definicjami klas reprezentująmi miejsca w teatrze.

Klasy:
- MiejsceTeatralne: klasa bazowa
- MiejsceZwykle: zwykłe miejsce
- MiejsceVIP: miejsce VIP
- MiejsceDlaNiepelnosprawnych: miejsce dla niepełnosprawnych
"""

from abc import ABC, abstractmethod
from enum import Enum