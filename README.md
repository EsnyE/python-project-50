### Hexlet tests and linter status:
[![Actions Status](https://github.com/EsnyE/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EsnyE/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EsnyE_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EsnyE_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EsnyE_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EsnyE_python-project-50)

## Описание

Вычислитель отличий — это утилита командной строки, которая сравнивает два конфигурационных файла в формате JSON или YAML (включая вложенные структуры) и выводит различия между ними в наглядном виде.

### Возможности

- Поддержка JSON и YAML/YML файлов
- Рекурсивное сравнение вложенных структур
- Три формата вывода:
  - `stylish` — древовидное представление с символами `+` и `-` (по умолчанию)
  - `plain` — текстовое описание изменений
  - `json` — структурированный JSON-вывод для интеграции с другими системами

## Демонстрация работы

[![asciicast](https://asciinema.org/a/tcgYKDS96lbBCG9n)]

# Клонирование репозитория
git clone https://github.com/EsnyE/python-project-50.git

## Запуск
cd gendiff
