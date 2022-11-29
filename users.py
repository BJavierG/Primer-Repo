#diccionario en un diccionario

#tarea: crear dos nuevos diccionarios con dos o 3 nuevas personas,
#  eso guardarlo como una lista llamada personas.
#  luego hacer un loop para mostrar la info de cada persona.


users = {
    'lmessi':{
        'first':'leo',
        'last':'messi',
        'location':'paris'
    },
    'bgates':{
        'first':'bill',
        'last':'gates',
        'location':'sillicon valley'
    },
}

for username, user_info in users.items():
    print("\nUsername: "+username)
    fullname = user_info['first']+ " "+user_info['last']
    location = user_info['location']
    print("\tNombre Completo: "+fullname.title())
    print("\tLocación: "+location.title())