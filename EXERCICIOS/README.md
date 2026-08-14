# 🎓 Exercícios - Keylogger Educacional

Bem-vindo aos exercícios práticos! Aqui você vai praticar os conceitos aprendidos no tutorial.

## Estrutura

```
EXERCICIOS/
├── nivel1_timestamps.py       # Iniciante
├── nivel2_analise.py          # Intermediário
├── nivel3_encriptacao.py      # Avançado
└── README.md                  # Este arquivo
```

## Pré-requisitos

Antes de começar, instale as dependências:

```bash
pip install pynput cryptography pygetwindow
```

## Nível 1: Iniciante 🟢

**Arquivo:** `nivel1_timestamps.py`

**Objetivo:** Aprender a adicionar timestamps aos logs

**O que você vai fazer:**
1. Abrir o arquivo `nivel1_timestamps.py`
2. Adicionar `from datetime import datetime`
3. Modificar a função `on_press()` para incluir timestamp
4. Testar o programa
5. Verificar se `keys_nivel1.log` contém datas/horas

**Exemplo esperado:**
```
[2026-08-14 14:30:45] o
[2026-08-14 14:30:46] l
[2026-08-14 14:30:47] a
```

**Dica:**
```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

**Executar:**
```bash
python nivel1_timestamps.py
```

---

## Nível 2: Intermediário 🟡

**Arquivo:** `nivel2_analise.py`

**Objetivo:** Analisar dados capturados e encontrar padrões

**O que você vai fazer:**
1. Executar o keylogger normal: `python ../keylogger.py`
2. Digitar algo (tipo: "olá mundo teste teste")
3. Pressionar ESC para parar
4. Executar: `python nivel2_analise.py`
5. Ver as teclas mais frequentes

**Exemplo de saída:**
```
📊 ANÁLISE DE TECLAS
==================================================

Teclas mais digitadas:
  'e': 3x
  't': 3x
  'o': 2x
  ' ': 2x
```

**O que você aprende:**
- Análise de frequência (importante em criptografia)
- Leitura e processamento de arquivos
- Collections.Counter
- Formato JSON

**Desafios extras:**
1. Encontre a palavra mais longa digitada
2. Calcule palavras por minuto (WPM)
3. Detecte URLs digitadas
4. Exporte para CSV

**Executar:**
```bash
python nivel2_analise.py
```

---

## Nível 3: Avançado 🔴

**Arquivo:** `nivel3_encriptacao.py`

**Objetivo:** Implementar encriptação e detecção de keylogger

**O que você vai fazer:**
1. Executar: `python nivel3_encriptacao.py`
2. Observar como funciona encriptação
3. Ver dados criptografados vs descriptografados
4. Aprender detecção de ameaças

**Conceitos:**
- Encriptação Fernet (simétrica)
- Geração e armazenamento de chaves
- Detecção de processos suspeitos
- Relatórios de segurança

**O que será criado:**
- `chave.key` - Sua chave secreta (⚠️ NUNCA compartilhe!)
- `keys.enc` - Arquivo de log encriptado

**Importante:**
```
🔒 Se perder chave.key, não consegue ler os dados!
```

**Desafios extras:**
1. Integre encriptação no keylogger principal
2. Crie detector automático de keylogger
3. Implemente 2FA no seu sistema
4. Analise comportamento de encriptação

**Executar:**
```bash
python nivel3_encriptacao.py
```

---

## Roadmap Recomendado

### Semana 1: Fundações
- [ ] Completar Nível 1
- [ ] Entender datetime
- [ ] Testar e debugar

### Semana 2: Análise
- [ ] Completar Nível 2
- [ ] Fazer desafios extras
- [ ] Criar análises customizadas

### Semana 3: Segurança
- [ ] Completar Nível 3
- [ ] Implementar encriptação no código principal
- [ ] Criar detector de ameaças

### Semana 4: Integração
- [ ] Combinar todos os conceitos
- [ ] Criar projeto final
- [ ] Apresentar aprendizados

---

## Soluções

### Se estiver preso:

1. **Verifique o tutorial:** [TUTORIAL.md](../TUTORIAL.md)
2. **Leia os comentários:** Há soluções comentadas nos arquivos
3. **Teste incrementalmente:** Não tente tudo de uma vez
4. **Use print():** Debug seu código

### Exemplo de Debug:

```python
# Adicione prints para entender o que está acontecendo
print(f"Tecla digitada: {key}")
print(f"Timestamp: {datetime.now()}")
print(f"Arquivo aberto: {os.path.exists(LOG_FILE)}")
```

---

## Checklist de Aprendizado

Quando você completar cada exercício, marque:

### Nível 1
- [ ] Entendo como usar `datetime`
- [ ] Sei o formato `strftime`
- [ ] Consegui adicionar timestamp ao log
- [ ] Testei e funcionou

### Nível 2
- [ ] Sei ler arquivo completo
- [ ] Entendo `Counter`
- [ ] Consigo encontrar padrões
- [ ] Criei análise customizada

### Nível 3
- [ ] Entendo encriptação básica
- [ ] Consegui encriptar/descriptografar
- [ ] Sei diferenciar dados seguros vs não seguros
- [ ] Implementei detector de ameaças

---

## Recursos Adicionais

### Documentação
- [Datetime Docs](https://docs.python.org/3/library/datetime.html)
- [Collections Docs](https://docs.python.org/3/library/collections.html)
- [Cryptography Docs](https://cryptography.io/)

### Tutoriais
- [Real Python - Datetime](https://realpython.com/python-datetime/)
- [Real Python - Collections](https://realpython.com/python-collections/)
- [Real Python - Cryptography](https://realpython.com/cryptography-python/)

---

## Perguntas Frequentes

### P: Qual exercício devo fazer primeiro?
**R:** Sempre comece pelo Nível 1. Eles aumentam em dificuldade.

### P: Preciso fazer todos os desafios extras?
**R:** Não obrigatório, mas recomendado para aprender mais.

### P: Posso modificar os exercícios?
**R:** Sim! Personalize de acordo com seus objetivos.

### P: Como faço para comparar com a solução?
**R:** Procure por comentários comentados no código.

### P: O que fazer se eu estiver preso?
**R:** Revise o tutorial e use `print()` para debugar.

---

## Contribuindo

Tem uma ideia para novo exercício?

1. Crie um arquivo `nivelX_seu_topico.py`
2. Siga o padrão dos outros exercícios
3. Adicione documentação clara
4. Teste completamente

---

**Boa sorte com os exercícios! 🚀**

Lembre-se: o melhor jeito de aprender é praticando! 🎓
