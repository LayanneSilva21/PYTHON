import io
import zipfile
import sys
import os  # Importe o módulo os para verificar a existência do arquivo

def main(path): # Aceita o caminho do arquivo como argumento
    if not os.path.exists(path):
        print(f'Arquivo {path} não encontrado') # Usa f-string para melhor formatação
        sys.exit(-1)  # Saia com um código de erro
    else:
        try:
            with zipfile.ZipFile(path, 'r') as zfile: # Abre o arquivo zip em modo de leitura ('r') e usa 'with' para garantir o fechamento
                zfile.extractall()
                print('Arquivos extraídos para o diretório atual') # Informa o diretório de extração
        except zipfile.BadZipFile: # Trata exceções de arquivos zip corrompidos
            print(f'Arquivo {path} corrompido ou inválido')
            sys.exit(-1)
        except Exception as e: # Captura outras exceções
            print(f'Ocorreu um erro durante a extração: {e}')
            sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) != 2: # Verifica se o usuário forneceu o caminho do arquivo
        print('Uso: python script.py <caminho_do_arquivo.zip>')
        sys.exit(-1)
    path = sys.argv[1] # Obtem o caminho do arquivo do argumento da linha de comando
    main(path) # Chama a função main passando o caminho do arquivo