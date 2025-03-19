import io 
import sys
import urllib.request as request
import os

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        try:
            output.write(response.read(BUFF_SIZE))
            print(f'Downloaded{((time * BUFF_SIZE)/ length) * 100:.2f}% \r', end='')
        except Exception as e:
            print(f'Erro durante o download: {e}')
            return 
    print('\n')

def download(response, output):
    total_downloaded = 0
    while True:
        try:
            data = response.read(BUFF_SIZE)
            if not data:
                break
            output.write(data)
            total_downloaded += len(data)
            print(f'Downloaded {total_downloaded} bytes \r', end='')
        except Exception as e:
            print(f'Erro durante o download: {e}')
            return
    print('\n')
def main():
    if len(sys.argv) != 2:
        print('Uso: python script.py <url>')
        return
    url = sys.argv[1]
    try:
        response = request.urlopen(url)
    except Exception as e:
        print('Erro ao abrir a URL: {e}')
        return
    
    filename = os.path.basename(url) # Extrai o nome do arquivo da URL
    if not filename:
        filename = 'downloaded_file'
    try:
        with open(filename, 'wb') as out_file:
            content_length = response.getheader('Content-Length')
            if content_length:
                length = int(content_length)
                download_length(response, out_file, length)
            else:
                download(response, out_file)
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')
        return
    finally:
        response.close()
    
    print('Finalizado com sucesso!{filename}')

if __name__ == '__main__':
    main()


