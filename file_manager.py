class FileManager:
    def __init__(self, file_path):
        """
        Initialisation de la classe FileManager avec le chemin du fichier.
        :param file_path: Chemin du fichier à manipuler.
        """
        self.file_path = file_path

    def read_file(self):
        """
        Lit et affiche le contenu du fichier.
        """
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")

    def write_to_file(self, data):
        """
        Écrit des données dans le fichier.
        :param data: Données à écrire dans le fichier.
        """
        with open(self.file_path, 'a') as file:
            file.write(data + '\n')

    def count_lines(self):
        """
        Retourne le nombre de lignes dans le fichier.
        :return: Nombre de lignes dans le fichier.
        """
        try:
            with open(self.file_path, 'r') as file:
                return len(file.readlines())
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")
            return 0

    def search_keyword(self, keyword):
        """
        Recherche un mot-clé dans le fichier et affiche les lignes correspondantes.
        :param keyword: Mot-clé à rechercher dans le fichier.
        """
        try:
            with open(self.file_path, 'r') as file:
                found = False
                for line in file:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print(f"Aucune ligne contenant le mot-clé '{keyword}' n'a été trouvée.")
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")

    def add_and_search_keyword(self, new_line, keyword):
        """
        Ajoute une nouvelle ligne dans le fichier et cherche ensuite un mot-clé.
        :param new_line: Nouvelle ligne à ajouter.
        :param keyword: Mot-clé à rechercher dans le fichier.
        """
        self.write_to_file(new_line)  # Ajouter une nouvelle ligne
        print(f"La ligne suivante a été ajoutée : '{new_line}'")
        
        print(f"Recherche des lignes contenant le mot-clé '{keyword}':")
        self.search_keyword(keyword)  # Recherche du mot-clé


def display_menu():
    print("\nMenu :")
    print("1. Chercher un mot-clé")
    print("2. Ajouter une nouvelle ligne")
    print("3. Lire tout le contenu du fichier")
    print("4. Compter le nombre de lignes dans le fichier")
    print("5. Quitter")


def main():
    file_manager = FileManager("log.txt")

    while True:
        display_menu()
        choice = input("Choisissez une option (1-5) : ")

        if choice == '1':
            keyword = input("Entrez le mot-clé à rechercher : ")
            file_manager.search_keyword(keyword)
        elif choice == '2':
            new_line = input("Entrez la nouvelle ligne à ajouter : ")
            file_manager.write_to_file(new_line)
            print(f"La ligne suivante a été ajoutée : '{new_line}'")
        elif choice == '3':
            print("Contenu du fichier :")
            file_manager.read_file()
        elif choice == '4':
            line_count = file_manager.count_lines()
            print(f"Le fichier contient {line_count} lignes.")
        elif choice == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
