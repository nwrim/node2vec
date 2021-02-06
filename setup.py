import setuptools

setuptools.setup(
    name="node2vec_mod",
    version="0.0.1",
    author="nwrim",
    author_email=" ",
    description="modifying node2vec for my purposes",
    url="https://github.com/nwrim/node2vec",
    packages=setuptools.find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'gensim',
    ],
)
