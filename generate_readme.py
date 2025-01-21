import os
import re

def gerar_readme_principal(caminho_repositorio):
    conteudo_readme_principal = "# Repositório de Guias e Tutoriais\n\nEste é o README principal do repositório, que lista todos os guias e tutoriais disponíveis.\n\n"
    
    arquivos_ordenados = []
    for arquivo in os.listdir(caminho_repositorio):
        if arquivo.endswith(".md") and arquivo != "README.md":
            match = re.match(r'^(\d+)-', arquivo)
            if match:
                numero = int(match.group(1))
                arquivos_ordenados.append((numero, arquivo))
            else:
                arquivos_ordenados.append((float('inf'), arquivo))
    
    arquivos_ordenados.sort(key=lambda item: item[0])
        
    for numero, arquivo in arquivos_ordenados:
        caminho_completo = os.path.join(caminho_repositorio, arquivo)
        caminho_relativo = os.path.relpath(caminho_completo, caminho_repositorio)
        try:
            with open(caminho_completo, "r", encoding="utf-8") as f:
                primeira_linha = f.readline().strip()
        except UnicodeDecodeError:
                primeira_linha = "Arquivo não pode ser lido ou está vazio"
        conteudo_readme_principal += f"- [{primeira_linha}]({caminho_relativo})\n"
            
    with open(os.path.join(caminho_repositorio, "README.md"), "w", encoding="utf-8") as arquivo_readme_principal:
        arquivo_readme_principal.write(conteudo_readme_principal)
            

if __name__ == "__main__":
    caminho_repositorio = "."
    gerar_readme_principal(caminho_repositorio)