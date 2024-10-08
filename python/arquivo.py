"""
Created on Wed Feb 28 23:13:36 2024

@author: luiz
"""
'''
import os
import struct

def read(path, inicio=0, nbytes=None):
  """
  Função que lê um arquivo completo e retorna uma lista de uint16 big endian.

  Args:
    path: String com o endereço do arquivo.
    inicio (opcional): Inteiro com o valor indicando onde começar a ler. Padrão: 0.
    nbytes (opcional): Inteiro com o número de bytes para ler. Padrão: ler o arquivo completo.

  Returns:
    dados: Lista de uint16 com os dados lidos do arquivo.
  """

  # Abrir o arquivo em modo binário
  with open(path, "rb") as arquivo:
    # Obter o tamanho do arquivo
    if nbytes is None:
      nbytes = os.path.getsize(path)

    # Posicionar o cursor no início da leitura
    arquivo.seek(inicio)
    # Ler os bytes do arquivo
    dados_bytes = arquivo.read(nbytes)

  # Converter os bytes em uma lista de uint16 big endian
  dados = []
  for i in range(0, len(dados_bytes), 2):
    valor_uint16 = struct.unpack(">H", dados_bytes[i:i+2])[0]  # Usando ">" para big endian
    dados.append(valor_uint16)

  # Retornar a lista de uint16
  return dados

def write(path, dados):
  # Abrindo o arquivo no modo binário para escrita.
  with open(path, "wb") as arquivo:
    # Convertendo a lista de inteiros para um objeto bytes em big endian.
    dados_bytes = struct.pack('>' + 'H' * len(dados), *dados)  # Usando struct.pack para big-endian
    # Gravando o objeto bytes no arquivo.
    arquivo.write(dados_bytes)

'''
import numpy as np
import os
import struct

def read(path, inicio=0, nbytes=None):
  """
  Função que lê um arquivo completo e retorna uma lista de uint16 little endian.

  Args:
    path: String com o endereço do arquivo.
    inicio (opcional): Inteiro com o valor indicando onde começar a ler. Padrão: 0.
    nbytes (opcional): Inteiro com o número de bytes para ler. Padrão: ler o arquivo completo.

  Returns:
    dados: Lista de uint16 com os dados lidos do arquivo.
  """

  # Abrir o arquivo em modo binário
  with open(path, "rb") as arquivo:
    # Obter o tamanho do arquivo
    if nbytes is None:
      nbytes = os.path.getsize(path)

    # Posicionar o cursor no início da leitura
    arquivo.seek(inicio)
    # Ler os bytes do arquivo
    dados_bytes = arquivo.read(nbytes)

  # Converter os bytes em uma lista de uint16 little endian
  dados = []
  for i in range(0, len(dados_bytes), 2):
    valor_uint16 = struct.unpack("<H", dados_bytes[i:i+2])[0]
    dados.append(valor_uint16)

  # Retornar a lista de uint16
  return dados

def write(path, dados):
  # Abrindo o arquivo no modo binário para escrita.
  with open(path, "wb") as arquivo:
    # Convertendo a lista de inteiros para um objeto bytes.
    dados_bytes = np.array(dados, dtype=np.uint16).tobytes()
    # Gravando o objeto bytes no arquivo.
    arquivo.write(dados_bytes)
