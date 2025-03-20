# Blog App

Este é um sistema simples de blog desenvolvido com Django, permitindo que usuários criem contas, façam login, publiquem posts e visualizem perfis de outros usuários.

## Funcionalidades

- **Página Inicial (`index`)**: Exibe todos os posts em ordem reversa (do mais recente para o mais antigo).
- **Registro (`register`)**: Permite que novos usuários se cadastrem, validando se o nome de usuário e o e-mail já estão em uso e se as senhas coincidem.
- **Login (`login`)**: Permite que os usuários façam login, autenticando suas credenciais e redirecionando para a página inicial.
- **Logout (`logout`)**: Faz o logout do usuário e o redireciona para a página inicial.
- **Criar Post (`create_post`)**: Permite que usuários autenticados criem posts, exigindo título e conteúdo.
- **Perfil do Usuário (`user_profile`)**: Mostra os posts do usuário logado e a contagem total de seus posts.
- **Página de Usuário (`user_page`)**: Exibe os posts de um usuário específico, desde que ele exista. Se for o próprio usuário logado, redireciona para o perfil.
- **Página do Post (`post_page`)**: Exibe um post específico baseado no seu ID.

O sistema implementa autenticação para garantir que apenas usuários logados possam criar posts ou visualizar perfis.

## Tecnologias Utilizadas
- **Django**: Framework principal para o desenvolvimento do back-end.
- **SQLite**: Banco de dados utilizado por padrão.
- **HTML, CSS**: Para a estrutura e estilização das páginas.

## Tela Inicial

![Screenshot 2025-03-19 151349](https://github.com/user-attachments/assets/2ca0e0b4-28b4-4eba-ae67-c258fd0b9baf)

## Tela do Perfil do Usuário

![Screenshot 2025-03-19 153237](https://github.com/user-attachments/assets/93bc82ca-3a44-43d6-a764-d16988fd1dd3)
