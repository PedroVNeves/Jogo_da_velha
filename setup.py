from setuptools import setup,find_packages

setup(
    name = 'jogo_da_velha_estrategia_aleatoria',
    version = '1.0',
    description = 'Jogo da Velha com estratégia aleatória',
    install_requires = ['tabulate','random'],
    packages = find_packages(),
    author = 'Pedro Neves',
    author_email = 'pedro.vasconcelosneves@gmail.com',
)