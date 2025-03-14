def xor(bytes1, bytes2):
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

# Valeurs chiffrées
c1 = 36090144755922289111874149912624586104827141550480778361069701468216394000169793076847790901596641569849475155408120250872696688660895686540
c2 = 44650713323251381086823566213137067535302450177582800043899613361403721543722305609301335578791112968915202037730763136493855017631800923382

# Convertir les entiers en bytes
c1_bytes = c1.to_bytes((c1.bit_length() + 7) // 8, 'big')
c2_bytes = c2.to_bytes((c2.bit_length() + 7) // 8, 'big')

# Message m2 connu
m2 = b'I can\'t believe that no one has thought of this scheme yet'

# Récupérer la clé en déchiffrant c2
# La clé utilisée pour c2 est k[1:] + k[:1]
# Donc, nous pouvons faire l'opération suivante
k_modified = xor(c2_bytes, m2)

# La clé `k` originale peut être récupérée en décalant le premier byte de `k_modified` à la fin
k_original = k_modified[1:] + k_modified[:1]

# Déchiffrer c1 pour récupérer le flag
flag = xor(c1_bytes, k_original)

# Afficher le résultat
print(flag.decode())
