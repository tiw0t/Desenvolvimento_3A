"""
from controllers.livro_controller import LivroController

def main():
    db_config = {
        "dbname": "mvc_3a",
        "user": "postgres",
        "password": "30042007",
        "host": "localhost",
        "port": "5432"
    }

    livro_controller = LivroController(db_config)

    # Exemplo de uso
    livro_controller.adicionar_livro(
        1, "1984", "George Orwell ", 1949, "1234567890123")
"""
from views.livro_view import LivroView

def main():
    LivroView
if __name__ == "__main__":
    main()
