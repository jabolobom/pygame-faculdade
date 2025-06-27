# Setup para rodar

1. **Criar o ambiente**

   ```bash
   python -m .venv .venv
   ```

2. **Ativar ambiente virtual**
   **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

3. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

   **Sair do ambiente**

   ```bash
   deactivate
   ```

   **Rodar o código**

   ```bash
   cd src
   ```

   ```bash
   python3 .main.py
   ```

   ou

   ```bash
   python .main.py
   ```
