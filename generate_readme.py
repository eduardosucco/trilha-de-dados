import os

def generate_main_readme(repo_path):
    main_readme_content = "# Repositório de Guias e Tutoriais\n\nEste é o README principal do repositório, que lista todos os guias e tutoriais disponíveis.\n\n"
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file == "README.md" and root != repo_path:
                relative_path = os.path.relpath(os.path.join(root, file), repo_path)
                with open(os.path.join(root,file),"r",encoding="utf-8") as f:
                    try:
                        first_line = f.readline().strip()
                    except UnicodeDecodeError:
                         first_line = "Arquivo não pode ser lido ou está vazio"
                main_readme_content += f"- [{first_line}]({relative_path})\n"

    with open(os.path.join(repo_path, "README.md"), "w", encoding="utf-8") as main_readme_file:
        main_readme_file.write(main_readme_content)

if __name__ == "__main__":
    repo_path = "."  # Caminho para a raiz do repositório (pode ser alterado se necessário)
    generate_main_readme(repo_path)