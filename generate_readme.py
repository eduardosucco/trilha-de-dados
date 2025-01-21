# Importa o módulo 'os', que fornece funcionalidades para interagir com o sistema operacional
import os

# Define uma função chamada 'gerar_readme_principal' que recebe o caminho do repositório como argumento
def gerar_readme_principal(caminho_repositorio):
    # Inicializa a string que conterá o conteúdo do README principal
    conteudo_readme_principal = "# Repositório de Guias e Tutoriais\n\nEste é o README principal do repositório, que lista todos os guias e tutoriais disponíveis.\n\n"

    # Percorre todos os arquivos e diretórios dentro do caminho do repositório
    for diretorio_raiz, _, arquivos in os.walk(caminho_repositorio):
        # Percorre todos os arquivos dentro do diretório atual
        for arquivo in arquivos:
            # Verifica se o arquivo atual se chama "README.md" e se o diretório atual não é a raiz do repositório
            if arquivo == "README.md" and diretorio_raiz != caminho_repositorio:
                # Constrói o caminho relativo do arquivo README.md em relação à raiz do repositório
                caminho_relativo = os.path.relpath(os.path.join(diretorio_raiz, arquivo), caminho_repositorio)
                # Abre o arquivo README.md para leitura usando encoding utf-8
                with open(os.path.join(diretorio_raiz,arquivo),"r",encoding="utf-8") as f:
                    # Tenta ler a primeira linha do arquivo
                    try:
                        primeira_linha = f.readline().strip()
                    # Trata erro de leitura de caracteres que não fazem parte do padrão utf-8
                    except UnicodeDecodeError:
                         primeira_linha = "Arquivo não pode ser lido ou está vazio"
                # Adiciona uma linha ao conteúdo do README principal, com um link para o README secundário e sua primeira linha
                conteudo_readme_principal += f"- [{primeira_linha}]({caminho_relativo})\n"

    # Abre o arquivo "README.md" na raiz do repositório para escrita, usando encoding utf-8
    with open(os.path.join(caminho_repositorio, "README.md"), "w", encoding="utf-8") as arquivo_readme_principal:
        # Escreve o conteúdo gerado no arquivo README principal
        arquivo_readme_principal.write(conteudo_readme_principal)

# Verifica se o script está sendo executado diretamente (e não importado como um módulo)
if __name__ == "__main__":
    # Define o caminho para a raiz do repositório (pode ser alterado se necessário)
    caminho_repositorio = "."
    # Chama a função gerar_readme_principal, passando o caminho do repositório como argumento
    gerar_readme_principal(caminho_repositorio)