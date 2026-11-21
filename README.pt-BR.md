# Recruiting OS

[English](README.en.md) · [Español](README.md) · **Português**

Um sistema para conduzir processos seletivos com o **Claude Code** e com critério: a reunião de alinhamento com o gestor da vaga, um scorecard que dá para avaliar, cada candidato comparado com esse scorecard, as entrevistas, a shortlist, os retornos e um painel que diz o que fazer hoje. Tudo fica em pastas no computador da consultoria.

Foi pensado para **consultorias boutique e recrutadores independentes da América Latina** que fazem processos de **Produto** e de **Atendimento ao Cliente** (liderança e especialistas) em empresas de tecnologia. Não está calibrado para recrutamento em massa nem para vagas de Tecnologia ou Design.

É o outro lado do [busqueda-laboral-os](https://github.com/JuanLoredo6/busqueda-laboral-os), o sistema para pessoas em busca de emprego.

> **Idioma:** o Claude conversa com a consultoria em **português do Brasil** se ela escrever em português ou escolher esse idioma ao começar. Também escreve cada anúncio de vaga, mensagem ou roteiro de entrevista no idioma de quem vai ler: português, espanhol ou inglês. Por dentro, os comandos, os skills, os modelos e o painel continuam em espanhol: comandos como `/empezar` têm nome em espanhol, mas você pode pedir tudo com as suas palavras, em português.

## Como funciona

- **A IA prepara, as pessoas decidem.** Nenhuma pontuação descarta ninguém. Cada candidato é avaliado contra o scorecard, critério por critério, com evidência: ✅ atende · 🟡 parcial · ❌ não atende · ❓ falta saber.
- **Avaliação cega no que é protegido.** Idade, gênero, origem, foto, estado civil ou saúde não entram em nenhuma avaliação. Se um cliente pede algo assim («boa aparência», «até 35 anos»), o sistema sinaliza e propõe um requisito baseado em comportamento.
- **Dados de terceiros, em ordem.** Cada candidato tem registrado o consentimento e a data em que seus dados são apagados. `/privacidad` revisa o que venceu. CPF, RG e dados bancários nunca são guardados.
- **Nada é enviado sozinho.** O Claude escreve mensagens, anúncios, retornos e relatórios; quem envia é uma pessoa. Um hook pede confirmação antes de qualquer envio ou alteração no Gmail, Calendar, Drive ou Sheets, mesmo no modo automático. Não automatiza o LinkedIn.
- **Limites escritos e testados.** As regras que nunca se quebram estão numeradas no `CLAUDE.md` (L1 a L15). Testes automáticos (`evals/`) as verificam com uma consultoria fictícia antes de cada versão.
- **Todo candidato recebe um retorno.** O painel marca os atrasados.

---

## Instalação assistida

Você precisa de um plano do Claude que inclua o Claude Code e do **app de desktop do Claude** ([claude.com/download](https://claude.com/download)). Para uma consultoria com mais de uma pessoa, recomendamos um plano **Team** ou **Enterprise**. Não precisa saber programar.

1. Abra o app, aba **Code**, e escolha a sua pasta **Documentos** como pasta de trabalho.
2. Cole este pedido:

```
Instale o Recruiting OS seguindo, etapa por etapa, o guia https://raw.githubusercontent.com/JuanLoredo6/recruiting-os/main/INSTALACION.md. Fale comigo em português do Brasil.
```

Se na sua rede o Claude não conseguir baixar do GitHub, baixe o [ZIP](https://github.com/JuanLoredo6/recruiting-os/archive/refs/heads/main.zip) pelo navegador, deixe em Documentos e peça: «Instale o Recruiting OS a partir do ZIP que deixei em Documentos». O guia completo está em **[INSTALACION.md](INSTALACION.md)** (em espanhol; o Claude explica em português).

Ao terminar, na pasta do sistema, escreva:

```
/empezar
```

### Problemas frequentes

| O que acontece | O que fazer |
|---|---|
| Escrevo `/empezar` e não aparece | O Claude Code está aberto em outra pasta. Abra uma sessão nova **na pasta do sistema** (a que tem o `CLAUDE.md` dentro) |
| O painel diz «Todavía no hay datos» | Rode `/empezar` primeiro. Se já rodou, peça ao Claude: «regenere o painel» |
| O painel não atualiza | Recarregue a página (F5). Se continuar igual, peça ao Claude: «rode tablero/sincronizar.sh» |
| `/sincronizar-correo` diz que falta um conector | Toque no **+** ao lado da caixa de mensagem → conectores → Gmail ou Google Calendar → Conectar. Depois abra uma sessão nova |
| `/vista-cliente` diz que falta um conector | O mesmo, com o **Google Drive** (e o **Google Sheets**, se aparecer separado), com a conta da consultoria |
| Não sei o que fazer agora | Pergunte ao Claude «o que eu faço agora?» ou escreva `/mapa-de-skills` |

---

## Como se usa

| Quando | O que você diz ao Claude |
|---|---|
| A primeira vez | `/empezar` |
| Antes de aceitar um processo | `/mapeo-de-mercado` |
| Antes do alinhamento com o gestor | `/nueva-busqueda` (monta o roteiro) |
| Depois do alinhamento, com as notas ou a transcrição | `/nueva-busqueda` (perfil da vaga e scorecard) |
| Para sair buscando | `/pitch-del-rol`, `/redactar-aviso`, `/plan-de-sourcing` |
| Cada currículo ou perfil | `/evaluar-candidato` |
| Antes de uma entrevista | `/guia-de-entrevista` (perguntas de comportamento com aprofundamento em STAR-L) |
| Depois de uma entrevista | `/registrar-entrevista` |
| Quando algo acontece («X respondeu», «o cliente descartou Y») | Conte ao Claude, ou `/actualizar` |
| Para trazer o que chegou por e-mail ou na agenda | 🔄 SYNC no painel, ou `/sincronizar-correo` |
| Para escrever a um candidato ou ao cliente | `/redactar-mensaje` |
| Quando há finalistas | `/armar-terna` |
| Se você compartilha o andamento com o cliente no Google Sheets e Drive | `/vista-cliente` |
| Às sextas | `/reporte-semanal` |
| Quando um processo trava | `/diagnostico-proceso` |
| Para ver tudo o que existe | `/mapa-de-skills` |

Não precisa lembrar os nomes: se você pedir algo com as suas palavras, o Claude escolhe o skill certo.

O painel (`tablero/tablero.html`) abre com dois cliques e mostra o que fazer hoje, o que a sincronização trouxe para revisar, os alertas (retornos atrasados, processos parados, dados que já devem ser apagados), a carteira de processos e o pipeline de candidatos. Os rótulos do painel estão em espanhol.

---

## Os dados

- Os dados da consultoria, dos clientes e dos candidatos ficam **só no computador** de cada pessoa. O `.gitignore` evita que subam para o GitHub por engano.
- Este repositório é público e traz **só o sistema**: skills, modelos e painel, sem dados de ninguém.
- **A sua cópia, por outro lado, tem dados de candidatos: não suba para um repositório público.** Se quiser backup, use uma nuvem da empresa ou um repositório **privado**.
- `contexto/privacidad.md` é um ponto de partida, não assessoria jurídica: revise com quem assessora a consultoria nos países onde trabalha (no Brasil, a LGPD).
- **Com a visão do cliente (opcional),** uma parte sai do computador de propósito: os candidatos que aceitaram ser apresentados, com a avaliação e um currículo sem dados pessoais, vão para uma pasta do Drive da consultoria compartilhada com e-mails específicos do cliente. Nada é publicado nem compartilhado sem o seu OK.

## Atualizar o sistema

Quando houver melhorias, peça ao Claude «atualize o sistema» ou rode `git pull`. Os seus dados não são tocados. O que mudou em cada versão está no [CHANGELOG.md](CHANGELOG.md) (em espanhol) e nas [releases](https://github.com/JuanLoredo6/recruiting-os/releases).

## Créditos

- Sistema montado por Juan Rodríguez Loredo. Licença MIT: veja [LICENSE](LICENSE).
- Várias partes são adaptações dos skills de produto de **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills)) e de **Paweł Huryn** ([pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) e [pm-brain](https://github.com/phuryn/pm-brain)), ambos com licença MIT. Detalhes em [CREDITOS.md](CREDITOS.md).
