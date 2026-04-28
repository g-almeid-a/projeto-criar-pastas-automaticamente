# 💾 Backup Tool

Ferramenta automatizada para criação de estrutura de pastas de backup de forma rápida, padronizada e sem erros manuais.

---

## 📌 Sobre o projeto

O **Backup Tool** é um programa desenvolvido em Python que cria automaticamente uma estrutura de diretórios para organização de backups.

O objetivo é facilitar o processo de padronização de backups, podendo ser utilizado tanto em ambientes pessoais quanto corporativos.

---

## 🧱 Estrutura criada

Ao executar o programa, será criada automaticamente a seguinte estrutura:

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
* Gera subpastas com base no arquivo `config.json`
* Evita recriar pastas já existentes

---

## 📂 Estrutura do projeto

```
Backup_tool/
│
├── main.py          # Arquivo principal
├── estrutura.py     # Lógica de criação das pastas
├── utils.py         # Funções auxiliares
├── config.json      # Configuração da estrutura
├── build.bat        # Script para gerar o executável automaticamente
├── icone.ico        # Ícone personalizado do executável
└── dist/
    └── main.exe     # Executável gerado
```

---

## ▶️ Como executar

### 🔹 Executável (.exe)

1. Vá até a pasta onde está o `main.exe`
2. Certifique-se de que o arquivo `config.json` está na mesma pasta
3. Execute o `main.exe`

✔️ A pasta `backup` será criada automaticamente

---

### 🔹 Rodar pelo Python

No terminal:

```
python main.py
```

---

## ⚙️ Automação de build (build.bat)

O projeto possui um arquivo `build.bat` que automatiza a geração do executável.

Ao executá-lo, o sistema:

* 🧹 Remove builds antigos (`build/`, `dist/`, `.spec`)
* 🔄 Gera um novo executável atualizado
* 🎨 Aplica automaticamente o ícone personalizado

### ▶️ Como usar

1. Abra o projeto no VS Code
2. Execute o arquivo `build.bat`

✔️ Isso garante um `.exe` sempre limpo e atualizado

---

## 🚀 Gerar executável manualmente

Caso queira gerar manualmente:

```
pyinstaller --onefile --clean --icon=icone.ico --add-data "config.json;." main.py
```

---

## ⚠️ Observações importantes

* O arquivo `config.json` deve estar na mesma pasta do executável
* O programa cria as pastas no local onde está sendo executado
* O executável pode ser movido para qualquer diretório

---

## 🧪 Tecnologias utilizadas

* Python 3
* pathlib
* PyInstaller

---

## 📈 Possíveis melhorias

* Interface gráfica (GUI)
* Escolha do diretório de destino
* Sistema de logs
* Versionamento de backups
* Instalador completo (setup.exe)

---

## 👨‍💻 Autor

Gabriel Almeida

---

## 📄 Licença

Este projeto é livre para uso e modificação.
