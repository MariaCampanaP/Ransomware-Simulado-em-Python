# ☕︎ Ransomware Simulado em Python

Este projeto contém uma simulação de **ransomware** utilizando a criptografia **AES** (Advanced Encryption Standard) para criptografar arquivos. O objetivos deste código é educacional e não deve ser utilizado para fins maliciosos.

## ☕︎ Funcionamento

O programa realiza as seguintes ações:

1. **Criptografar arquivos**;
   O código percorre todos os arquivos do diretório e os criptografa utilizando AES no 
   modo **CBC**. Arquivos já criptografados não são modificados.

2. **Descriptografar arquivos**;
   É possível descriptografar os arquivos criptografados, desde que a chave correta seja 
   fornecida.

## ☕︎ Como Usar

1. Clone este repositório para o seu computador ou utilize o Replit.

2. Instale as dependências necessárias:
   ```bash
   pip install pycryptodome

3. Execute o script ransomware_simulado.py
   Para rodar o script execute o seguinte comando:
   python ransomware_simulado.py

4. O código criptografará os arquivos no diretório atual (.). Para usar um diretório diferente, altere a variável diretorio no código:
   No código, procute pela linha:
   diretorio = '.' # o diretório atual.
   Altere o valor de diretorio para o caminho do diretório que deseja criptografar. Exemplo: diretorio = '/caminho/para/seu/diretorio'

5. Para testar a descriptografia:
   O código de descriptografia está comentado no final do script. Para testar a 
   descriptografia, descomente o trecho abaixo no código:
   ![image](https://github.com/user-attachments/assets/191b42b2-eb09-4c7a-b5db-dc0e1105518d)

6. O código descriptografará os arquivos .enc gerados e os restaurará ao seu formato original.






