n1 = int(input('Digite um número = '))
n2 = int(input('Digite outro número = '))
soma = n1 + n2
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'magenta' : '\033[35m'}
 
print('A soma de {0}{1}{2} e {0}{3}{2} é igual a {4}{5}{2}.'.format(cores['azul'],n1, cores['limpa'], n2, cores['magenta'], soma))





