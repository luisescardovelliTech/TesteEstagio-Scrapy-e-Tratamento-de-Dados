import json
import datetime

with open('teste_estagio_instar.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

def limparEspacos(valor):
    if isinstance(valor, str):
        return valor.strip().replace('\xa0', ' ')
    return valor

def converterData(data_str):
    formatoSQL = ["%d/%m/%Y %H:%M:%S", "%d/%m/%Y"]
    for formatoAtual in formatoSQL:
        try:
            data = datetime.datetime.strptime(data_str, formatoAtual)
            return data.strftime("%Y-%m-%d %H:%M:%S")
        except:
            continue

def trocarMarcadores(titulo, data):
    if '...' in titulo:
        try:
            data = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            data_str = data.strftime("%d/%m/%Y")
            hora_str = data.strftime("%H:%M:%S")
            titulo = titulo.replace('...', data_str, 1)
            titulo = titulo.replace('...', hora_str, 1)
        except:
            pass
    return titulo

def listarString(lista):
    if isinstance(lista, list):
        return ' '.join(lista)
    return lista

def removeCampos(objeto):
    return {chave: valor for chave,
            valor in objeto.items() 
            if valor is not None}

dadosAtualizado = []

for item in dados:
    for chave in ['nome', 'sobrenome', 'titulo']:
        if chave in item:
            item[chave] = limparEspacos(item[chave])
    
    if 'dataRealizacao' in item:
        item['dataRealizacao'] = converterData(item['dataRealizacao'])
    
    if 'arquivos' in item:
        for arquivo in item['arquivos']:
            if 'data' in arquivo:
                arquivo['data'] = converterData(arquivo['data'])

    if 'titulo' in item and 'dataRealizacao' in item:
        item['titulo'] = trocarMarcadores(item['titulo'], item['dataRealizacao'])
    
    if 'descricao' in item:
        item['descricao'] = listarString(item['descricao'])
    
    item = removeCampos(item)

    if 'arquivos' in item:
        item['arquivos'] = [removeCampos(arquivo) for arquivo in item['arquivos']]

    dadosAtualizado.append(item) 

with open('dadosTratados.json', 'w', encoding='utf-8') as f:
    json.dump(dadosAtualizado, f, ensure_ascii=False, indent= 2)