# Fluxos de Navegação

> Mapa completo de como o usuário se move entre as telas do app.

---

## Estrutura de Navegação Principal

```
┌─────────────────────────────────────────────────────┐
│                   APP NAVIGATION                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  [Não autenticado]          [Autenticado]            │
│                                                      │
│  Splash                     Tab Bar                  │
│    ↓                        ├── Home / Dashboard     │
│  Login ←──────────────────→ ├── Treinos              │
│    ↓                        ├── Rotinas              │
│  Dashboard                  ├── Avaliações           │
│                             └── Perfil               │
└─────────────────────────────────────────────────────┘
```

---

## Fluxo 1 — Autenticação

```
[Splash Screen]
    │
    ├── Usuário JÁ logado → [Dashboard / Home]
    │
    └── Usuário NÃO logado
            │
            ↓
        [Login]
            │
            ├── Login com sucesso → [Dashboard]
            │
            ├── "Esqueci senha" → [Recuperar Senha]
            │       ↓
            │   Insere e-mail → E-mail enviado
            │       ↓
            │   [Redefinir Senha] (via link no e-mail)
            │       ↓
            │   Senha redefinida → [Login]
            │
            └── "Criar conta" → [Cadastro]
                    │
                    ├── Cadastro concluído → [Onboarding]
                    │       ↓
                    │   [Boas-vindas]
                    │       ↓
                    │   [Dados Pessoais]
                    │       ↓
                    │   [Objetivo / Meta]
                    │       ↓
                    │   [Nível de Experiência]
                    │       ↓
                    │   [Dashboard]
```

---

## Navegação Bottom Tab Bar

> Visível apenas para usuários autenticados

| Tab | Ícone | Tela |
|---|---|---|
| 1 | 🏠 Home | Dashboard |
| 2 | 💪 Treinos | Lista de Treinos |
| 3 | 📋 Rotinas | Lista de Rotinas |
| 4 | 📊 Evolução | Avaliações / Gráficos |
| 5 | 👤 Perfil | Meu Perfil |

---

## Modais e Sheets Recorrentes

| Modal | Disparado por | Conteúdo |
|---|---|---|
| Seleção de Exercício | Criar/Editar Rotina | Catálogo com busca e filtros |
| Timer de Descanso | Concluir série | Contador regressivo com som |
| Confirmar Saída | Botão voltar durante treino | "Deseja pausar ou abandonar?" |
| Seletor de Tipo de Avaliação | FAB "Nova avaliação" em `[VELA-2001]` | Anamnese / Antropométrica / Dobras Cutâneas / Bioimpedância |
| Confirmar Exclusão de Avaliação | Menu ⋮ → "Excluir" em `[VELA-2001]`/`[VELA-2002]` | "Excluir esta avaliação? Esta ação não pode ser desfeita." |

---

## Fluxo 3 — Perfil do Aluno

```
[Meu Perfil]  ← Tab Bar (ícone Perfil)
    │
    ├── Toque na foto → [Modal: Atualizar Foto]
    │       ↓
    │   Câmera / Galeria → foto salva → [Meu Perfil]
    │
    ├── Card "Dados Pessoais" → [Editar Perfil]
    │       │
    │       ├── Salvar com sucesso → [Meu Perfil]
    │       └── Voltar (sem salvar) → alerta "Descartar?" → [Meu Perfil]
    │
    ├── Card "Avaliações" → [Lista de Avaliações VELA-2001]
    │       │   (também acessível pela Tab Bar — aba Avaliações/Evolução)
    │       │   Detalhe completo de papéis/status no Fluxo 4
    │       │
    │       ├── [TREINADOR] FAB "Nova avaliação" → seletor de tipo → [VELA-2003]
    │       │       (Salvar=Concluída ou Liberar=Solicitada para o aluno preencher)
    │       ├── [TREINADOR] Card → "Editar" → [VELA-2003] ; menu ⋮ "Excluir" (definitivo)
    │       ├── [ALUNO] Card "Solicitada" → "Preencher" → [VELA-2003] → Enviar (trava)
    │       └── [AMBOS] Card → "Visualizar" → [Visualizar Avaliação VELA-2002]
    │
    └── Card "Minha Dieta" (Pós-MVP) → [Minha Dieta]
            │
            └── "Ver histórico" → [Histórico de Dietas]
```

> ⚠️ Fluxo do Personal Trainer (como acessa o perfil do aluno) ainda não mapeado — aguarda decisão sobre vínculo PT-Aluno.

---

## Fluxo 4 — Avaliações (lista única, multi-tipo)

```
[Lista de Avaliações VELA-2001]  ← Tab Bar (Avaliações/Evolução) ou Perfil
    │   • Reúne TODOS os tipos, ordenados por data (mais recente no topo)
    │   • Cards distintos por tipo (Anamnese / Antropométrica / Dobras / Bioimpedância)
    │   • Cada card tem STATUS: Solicitada / Em andamento / Concluída / Expirada
    │   • Filtro por período (30d / 3m / 6m / 12m / Tudo / Personalizado) + por tipo
    │
    ├── [TREINADOR] FAB "Nova avaliação" → seletor de tipo → [Cadastro/Edição VELA-2003]
    │       ├── "Salvar" → Concluída → volta para [VELA-2001]
    │       └── "Liberar para o aluno preencher" → Solicitada → volta para [VELA-2001]
    │               └── dispara NOTIFICAÇÃO (push + in-app) ao Aluno
    │                   + pendência em destaque no topo da aba + badge na Tab Bar
    │
    ├── [ALUNO] Notificação "avaliação para preencher" → abre [VELA-2001]
    │       (pendências fixas no topo, seção "Para preencher (N)") ou direto [VELA-2003]
    │
    ├── [TREINADOR] Card → "Editar" → [Cadastro/Edição VELA-2003] (preenchido) → Salvar
    │
    ├── [ALUNO] Card "Solicitada" → "Preencher" → [Cadastro/Edição VELA-2003]
    │       └── "Enviar" → status vira Concluída e TRAVA p/ o aluno → volta para [VELA-2001]
    │
    ├── [AMBOS] Card → "Visualizar" → [Visualizar Avaliação VELA-2002] (somente leitura)
    │       ├── [TREINADOR] "Editar" → [VELA-2003] ; menu ⋮ "Excluir" → confirmação
    │       └── [ALUNO] "Preencher" (se Solicitada) → [VELA-2003]
    │
    └── [TREINADOR] Card → menu ⋮ → "Excluir" → confirmação (DEFINITIVA, sem lixeira)
```

**Regra de papéis:**

```
TREINADOR  → cria, edita, exclui (definitivo) e libera/solicita avaliações
ALUNO      → apenas VISUALIZA; e PREENCHE as Solicitadas liberadas a ele
             (após ENVIAR, a avaliação vira Concluída e trava — só o Treinador altera)
```

> Bidirecionalidade: `[VELA-2001]` ↔ `[VELA-2003]` (criar/editar/preencher) e `[VELA-2001]` ↔ `[VELA-2002]` (visualizar); de `[VELA-2002]` o Treinador vai para editar e o Aluno para preencher (se Solicitada), e voltam. Telas futuras **Comparar Avaliações** e **Evolução/Gráficos** partirão de `[VELA-2001]`/`[VELA-2002]`.

---

## ⚠️ Pontos Pendentes de Definição

- Haverá deep link por notificação push? (ex: lembrete de treino)
- Como funciona a navegação entre tabs durante um treino ativo?
- Haverá onboarding de feature (tooltips) além do onboarding inicial?
- Como Personal Trainer navega para o perfil de um aluno vinculado?
- Como Nutricionista acessa o app para cadastrar dietas?
