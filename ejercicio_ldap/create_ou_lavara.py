def create_organizational_unit_ldif(filename, ou_name, base_dn):
    """Creates an LDIF file for an organizational unit."""

    ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "ou.ldif"  # Name of the LDIF file
ou_name = "directores"                   # Name of the organizational unit
base_dn = "dc=examenlavara,dc=org"   # Your base DN (replace with your actual DN)

ou_list = [
	"alumnos",
	"3esoA", "3esoB", "3esoC", "3esoD", "3esoE", "3esoF", "3esoG",
	"3bachA", "3bachB", "3bachC", "3bachD", "3bachE",
 	"GSasir1", "GSasir2",
	"GSdaw1", "GSdaw2"
]

create_organizational_unit_ldif(filename, ou_list, base_dn)



