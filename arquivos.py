# -*- coding:utf-8 -*-
'''
fopen

r   somente leitura
w   escrita (apaga e recria o arquivo caso ele exista)
a leitura e escrita (adiciona um novo conteúdo ao fim do arquivo)
r+  leitura e escrita
w+  escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
a+  leitura e escrita (abre o arquivo para atualização)

'''
w = open("arquivo2.txt", "a")
w.write("Esse é o meu arquivo\n") 
w.close()