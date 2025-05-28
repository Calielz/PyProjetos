my_string = "hello world" #hash é uma função responsável por transformar dados em um valor de tamanho físico, bom para armazenamento seguro de dados como senhas, etc

 #apenas objetos de classes imutáveis podem ser hashables

# Calculate the hash value of the string
hash_value = hash(my_string)

# Print the string and its hash value
print("String: ", my_string)
print("Hash value: ", hash_value)