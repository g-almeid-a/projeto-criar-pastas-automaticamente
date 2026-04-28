# 💾 Backup Tool

Ferramenta simples e automatizada para criação de estrutura de pastas de backup padrão.

---

## 📌 Sobre o projeto

O **Backup Tool** é um programa desenvolvido em Python que cria automaticamente uma estrutura de diretórios para organização de backups, evitando erros manuais e padronizando o processo.

Ideal para uso interno em empresas ou uso pessoal.

---

## 🧱 Estrutura criada

Ao executar o programa, será criada a seguinte estrutura:

```
backup/
│
├── Disco C/
├── Email/
├── Programas/
└── User/
    ├── Area de trabalho/
    ├── documentos/
    ├── download/
    └── imagens/
```

---

## ⚙️ Como funciona

O sistema:

* Detecta automaticamente o local onde está sendo executado
* Cria a pasta `backup` no mesmo diretório
* Gera subpastas com base em um arquivo de configuração (`config.json`)

---

## 📂 Estrutura do projeto

```
Backup_tool/
│
├── main.py          # Arquivo principal
├── estrutura.py     # Lógica de criação das pastas
├── utils.py         # Funções auxiliares
├── config.json      # Configuração da estrutura
└── dist/
    └── main.exe     # Executável gerado
```

---

## ▶️ Como executar o programa

### 🔹 Opção 1 — Executável (.exe)

1. Vá até a pasta onde está o arquivo `main.exe`
2. Certifique-se de que o arquivo `config.json` está na mesma pasta
3. Dê duplo clique no `main.exe`

✔️ A pasta `backup` será criada automaticamente

---

### 🔹 Opção 2 — Rodar pelo terminal

Abra o terminal na pasta do projeto e execute:

```
python main.py
```

---

## ⚠️ Observações importantes

* O arquivo `config.json` deve estar sempre na mesma pasta do executável
* O programa cria as pastas no mesmo local onde está sendo executado
* Caso a pasta já exista, ela não será sobrescrita

---

## 🧪 Tecnologias utilizadas

* Python 3
* pathlib
* PyInstaller (para gerar o executável)

---

## 🚀 Gerar o executável

Para gerar o `.exe`, utilize:

```
pyinstaller --onefile --clean --icon=icone.ico --add-data "config.json;." main.py
```

---

## 📈 Possíveis melhorias

* Interface gráfica (GUI)
* Seleção de diretório de destino
* Sistema de logs
* Versionamento automático de backups
* Instalador completo (setup.exe)

---

## 👨‍💻 Autor

Gabriel Almeida

---

## 📄 Licença

Este projeto é livre para uso e modificação.