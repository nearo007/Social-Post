# Blog App

Este é um projeto de blog simples desenvolvido com **Django**. Os usuários podem se cadastrar, fazer login, criar postagens, editá-las, excluí-las e visualizar perfis de outros usuários.

---

## Tela Inicial

![Screenshot 2025-03-19 151349](https://github.com/user-attachments/assets/2ca0e0b4-28b4-4eba-ae67-c258fd0b9baf)

## Tela do Perfil do Usuário

![Screenshot 2025-03-19 153237](https://github.com/user-attachments/assets/93bc82ca-3a44-43d6-a764-d16988fd1dd3)

## Funcionalidades

### Página Inicial (`/`)
- Exibe todos os posts publicados.
- Os posts são mostrados em ordem cronológica reversa (mais recentes primeiro).
- Se o usuário estiver logado, seu perfil é carregado junto.

---

### Registro de Usuário (`/register`)
- Permite que novos usuários se registrem fornecendo:
  - Nome de usuário
  - E-mail
  - Senha (com confirmação)
- Valida:
  - Unicidade do nome de usuário e e-mail
  - Correspondência das senhas
- Cria um perfil com imagem e biografia padrão.

---

### Autenticação
#### Login (`/login`)
- Autentica usuários com nome de usuário e senha.
- Redireciona para a página inicial após login bem-sucedido.
- Exibe mensagens em caso de falhas.

#### Logout (`/logout`)
- Finaliza a sessão do usuário.

---

### Criar Post (`/create_post`)
- Apenas usuários autenticados podem criar posts.
- Valida:
  - Campos obrigatórios: título (máx. 50 caracteres) e conteúdo.
- Armazena a data de criação automaticamente.

---

### Editar Post (`/update_post/<post_id>`)
- Permite ao autor atualizar o título e o conteúdo do post.
- Marca o post como editado.
- Verifica se o título respeita o limite de 50 caracteres.

---

### Deletar Post (`/delete_post/<post_id>`)
- Apenas o autor do post pode deletá-lo.
- Após a exclusão, o usuário é redirecionado à página inicial.

---

### Perfil do Usuário (`/profile`)
- Exibe os posts criados pelo usuário autenticado.
- Mostra o número total de posts.

---

### Página de Usuário (`/user/<user_id>`)
- Exibe o perfil de qualquer outro usuário da plataforma.
- Caso o usuário tente acessar seu próprio perfil por essa rota, será redirecionado para `/profile`.
- Mostra os posts e o número total de publicações desse usuário.

---

### Página de Postagem (`/post/<post_id>`)
- Exibe os detalhes completos de um único post.

---

## Estrutura Padrão
- Autenticação usando `django.contrib.auth`
- Proteção de rotas com `@login_required`
- Upload automático de imagem de perfil padrão
- Uso de mensagens (`messages`) para feedback ao usuário
- Organização de templates por páginas funcionais (`index.html`, `register.html`, etc.)

---

## Modelos Usados
- `User` (do Django)
- `Post` (modelo customizado de postagens)
- `UserProfile` (perfil estendido do usuário)

---

## Pastas e Arquivos Importantes
- `views.py`: lógica principal das rotas e funcionalidades
- `models.py`: definição dos modelos `Post` e `UserProfile`
- `templates/`: arquivos HTML para as views
- `static/assets/img/user_default_profile.png`: imagem padrão de perfil

---

## Requisitos
- Python 3.x
- Django 4.x ou superior

---
