# honeypot
#Seguridad informatica y encripacion


# Prerrequisitos
1. Python3
2. Instalar Paramiko
3. Crear llave key-gen

```
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): key
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in key
Your public key has been saved in key.pub
The key fingerprint is:
SHA256:lentMl/0Ly3auDS+sUtCOfTdtfnKAFEKgTKSsfPGXdQ root@localhost
The key's randomart image is:
+---[RSA 3072]----+
|  .o   .+o  .    |
|  o.o .. .E=     |
|  o. o  . B     .|
|   + . . + = . .+|
|    + . S * o oo.|
|   .     . + . ..|
|          + B ..o|
|           O Xo.o|
|            X=+o.|
+----[SHA256]-----+
root@localhost:~/honeypot# 
```

4. Invocar el honeypot.py