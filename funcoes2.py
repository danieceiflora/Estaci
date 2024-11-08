def loginUsuario(perfil):
  if perfil.lower() == 'admin':
    print('Bem-vindo, Administrator')
  else:
    print('Bem-vindo, Usuário')

loginUsuario('ADMIN') 