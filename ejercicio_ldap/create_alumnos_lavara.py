def generate_alumnos_ldif(filename, base_dn, group_gid=10000):
    """
    Crea 2000 registros LDIF de usuarios tipo alumno que pertenecen al grupo alumnos.
    """
    ldif = ""
    for i in range(1, 2001):
        uid = f"alumno{i:04d}"
        cn = f"Alumno {i}"
        sn = f"{i}"
        user_dn = f"uid={uid},ou=alumnos,{base_dn}"

        ldif += f"""dn: {user_dn}
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
cn: {cn}
sn: {sn}
uid: {uid}
uidNumber: {2000 + i}
gidNumber: {group_gid}
homeDirectory: /home/{uid}
loginShell: /bin/bash
userPassword: alumno123

"""

    try:
        with open(filename, "w") as f:
            f.write(ldif)
            print(f"Archivo LDIF '{filename}' creado con éxito con 2000 alumnos.")
    except Exception as e:
        print(f"Error creando archivo LDIF: {e}")


# Parámetros
filename = "alumnoslavara.ldif"
base_dn = "dc=examenlavara,dc=org"  # Asegúrate de usar tu DN real

# Ejecutar función
generate_alumnos_ldif(filename, base_dn)
