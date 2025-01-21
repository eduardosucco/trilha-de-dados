import os
import re

def gerar_readme_principal(caminho_repositorio):
    conteudo_readme_principal = "# Repositório de Guias e Tutoriais\n\nEste é o README principal do repositório, que lista todos os guias e tutoriais disponíveis.\n\n"
    
    arquivos_ordenados = []
    for arquivo in os.listdir(caminho_repositorio):
        if arquivo.endswith(".md") and arquivo != "README.md":
            match = re.match(r'^(\d+)-(.*)\.md$', arquivo)
            if match:
                numero = int(match.group(1))
                titulo = match.group(2).replace("-", " ").strip()
                arquivos_ordenados.append((numero, titulo, arquivo))
            else:
                titulo = arquivo[:-3].replace("-", " ").strip()
                arquivos_ordenados.append((float('inf'), titulo, arquivo))
    
    arquivos_ordenados.sort(key=lambda item: item[0])
        
    for numero, titulo, arquivo in arquivos_ordenados:
        caminho_completo = os.path.join(caminho_repositorio, arquivo)
        caminho_relativo = os.path.relpath(caminho_completo, caminho_repositorio)
            
        conteudo_readme_principal += f"- {numero if numero != float('inf') else ''} **{titulo}** 📚  ([Leia mais]({caminho_relativo}))\n"

    with open(os.path.join(caminho_repositorio, "README.md"), "w", encoding="utf-8") as arquivo_readme_principal:
        arquivo_readme_principal.write(conteudo_readme_principal)
            

if __name__ == "__main__":
    caminho_repositorio = "."
    gerar_readme_principal(caminho_repositorio)