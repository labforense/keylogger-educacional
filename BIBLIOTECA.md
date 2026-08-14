# 📚 keylogger-edu - Biblioteca Educacional

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue)]()
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)]()
[![Status: Educational](https://img.shields.io/badge/Status-Educational-green)]()

Uma **biblioteca Python profissional** para fins educacionais sobre segurança ofensiva, keyloggers e análise de ameaças.

## 📦 Instalação

### Via pip (quando publicado)

```bash
pip install keylogger-edu
```

### Instalação local

```bash
git clone https://github.com/labforense/keylogger-educacional.git
cd keylogger-educacional
pip install -e .
```

## 🚀 Quick Start

### Exemplo 1: Keylogger Básico

```python
from keylogger_edu import KeyLogger

# Criar keylogger
logger = KeyLogger()

# Iniciar captura (pressione ESC para parar)
logger.start()
```

### Exemplo 2: Análise de Dados

```python
from keylogger_edu import LogAnalyzer

# Analisar arquivo de log
analyzer = LogAnalyzer("keys.log")

# Ver resumo
analyzer.print_summary()

# Exportar relatório
analyzer.export_report("relatorio.json")
```

### Exemplo 3: Keylogger com Encriptação

```python
from keylogger_edu import SecureKeyLogger

# Criar keylogger seguro
secure = SecureKeyLogger()

# Registrar dados encriptados
secure.register_key("minha_senha")

# Ler dados
secure.read_log()
```

### Exemplo 4: Detectar Ameaças

```python
from keylogger_edu import ThreatDetector

# Criar detector
detector = ThreatDetector()

# Fazer varredura
resultado = detector.scan_system()

# Imprimir relatório
detector.print_scan_report()
```

## 📖 Documentação Completa

### Módulos

#### `keylogger_edu.core`

**Classe: KeyLogger**

Captura de teclado básica.

```python
from keylogger_edu import KeyLogger
from pynput import keyboard

logger = KeyLogger(
    log_file="keys.log",
    stop_key=keyboard.Key.esc,
    ignore_keys={keyboard.Key.shift, ...}
)

logger.start()  # Iniciar captura
```

**Parâmetros:**
- `log_file` (str): Arquivo de saída
- `stop_key` (keyboard.Key): Tecla para parar
- `ignore_keys` (set): Teclas a ignorar

**Métodos:**
- `start()`: Inicia captura
- `start_callback(on_key_callback)`: Inicia com callback customizado

---

#### `keylogger_edu.analyzer`

**Classe: LogAnalyzer**

Análise de dados capturados.

```python
from keylogger_edu import LogAnalyzer

analyzer = LogAnalyzer("keys.log")

# Estatísticas
stats = analyzer.get_statistics()

# Teclas mais frequentes
top_keys = analyzer.get_most_common_keys(10)

# Detectar padrões
patterns = analyzer.detect_patterns()

# Exportar relatório
analyzer.export_report("relatorio.json")
```

**Métodos:**
- `get_statistics()`: Estatísticas gerais
- `get_most_common_keys(n)`: Top N teclas
- `detect_patterns()`: Detecta senhas, emails, URLs
- `get_frequency_analysis()`: Análise de frequência
- `export_report(file)`: Exporta em JSON
- `print_summary()`: Imprime resumo

---

#### `keylogger_edu.security`

**Classe: EncryptionManager**

Gerencia encriptação de dados.

```python
from keylogger_edu import EncryptionManager

manager = EncryptionManager("chave.key")

# Encriptar
encrypted = manager.encrypt("dados_sensíveis")

# Descriptografar
dados = manager.decrypt(encrypted)

# Rotacionar chave
manager.rotate_key("chave_nova.key")
```

**Classe: SecureKeyLogger**

Keylogger com encriptação automática.

```python
from keylogger_edu import SecureKeyLogger

secure = SecureKeyLogger()

# Registrar (encriptado automaticamente)
secure.register_key("tecla")

# Ler e descriptografar
secure.read_log()

# Estatísticas
stats = secure.get_statistics()
```

**Classe: ThreatDetector**

Detecta ameaças no sistema.

```python
from keylogger_edu.security import ThreatDetector

detector = ThreatDetector()

# Verificar arquivos suspeitos
files = detector.check_suspicious_files()

# Gerar checklist de segurança
checklist = detector.generate_security_checklist()

# Exportar relatório
detector.export_security_report("seguranca.json")
```

---

#### `keylogger_edu.detector`

**Classe: ThreatDetector**

Detecta keyloggers e ameaças.

```python
from keylogger_edu import ThreatDetector

detector = ThreatDetector()

# Varredura completa
resultado = detector.scan_system()

# Imprimir relatório
detector.print_scan_report()
```

---

## 🎓 Exemplos Práticos

A biblioteca inclui 5 exemplos completos em `examples/`:

1. **1_basico.py** - Keylogger simples
2. **2_analise.py** - Análise de dados
3. **3_encriptado.py** - Dados encriptados
4. **4_detector.py** - Detecção de ameaças
5. **5_completo.py** - Integração completa

```bash
# Executar exemplos
python examples/1_basico.py
python examples/2_analise.py
python examples/3_encriptado.py
python examples/4_detector.py
python examples/5_completo.py
```

---

## ⚖️ Legalidade e Ética

### ⚠️ IMPORTANTE

Este código é fornecido **APENAS para fins educacionais**.

**PERMITIDO:**
- ✅ Usar em seu próprio PC
- ✅ Fins educacionais e pesquisa
- ✅ Ambientes de teste controlados
- ✅ Pentesting autorizado

**PROIBIDO:**
- ❌ Usar contra terceiros
- ❌ Roubar dados sem autorização
- ❌ Atividades criminosas
- ❌ Violar privacidade

### Leis Aplicáveis

**Brasil:**
- Lei de Acesso a Computadores (12.965/14)
- Lei Geral de Proteção de Dados (LGPD)
- Código Penal (artigos 154, 286, 307)

**Penas:** Multa pesada + Prisão (3-8 anos)

---

## 🛡️ Proteção e Defesa

Esta biblioteca também ensina como se defender:

```python
from keylogger_edu import ThreatDetector

# Detectar keyloggers no sistema
detector = ThreatDetector()
detector.scan_system()
detector.print_scan_report()
```

**Dicas de segurança:**
- Manter Windows atualizado
- Usar antivírus (Windows Defender, Malwarebytes)
- Senhas fortes e únicas
- Ativar 2FA
- VPN em WiFi público
- Verificar certificados SSL

---

## 📊 Arquitetura

```
keylogger_edu/
├── __init__.py              # Exports principais
├── core.py                  # KeyLogger
├── analyzer.py              # LogAnalyzer
├── security.py              # EncryptionManager, SecureKeyLogger
├── detector.py              # ThreatDetector
└── utils.py                 # Funções auxiliares

examples/
├── 1_basico.py
├── 2_analise.py
├── 3_encriptado.py
├── 4_detector.py
└── 5_completo.py

tests/
├── test_core.py
├── test_analyzer.py
└── test_security.py
```

---

## 🔗 Recursos

- [Documentação Pynput](https://pynput.readthedocs.io/)
- [Python Security](https://realpython.com/)
- [OWASP](https://owasp.org/)
- [MITRE ATT&CK](https://attack.mitre.org/)

---

## 📝 Licença

Creative Commons Attribution-ShareAlike 4.0 International License

---

## ⚠️ Disclaimer

Este software é fornecido "COMO ESTÁ" sem garantias. Os autores não são responsáveis pelo uso indevido.

Use este conhecimento **responsavelmente e eticamente**. 🎓

---

**Criado para fins educacionais**

Last updated: 2026-08-14
