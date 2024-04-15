print("hola soy hash")
"""ALGORITMO
---Crear una clase
CAda elemento tiene atributo de:
    -clave
    -clave con hash
    -valor
Busqueda:
    -Con valor o clave, no lo se.
Insercion:
    -Con cualquier valor, tiene clave aun por definir
---Usar un objeto ya creado.
  """

class HashTable:
    def __init__(self, size):
        #inicia que valores? size y hashtable como lista de listas.
        self.size= size
        self.hash_table = self.create_buckets();
    def create_buckets(self):
        #retorna un valor
        return [[] for _ in range(self.size)]
    def set_val(self, key, value):
        #si no tiene key repetida, so agrega al final del x bucket
        #si tiene key repetida, se actualiza el valor
        #recorrido de algo
        keyhash = hash(key) % self.size
        bucket= self.hash_table[keyhash]

        isfound= False
        for index, content in enumerate(bucket):
            bkey, bvalue= content
            
            if bkey == key:
                isfound = True
                break
            
        if isfound:
            bucket[index] = (key, value)
        else:
            bucket.append((key,value))
            
    def __str__(self):
        return "".join(str(dupla) for dupla in self.hash_table)

hash_table= HashTable(10)
hash_table.set_val('isoncco@unsa.edu.pe','20')
print(hash_table)
print() 

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()


